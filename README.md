# ComfyUI DashScope Image

Custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that generates images with Alibaba Cloud DashScope Image Generation API.

The node supports Qwen Image models, regional DashScope endpoints, custom workspaces, deterministic seeds, and direct image output inside ComfyUI workflows.

## Features

- Generate images from text prompts with DashScope.
- Select the DashScope region from the node.
- Enter a custom DashScope `workspace_id`.
- Support for configurable image size, seed, and generation steps.
- Synchronous requests compatible with APIs that do not support asynchronous calls.
- Returns the generated image directly as a ComfyUI `IMAGE` output.

## Requirements

- ComfyUI
- Python 3.9 or newer
- A DashScope API key
- A DashScope workspace in the selected region

## Installation

### Manual installation

Clone or download this repository into the ComfyUI `custom_nodes` directory:

```text
ComfyUI/
└── custom_nodes/
	└── ComfyUI-DashscopeImage/
```

Install the Python dependencies from the ComfyUI environment:

```bash
pip install -r requirements.txt
```

Restart ComfyUI after installation.

## Configuration

Add the **Dashscope Image Generation** node to your workflow and fill in:

| Field | Description |
| --- | --- |
| `model` | DashScope image model to use. |
| `region` | Region where the workspace and API key were created. |
| `workspace_id` | DashScope workspace identifier, for example `ws-...`. |
| `api_key` | API key created in the selected DashScope region. |
| `prompt` | Description of the image to generate. |
| `size` | Output image dimensions. |
| `seed` | Numeric seed used to control generation randomness. |
| `steps` | Number of generation steps. |

The API key and workspace must belong to the same region. Using a key from another region can result in an authentication error.

## Supported models

The current node includes:

- `qwen-image-max-2025-12-30`
- `qwen-image-2.0-pro`

Model availability may depend on the selected region and workspace.

## Supported regions

- `cn-beijing`
- `cn-hongkong`
- `ap-southeast-1` (Singapore)
- `ap-northeast-1` (Tokyo)
- `eu-central-1` (Frankfurt)
- `us-east-1` (Virginia)

## Output sizes

The node currently supports:

```text
512*1024
768*512
768*1024
1024*576
576*1024
1024*1024
```

## Common errors

### `Current user api does not support asynchronous calls`

The node uses synchronous generation by setting `is_async=False`. Make sure you are using the current version of this node and restart ComfyUI after updating it.

### `parameters.seed` must be less than or equal to `2147483647`

The seed must be a 32-bit signed integer. The node limits the seed to the range accepted by DashScope.

### Authentication or workspace errors

Check that:

1. The API key was created in the selected `region`.
2. The `workspace_id` belongs to that region.
3. The selected model is available in the workspace.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
