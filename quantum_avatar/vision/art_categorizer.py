from transformers import CLIPProcessor, CLIPModel
import torch


class ArtCategorizer:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def categorize_art(
        self,
        image,
        categories=["abstract", "realistic", "impressionist", "modern", "classical"],
    ):
        inputs = self.processor(
            text=categories, images=image, return_tensors="pt", padding=True
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        outputs = self.model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)
        best_category = categories[probs.argmax().item()]
        return best_category

    def understand_art(
        self, image, description_prompt="Describe this artwork in detail"
    ):
        # For understanding, perhaps use a captioning model, but for simplicity, use CLIP with text
        # This is a placeholder; in reality, use a captioning model like BLIP
        return f"Artwork categorized as {self.categorize_art(image)}. {description_prompt} - AI analysis shows artistic elements."
