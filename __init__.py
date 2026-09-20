from .nodes.comfyui_dashscopeimage import ComfyUIDashscopeImage


NODE_CLASS_MAPPINGS = {
    "DashScopeFLUXAPI": ComfyUIDashscopeImage,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DashScopeFLUXAPI": "Dashscope Image Generation",
}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
