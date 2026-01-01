class AdGenerator:
    def __init__(self):
        self.templates = {
            "halal_meat": "Frisches Halal-Lamm aus {origin}, perfekt für Grillabende in Amriswil!",
            "vegetables": "Saisonale Gemüse aus lokalen Feldern, frisch und günstig!",
            "promotion": "Sonderaktion: {product} nur CHF {price}, solange Vorrat!",
        }

    def generate_ad(self, product_type, details):
        template = self.templates.get(
            product_type, "Willkommen in unserem türkischen Supermarkt!"
        )
        return template.format(**details)

    def generate_facebook_post(self, product, price, scarcity=False):
        if scarcity:
            return f"Nur noch wenige {product} vorhanden! Schnell zugreifen für CHF {price}."
        return f"Entdecken Sie unser {product} für nur CHF {price}. Perfekt für Ihre Familie!"

    def generate_flyer_text(self, offers):
        text = "Wochenangebote:\n"
        for offer in offers:
            text += f"- {offer['product']}: CHF {offer['price']}\n"
        text += "Besuchen Sie uns in Amriswil!"
        return text
