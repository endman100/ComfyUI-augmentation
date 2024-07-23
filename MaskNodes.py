import random
import torch

class RamdomFlipImage:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "probability": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 100000, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "method"
    CATEGORY = "Ramdom"

    def set_seed(self, seed):
        random.seed(seed)
        torch.manual_seed(seed)

    def method(self, image, probability, seed): #b, h, w, c
        self.set_seed(seed)
        print("RamdomFlipImage", type(image), image.shape, image.dtype)
        if random.random() < probability:
            image = torch.flip(image, [2])
        return image,
NODE_CLASS_MAPPINGS = {
    "RamdomFlipImage (endman100)": RamdomFlipImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RamdomFlipImage (endman100)": "RamdomFlipImage (endman100)"
}
