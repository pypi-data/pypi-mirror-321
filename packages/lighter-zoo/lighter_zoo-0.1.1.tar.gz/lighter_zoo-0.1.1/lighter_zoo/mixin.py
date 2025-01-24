from huggingface_hub import PyTorchModelHubMixin

class LighterZooMixin(
    PyTorchModelHubMixin,
    library_name="project-lighter",
    repo_url="https://github.com/project-lighter/lighter-zoo",
    docs_url="https://project-lighter.github.io/lighter/",
    tags=["lighter"],
):
    pass