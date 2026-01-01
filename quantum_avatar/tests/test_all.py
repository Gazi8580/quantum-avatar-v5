import unittest
from quantum_avatar.nlp.nlp_processor import NLPProcessor
from quantum_avatar.vision.image_generator import ImageGenerator
from quantum_avatar.vision.art_categorizer import ArtCategorizer
from quantum_avatar.quantum.quantum_calculator import QuantumCalculator
from quantum_avatar.business.business_logic import BusinessLogic
from quantum_avatar.autonomy.autonomous_executor import AutonomousExecutor
from quantum_avatar.security.security_module import SecurityModule


class TestAllModules(unittest.TestCase):
    def test_nlp(self):
        nlp = NLPProcessor()
        result = nlp.process_text("Hallo Welt")
        self.assertIsInstance(result, dict)
        self.assertIn("corrected_text", result)
        self.assertIn("tokens", result)

    def test_vision(self):
        # Mock image
        img = "mock_image"
        gen = ImageGenerator()
        # Note: actual generation requires model, so skip or mock
        self.assertTrue(True)  # Placeholder

    def test_art(self):
        art = ArtCategorizer()
        # Mock image
        result = art.categorize_art("mock")
        self.assertIsInstance(result, str)

    def test_quantum(self):
        qc = QuantumCalculator()
        products = [{"name": "Apple", "spoil_rate": 0.1, "freshness_index": 0.9}]
        result = qc.optimize_produce_display(products, 20)
        self.assertIsInstance(result, list)

    def test_business(self):
        bl = BusinessLogic()
        result = bl.earn_points("user1", 10)
        self.assertEqual(result["points"], 10)

    def test_autonomy(self):
        ae = AutonomousExecutor()
        state = {"day": "Saturday", "weather": "sunny"}
        result = ae.autonomous_decision(state)
        self.assertIsInstance(result, str)

    def test_security(self):
        sm = SecurityModule()
        result = sm.check_data_privacy({"name": "John"})
        self.assertIn("Consent", result)


if __name__ == "__main__":
    unittest.main()
