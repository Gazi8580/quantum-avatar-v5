class PriceLabelCreator:
    def __init__(self):
        self.templates = {
            "standard": "Produkt: {product}\nPreis: CHF {price}\nHerkunft: {origin}\nHalal: {halal}",
            "promotion": "Sonderangebot!\n{product}\nCHF {price} statt {old_price}\nNur solange Vorrat!",
        }

    def create_label(
        self,
        product,
        price,
        origin="Türkei",
        halal="Ja",
        promotion=False,
        old_price=None,
    ):
        if promotion and old_price:
            template = self.templates["promotion"]
            return template.format(product=product, price=price, old_price=old_price)
        else:
            template = self.templates["standard"]
            return template.format(
                product=product, price=price, origin=origin, halal=halal
            )

    def generate_bulk_labels(self, products_list):
        labels = []
        for product in products_list:
            label = self.create_label(**product)
            labels.append(label)
        return labels
