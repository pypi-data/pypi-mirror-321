from .mixin import LighterZooMixin
from monai.networks.nets import SegResNetDS as SegResNet_base

class SegResNet(SegResNet_base, LighterZooMixin):
    """Monai model with HuggingFace Hub integration capabilities."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)