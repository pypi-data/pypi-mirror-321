
## Installation

To install the `lighter-zoo` package, use pip:

```bash
pip install lighter-zoo
```

## Example Usage

```python
# Import the SegResNet model from lighter_zoo
from lighter_zoo import SegResNet

# Create a 3D segmentation model for whole body segmentation
model = SegResNet(
    spatial_dims=3,      # 3D input volumes
    in_channels=1,       # Single channel input (e.g. CT or MRI)
    out_channels=118,    # Number of segmentation classes
    init_filters=32,     # Initial number of filters in first conv layer
    blocks_down=[1, 2, 2, 4, 4],  # Number of residual blocks in each downsampling stage
    dsdepth=4           # Depth of deep supervision
)

# Load pretrained weights from the whole body segmentation model
model.from_pretrained("project-lighter/whole_body_segmentation")
```

This example demonstrates how to load the `SegResNet` model with pre-trained weights for whole-body segmentation.

## Available Models

The following models are currently available in the Lighter-Zoo:

- **SegResNet:** A 3D segmentation model based on the MONAI implementation.

More models will be added in the future.

## Contributing

Contributions are welcome! If you have a pre-trained model you would like to share, please submit a pull request.

## License

This project is licensed under the Apache 2.0 License.
