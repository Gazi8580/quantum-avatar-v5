class PushNotifications:
    def __init__(self):
        self.subscribers = []

    def subscribe_user(self, user_id):
        self.subscribers.append(user_id)

    def send_push(self, message):
        for user in self.subscribers:
            print(f"Push to {user}: {message}")

    def simit_alarm(self):
        self.send_push("Simit-Alarm! Frisches Brot aus dem Ofen!")

    def simulate_alarm(self):
        return self.simit_alarm()
