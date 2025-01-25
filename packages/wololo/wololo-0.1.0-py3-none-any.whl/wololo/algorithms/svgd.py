import math

import torch
from tqdm import tqdm

from ..converters import Converter


class ParticleParam(torch.nn.modules.lazy.LazyModuleMixin, torch.nn.Module):
    """
    A module to represent stochastic parameter particles for particle-based inference.

    Args:
        parameter (torch.Tensor): The parameter to be modeled with particles.
    """

    def __init__(self, parameter):
        super().__init__()
        self.prior = torch.distributions.Normal(
            loc=parameter, scale=torch.full(parameter.size(), 1.0)
        )
        self.register_parameter("particles", torch.nn.UninitializedParameter())
        self.einsum_equations = {}

    def initialize_parameters(self, n_samples: int) -> None:
        if self.has_uninitialized_params():
            self.particles.materialize((n_samples, *self.prior.loc.shape))

        with torch.no_grad():
            self.particles = torch.nn.Parameter(
                self.prior.rsample(
                    (n_samples,),
                )
            )

    @property
    def flattened_particles(self) -> torch.Tensor:
        return torch.flatten(self.particles, start_dim=1)

    def general_product(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        ndim_B = B.ndim
        if ndim_B not in self.einsum_equations:
            suffix = "".join([chr(ord("k") + i) for i in range(ndim_B - 1)])
            self.einsum_equations[ndim_B] = f"ij,j{suffix}->i{suffix}"
        equation = self.einsum_equations[ndim_B]
        return torch.einsum(equation, A, B)

    def perturb_gradients(self, kernel_matrix: torch.Tensor) -> None:
        """
        Modifies particle gradients multiplying them by the kernel matrix
        to reflect particle interactions.

        Args:
            kernel_matrix (torch.Tensor): Kernel matrix encoding pairwise distances.
        """
        self.particles.grad = self.general_product(kernel_matrix, self.particles.grad)

    def forward(self, n_samples):
        """
        Forward pass returning the particles.

        Args:
            n_samples (int): Number of particle realizations.

        Returns:
            torch.Tensor: The particles.
        """
        return self.particles


def initialize_particles(module: torch.nn.Module, n_particles: int) -> None:
    """
    Initialize particles for all `ParticleParam` submodules in the model.

    Args:
        module (torch.nn.Module): The model containing `ParticleParam` submodules.
        n_particles (int): Number of particles to initialize for each submodule.
    """
    module.n_particles = n_particles
    module.particle_modules = [
        submodule
        for submodule in module.modules()
        if isinstance(submodule, ParticleParam)
    ]


def named_particles(module: torch.nn.Module):
    """
    Yield named particles for all `ParticleParam` submodules.

    Args:
        module (torch.nn.Module): The model containing `ParticleParam` submodules.

    Yields:
        Tuple[str, torch.Tensor]: Name and tensor of particles.
    """
    for name, submodule in module.named_modules():
        if isinstance(submodule, ParticleParam):
            yield name, submodule.particles
        else:
            for param_name, param in submodule.named_parameters(recurse=False):
                expanded_param = param.unsqueeze(0).expand(
                    module.n_particles, *param.size()
                )
                yield f"{name}.{param_name}", expanded_param


def all_particles(module: torch.nn.Module) -> torch.Tensor:
    """
    Concatenate all particles into a single tensor.

    Args:
        module (torch.nn.Module): The model containing `ParticleParam` submodules.

    Returns:
        torch.Tensor: Flattened and concatenated particles from all submodules.
    """
    return torch.cat(
        [torch.flatten(tensor, start_dim=1) for _, tensor in module.named_particles()],
        dim=1,
    )


def compute_kernel_matrix(module: torch.nn.Module) -> None:
    """
    Computes the RBF kernel matrix for the particles in the model.

    Args:
        module (torch.nn.Module): The model containing particles.
    """
    particles = module.all_particles()
    pairwise_sq_dists = torch.cdist(particles, particles, p=2) ** 2
    median_squared_dist = pairwise_sq_dists.median()
    lengthscale = torch.sqrt(0.5 * median_squared_dist / math.log(module.n_particles))
    module.kernel_matrix = torch.exp(-pairwise_sq_dists / (2 * lengthscale**2))


def perturb_gradients(module: torch.nn.Module) -> None:
    """
    Adjust gradients of all particles in the model using the kernel matrix.

    Args:
        module (torch.nn.Module): The model containing particles.
    """
    module.compute_kernel_matrix()
    for particle in module.particle_modules:
        particle.perturb_gradients(module.kernel_matrix)


toplevel_methods = {
    "named_particles": named_particles,
    "all_particles": all_particles,
    "compute_kernel_matrix": compute_kernel_matrix,
    "perturb_gradients": perturb_gradients,
    "initialize_particles": initialize_particles,
}


def SVGD(
    starting_model,
    n_samples,
    epochs,
    dataloader,
    loss_fn,
    optimizer_fn,
    learning_rate,
    transform_list=[],
):
    """
    Perform Stein Variational Gradient Descent (SVGD) on the given model.

    Args:
        starting_model: The initial model to be optimized.
        n_samples (int): Number of particle realizations for SVGD.
        epochs (int): Number of training epochs.
        dataloader: PyTorch DataLoader providing training data batches.
        loss_fn: Loss function used to compute prediction loss.
        optimizer_fn: Function to instantiate the optimizer.
        learning_rate (float): Learning rate for the optimizer.
        transform_list (list): List of transformations to apply to the model.

    Returns:
        Tuple:
            - model: The trained model after SVGD.
            - pred_history (list): History of prediction losses for all batches.
            - kernel_history (list): History of kernel matrix losses for all batches.
            - total_history (list): History of total losses for all batches.
    """
    model = Converter(toplevel_methods=toplevel_methods).convert(
        starting_model, ParticleParam
    )
    model.initialize_particles(n_samples)

    dataloader_iter = iter(dataloader)
    x_dummy, _ = next(dataloader_iter)  # Peek first batch

    output = model(x_dummy, n_samples)
    optimizer = optimizer_fn(model.parameters(), lr=learning_rate)

    pred_history = []
    kernel_history = []
    total_history = []

    for epoch in range(epochs):
        with tqdm(total=len(dataloader), desc=f"Epoch {epoch + 1}/{epochs}") as pbar:
            for x_batch, y_batch in dataloader:
                pred_loss, kernel_loss = SVGD_step(
                    model, n_samples, x_batch, y_batch, loss_fn, optimizer
                )
                total_loss = pred_loss + kernel_loss

                pred_history.append(pred_loss.detach().cpu().numpy())
                kernel_history.append(kernel_loss.detach().cpu().numpy())
                total_history.append(total_loss.detach().cpu().numpy())

                pbar.set_postfix(
                    tot_loss=total_loss.item(),
                    pred=pred_loss.item(),
                    kernel=kernel_loss.item(),
                )
                pbar.update(1)

    return model, pred_history, kernel_history, total_history


def SVGD_step(model, n_samples, x, y, loss_fn, optimizer):
    """
    Perform a single step of Stein Variational Gradient Descent (SVGD).

    Args:
        model: The model containing particles.
        n_samples (int): Number of particle realizations.
        x (torch.Tensor): Input batch of data.
        y (torch.Tensor): Target batch of data.
        loss_fn: Loss function used to compute prediction loss.
        optimizer: Optimizer instance for updating model parameters.

    Returns:
        Tuple:
            - pred_loss (torch.Tensor): Prediction loss for the batch.
            - kernel_loss (torch.Tensor): Kernel loss for the batch.
    """
    optimizer.zero_grad()
    model.compute_kernel_matrix()
    output = model(x, n_samples)
    pred_loss = torch.vmap(loss_fn, in_dims=(0, None))(output, y).mean()
    pred_loss.backward()

    model.perturb_gradients()
    kernel_loss = model.kernel_matrix.sum(dim=1).mean()
    kernel_loss.backward()

    optimizer.step()

    return pred_loss, kernel_loss
