class MarketingStrategy:
    def __init__(self):
        self.strategies = {
            "halal_transparency": "Hebe die Halal-Zertifizierung und Herkunft hervor, um Vertrauen aufzubauen.",
            "freshness_focus": "Betone Frische mit täglichen Lieferungen und Auslagen-Optimierung.",
            "community_engagement": "Baue Beziehungen zur türkischen Community in Amriswil auf.",
            "digital_presence": "Nutze WhatsApp, Facebook und Google Business für lokale Sichtbarkeit.",
        }

    def plan_strategy(self, focus_area):
        return self.strategies.get(focus_area, "Allgemeine Marketing-Strategie")

    def implement_campaign(self, campaign_type, details):
        if campaign_type == "probier_samstage":
            return f"Probier-Samstage: {details['product']} kostenlos probieren, Rezepte verteilen."
        elif campaign_type == "seasonal_highlights":
            return f"Saisonale Highlights: {details['product']} für {details['event']} platzieren."
        else:
            return "Kampagne implementiert."
