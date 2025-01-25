"""
This module provides a mixin class for integrating models with the HuggingFace Hub.

The LighterZooMixin class extends PyTorchModelHubMixin to provide HuggingFace Hub
integration capabilities specifically configured for the Project Lighter ecosystem.
This enables seamless model sharing, versioning, and distribution through the
HuggingFace Hub infrastructure.
"""

from huggingface_hub import PyTorchModelHubMixin


class LighterZooMixin(
    PyTorchModelHubMixin,
    library_name="project-lighter",
    repo_url="https://github.com/project-lighter/lighter-zoo",
    docs_url="https://project-lighter.github.io/lighter/",
    tags=["lighter"],
):
    """Mixin class that adds HuggingFace Hub integration capabilities to models.

    This mixin class inherits from PyTorchModelHubMixin and configures it with
    Project Lighter specific metadata. It enables models to be easily shared and
    loaded through the HuggingFace Hub.

    Attributes:
        library_name (str): Name of the library in HuggingFace Hub ("project-lighter")
        repo_url (str): URL of the GitHub repository
        docs_url (str): URL of the project documentation
        tags (list): List of tags for model categorization

    Example:
        ```python
        class MyModel(BaseModel, LighterZooMixin):
            def __init__(self):
                super().__init__()
                # Model implementation
        ```
    """
    pass
