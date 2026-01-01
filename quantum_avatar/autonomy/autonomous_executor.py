class AutonomousExecutor:
    def __init__(self):
        self.triggers = {}

    def add_trigger(self, condition, action):
        self.triggers[condition] = action

    def execute(self, current_state):
        for condition, action in self.triggers.items():
            if self.check_condition(condition, current_state):
                return self.perform_action(action)
        return None

    def check_condition(self, condition, state):
        # Simple condition check
        if "weather" in condition and state.get("weather") == condition["weather"]:
            return True
        if (
            "stock" in condition
            and state.get("stock_level", 1) < condition["stock_level"]
        ):
            return True
        if "day" in condition and state.get("day") == condition["day"]:
            return True
        return False

    def perform_action(self, action):
        if action == "send_whatsapp":
            return "WhatsApp-Einladung gesendet"
        if action == "generate_post":
            return "Facebook-Post generiert"
        if action == "book_radio":
            return "Radio-Werbung gebucht"
        return "Aktion ausgeführt"

    def autonomous_decision(self, state):
        # Example: If it's Saturday and sunny, send tasting invitation
        if state.get("day") == "Saturday" and state.get("weather") == "sunny":
            return self.perform_action("send_whatsapp")
        # If stock low, generate scarcity post
        if state.get("stock_level", 1) < 0.2:
            return self.perform_action("generate_post")
        # If market day, book radio
        if state.get("day") == "Thursday":
            return self.perform_action("book_radio")
        return "Keine Aktion"
