class LogoDesigner:
    def __init__(self):
        self.templates = {
            "turkish_supermarket": "Erstelle ein Logo für einen türkischen Supermarkt in Amriswil: Türkische Flaggenfarben Rot und Weiß, mit Elementen wie Halal-Zertifizierung, frisches Obst und Gemüse, freundlich und einladend.",
            "product": "Logo für {product}: Modern, ansprechend, mit türkischen Motiven wie {motiv}, für Supermarkt-Regal.",
        }

    def generate_logo_prompt(self, type, details):
        template = self.templates.get(type, "Generisches Logo")
        return template.format(**details)

    def customize_logo(self, base_prompt, customizations):
        prompt = base_prompt
        for key, value in customizations.items():
            prompt += f" {key}: {value}"
        return prompt
