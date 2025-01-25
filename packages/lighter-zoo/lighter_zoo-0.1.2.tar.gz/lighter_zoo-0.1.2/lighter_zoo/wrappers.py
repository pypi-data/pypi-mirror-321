"""
This module provides wrapper classes for MONAI models with HuggingFace Hub integration.

The wrappers extend base MONAI models with HuggingFace Hub capabilities through the
LighterZooMixin, enabling easy model sharing and distribution while preserving the
original model functionality.
"""

from .mixin import LighterZooMixin
from monai.networks.nets import SegResNetDS as SegResNet_base
from monai.networks.nets.segresnet_ds import SegResEncoder as SegResEncoder_base


class SegResNet(SegResNet_base, LighterZooMixin):
    """SegResNet model with HuggingFace Hub integration capabilities.
    
    This class wraps MONAI's SegResNetDS model and adds HuggingFace Hub integration
    through the LighterZooMixin. It maintains all the functionality of the base
    SegResNetDS while enabling easy model sharing and loading through the
    HuggingFace Hub.

    The model architecture follows the original SegResNet implementation from MONAI,
    which is a residual encoder-decoder architecture designed for volumetric
    segmentation tasks.

    Args:
        *args: Variable length argument list passed to SegResNetDS
        **kwargs: Arbitrary keyword arguments passed to SegResNetDS

    Example:
        ```python
        # Create a model instance
        model = SegResNet(
            init_filters=32,
            in_channels=1,
            out_channels=2
        )

        # Push to HuggingFace Hub
        model.push_to_hub("username/model-name")

        # Load from HuggingFace Hub
        loaded_model = SegResNet.from_pretrained("username/model-name")
        ```
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SegResEncoder(SegResEncoder_base, LighterZooMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)