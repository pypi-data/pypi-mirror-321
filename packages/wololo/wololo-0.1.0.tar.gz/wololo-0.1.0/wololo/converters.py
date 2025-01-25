import math
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple

import torch
import torch.fx
from torch.fx import GraphModule

from .adapters import Adapter
from .tracers import PreparatoryTracer
from .transformers import VmapTransformer


class Converter:
    """
    Manages the transformation of a deterministic model into a stochastic model by:
    - Tracing and preparing the computation graph of the deterministic model.
    - Adapting parameters and nodes stochasticly, accounting for multiple realizations.
    - Transforming the forward logic to support batched parameter dimensions.

    Attributes:
        tracer (torch.fx.Tracer): Traces the computation graph. Defaults to `PreparatoryTracer`,
            which adds "transform" metadata to nodes for stochastic adaptation; user can change this
            to allow for tracing dynamic architectures.
        adapter (Adapter): Adapts the graph and substitutes parameters with stochastic modules.
            Defaults to `Adapter`.
        transformer (torch.fx.Transformer): Transforms the forward method. Defaults to `VmapTransformer`,
            well suited for dense architectures; users can change this for more optimized forward() transformations.
        toplevel_methods (Dict): A dictionary of methods to be added to the transformed module,
            useful for implementing posterior approximation algorithms like BBVI or SVGD.
    """

    def __init__(
        self,
        tracer: torch.fx.Tracer = None,
        adapter: Adapter = None,
        transformer: torch.fx.Transformer = None,
        toplevel_methods: Dict = None,
    ) -> None:
        """
        Initializes the Converter with configurable components.

        Args:
            tracer (torch.fx.Tracer, optional): A tracer for graph preparation.
                Defaults to `PreparatoryTracer`.
            adapter (Adapter, optional): Handles stochastic adaptation of parameters and nodes.
                Defaults to `Adapter`.
            transformer (torch.fx.Transformer, optional): Handles forward method transformation.
                Defaults to `VmapTransformer`.
            toplevel_methods (Dict, optional): Methods to add at the top level of the transformed module.
        """
        self.tracer = tracer or PreparatoryTracer
        self.adapter = adapter or Adapter
        self.transformer = transformer or VmapTransformer
        self.toplevel_methods = toplevel_methods or {}

    def convert(
        self,
        module: torch.nn.Module,
        stochastic_parameter: type[torch.nn.Module],
        parameter_list: Optional[list] = None,
    ) -> GraphModule:
        """
        Converts a module by applying the three-part transformation: tracing, stochastic adaptation,
        and forward method transformation. Adds methods specified in `toplevel_methods` to the final module.

        Args:
            module (torch.nn.Module): The module to be transformed.
            stochastic_parameter (type[torch.nn.Module]): A class representing stochastic parameters.
                The `forward()` method of this class must return realizations of the parameter
                and accept `n_samples` as input to generate multiple realizations.
            parameter_list (Optional[List[str]], optional): List of parameter names to replace stochastically.
                Defaults to all parameters if not specified.

        Returns:
            GraphModule: The transformed module with stochastic parameters and an updated computation graph.

        Notes:
            - For dense architectures, specify the `stochastic_parameter` class, and Converter
              handles stochastic adaptation automatically.
            - For dynamic architectures, customize the `tracer` to accommodate for
              different graph preparation or transformation approaches.
            - For convolutional architectures, customize the `transformer` to accommodate for
              different transformation approaches.
        """
        if parameter_list is None:
            parameter_list = []

        original_graph = self.tracer().trace(module, parameter_list)
        new_module, new_graph = self.adapter(original_graph).adapt_module(
            module, stochastic_parameter
        )

        transformed_module = GraphModule(new_module, new_graph)
        final_module = self.transformer(transformed_module).transform()

        final_module.stochastic_parameters = [
            (name, module)
            for name, module in final_module.named_modules()
            if isinstance(module, stochastic_parameter)
        ]

        self.add_methods(final_module)
        return final_module

    def add_methods(self, module: GraphModule) -> None:
        """
        Adds user-defined methods to the transformed module.

        Args:
            module (GraphModule): The module to which methods will be added.
        """
        for method_name, method_function in self.toplevel_methods.items():
            setattr(module, method_name, method_function.__get__(module, type(module)))
