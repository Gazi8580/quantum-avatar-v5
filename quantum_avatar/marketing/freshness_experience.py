class FreshnessExperience:
    def __init__(self):
        self.strategies = {
            "daily_deliveries": "Tägliche Lieferungen frischer Produkte aus der Türkei.",
            "display_optimization": "Auslagen mit farbigen, frischen Produkten optimieren.",
            "tasting_events": "Regelmäßige Verkostungen für Kundenbindung.",
            "atmosphere_enhancement": "Duft und Musik für bessere Einkaufsatmosphäre.",
        }

    def implement_freshness(self, product_category):
        if product_category == "meat":
            return "Halal-Fleisch täglich frisch, Herkunft transparent."
        elif product_category == "vegetables":
            return "Obst und Gemüse aus lokalen Feldern, täglich erneuert."
        else:
            return "Allgemeine Frische-Strategie."

    def create_experience_plan(self, day):
        if day == "Saturday":
            return "Probier-Samstage: Sucuk und Oliven kostenlos, Rezepte verteilen."
        elif day == "Thursday":
            return "Markttag-Highlights: Frische Granatäpfel und Fladenbrot."
        else:
            return "Tägliche Erlebnis-Elemente: Duft-Diffuser mit Simit-Aroma."
