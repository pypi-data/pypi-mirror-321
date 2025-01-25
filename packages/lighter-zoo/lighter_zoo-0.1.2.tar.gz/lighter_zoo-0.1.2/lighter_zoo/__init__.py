"""
Lighter Zoo: A collection of medical imaging models with HuggingFace Hub integration.

This package provides medical imaging models from the MONAI ecosystem with added
HuggingFace Hub integration capabilities. It enables easy sharing, versioning, and
distribution of models through the HuggingFace Hub infrastructure while maintaining
the full functionality of the original MONAI implementations.

Available Models:
    - SegResNet: A residual encoder-decoder network for volumetric segmentation

Example:
    ```python
    from lighter_zoo import SegResNet

    # Create a model
    model = SegResNet(
        init_filters=32,
        in_channels=1,
        out_channels=2
    )

    # Use HuggingFace Hub integration
    model.push_to_hub("username/model-name")
    ```
"""

from .wrappers import SegResNet, SegResEncoder

__all__ = ["SegResNet", "SegResEncoder"]