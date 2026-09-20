from http import HTTPStatus
import requests, dashscope, torch
import numpy as np
from PIL import Image
from io import BytesIO
from dashscope.aigc.image_generation import ImageGeneration



class ComfyUIDashscopeImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (
                    [
                        "qwen-image-max-2025-12-30","qwen-image-2.0-pro",
                    ],
                    {
                        "default": "qwen-image-2.0-pro"
                    }
                ),
                "region": (
                    [
                        "cn-beijing",
                        "cn-hongkong",
                        "ap-southeast-1",
                        "ap-northeast-1",
                        "eu-central-1",
                        "us-east-1",
                    ],
                    {"default": "ap-southeast-1"},
                ),
                "workspace_id": ("STRING", {"multiline": False, "default": ""}),
                "api_key": ("STRING", {"multiline": False, "default": "",}),
                "prompt": ("STRING", {"multiline": True, "default": "",}),
                "size": (
                    [
                        "512*1024", "768*512", "768*1024", "1024*576", "576*1024", "1024*1024"
                    ],
                    {
                        "default": "1024*1024"
                    }
                ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2147483647}),
                "steps": ("INT", {"default": 30, "min": 1, "max": 50, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "call_api"
    CATEGORY = "DashScope"

    def preprocess_image(self, image):
        image = torch.Tensor(np.array(image, dtype=np.float32) * (1 / 255))
        return image

    def call_api(
        self, model, region, workspace_id, api_key, prompt, size, seed, steps
    ):
        seed = seed % 2147483647
        dashscope.api_key=api_key
        dashscope.set_region(region=region, workspace_id=workspace_id)
        rsp = ImageGeneration.call(
            model=model,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            api_key=api_key,
            workspace=workspace_id,
            size=size,
            seed=seed,
            steps=steps,
            is_async=False,
        )
        if rsp.status_code == HTTPStatus.OK:
            print(rsp.output)
            print(rsp.usage)
            image_url = rsp.output.choices[0].message.content[0]["image"]
            response = requests.get(image_url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img = self.preprocess_image(img)
            return ([img],)
        else:
            raise RuntimeError(
                "DashScope image generation failed: "
                f"status_code={rsp.status_code}, "
                f"code={rsp.code}, message={rsp.message}"
            )


