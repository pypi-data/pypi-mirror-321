import torch
from tqdm import tqdm

from ..converters import Converter


def BBVI(
    starting_model,
    stochastic_parameter,
    n_samples,
    epochs,
    dataloader,
    loss_fn,
    optimizer_fn,
    learning_rate,
    transform_list=[],
):
    """
    Perform Black Box Variational Inference (BBVI) on the given model.

    Args:
        starting_model: The initial model to be optimized.
        stochastic_parameter: A module encoding the random parameter logic,
            which will substitute parameters specified in the `transform_list` with corresponding
            stochastic modules.
        transform_list (list): List of parameters apply the random transformation to.
        n_samples (int): Number of random parameter realizations to use during inference.
        epochs (int): Number of training epochs.
        dataloader: PyTorch DataLoader providing training data batches.
        loss_fn: Loss function used to compute prediction loss.
        optimizer_fn: Function to instantiate the optimizer.
        learning_rate (float): Learning rate for the optimizer.

    Returns:
        Tuple:
            - model: The trained model after BBVI.
            - pred_history (list): History of prediction losses for all batches.
            - kl_history (list): History of KL divergence losses for all batches.
            - total_history (list): History of total losses for all batches.
    """
    num_parameters = sum(
        p.numel() for p in starting_model.parameters() if p.requires_grad
    )
    model = Converter().convert(starting_model, stochastic_parameter, transform_list)

    optimizer = optimizer_fn(model.parameters(), lr=learning_rate)

    pred_history = []
    kl_history = []
    total_history = []

    for epoch in range(epochs):
        with tqdm(total=len(dataloader), desc=f"Epoch {epoch + 1}/{epochs}") as pbar:
            for x_batch, y_batch in dataloader:
                batch_size = x_batch.shape[0]
                kl_weight = batch_size / num_parameters

                pred_loss, kl_loss, total_loss = BBVI_step(
                    model,
                    n_samples,
                    x_batch,
                    y_batch,
                    loss_fn,
                    optimizer,
                    kl_weight,
                )

                pred_history.append(pred_loss.detach().cpu().numpy())
                kl_history.append(kl_loss.detach().cpu().numpy())
                total_history.append(total_loss.detach().cpu().numpy())

                pbar.set_postfix(
                    tot_loss=total_loss.item(),
                    pred=pred_loss.item(),
                    kernel=kl_loss.item(),
                )
                pbar.update(1)

    return model, pred_history, kl_history, total_history


def BBVI_step(model, n_samples, x, y, loss_fn, optimizer, kl_weight):
    """
    Perform a single step of Black Box Variational Inference (BBVI).

    Args:
        model: The stochastic model being trained.
        n_samples (int): Number of random parameter realizations to use during inference.
        x (torch.Tensor): Input batch of data.
        y (torch.Tensor): Target batch of data.
        loss_fn: Loss function used to compute prediction loss.
        optimizer: Optimizer instance for updating model parameters.
        kl_weight (float): Weight applied to the KL divergence loss.

    Returns:
        Tuple:
            - pred_loss (torch.Tensor): Prediction loss for the batch.
            - kl_loss (torch.Tensor): KL divergence loss for the batch.
            - total_loss (torch.Tensor): Total loss (prediction + KL divergence) for the batch.
    """
    optimizer.zero_grad()
    output = model(x, n_samples)
    pred_loss = torch.vmap(loss_fn, in_dims=(0, None))(output, y).mean()
    kl_loss = 0
    for name, module in model.stochastic_parameters:
        kl_loss += module.kl_divergence()
    kl_loss = kl_loss * kl_weight
    total_loss = pred_loss + kl_loss
    total_loss.backward()
    optimizer.step()
    return pred_loss, kl_loss, total_loss
