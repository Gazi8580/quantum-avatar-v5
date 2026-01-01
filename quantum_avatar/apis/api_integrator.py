import requests
import stripe


class APIIntegrator:
    def __init__(self):
        stripe.api_key = "sk_test_..."  # Placeholder for Stripe key
        self.weather_api_key = "your_weather_api_key"  # Placeholder

    def process_payment(self, amount_chf, customer_email):
        # Amount in Rappen (100 Rappen = 1 CHF)
        amount_rappen = int(amount_chf * 100)
        try:
            charge = stripe.Charge.create(
                amount=amount_rappen,
                currency="chf",
                source="tok_visa",  # Placeholder
                description=f"Payment for {customer_email}",
            )
            return charge["id"]
        except stripe.error.StripeError as e:
            return f"Payment failed: {e}"

    def get_weather_amriswil(self):
        # Amriswil coordinates: 47.548, 9.303
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=47.548&lon=9.303&appid={self.weather_api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["main"].lower(),
            }
        return {"error": "Weather data not available"}

    def get_stock_data(self, product):
        # Placeholder for stock API
        # Assume a mock API
        mock_stock = {"sucuk": 50, "oliven": 30, "lamm": 20}
        return mock_stock.get(product.lower(), 0)
