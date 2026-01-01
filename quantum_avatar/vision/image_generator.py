from diffusers import StableDiffusionPipeline 
import torch  
class ImageGenerator:  
    def __init__(self):  
        self.pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")  
        self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")  
    def generate_image(self, prompt):  
        image = self.pipe(prompt).images[0]  
        return image 
