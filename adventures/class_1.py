# encapsulating using polymorphism
class NotificationBase:
    def __init__(self, message: str):
        self.message = message
        
    def send(self):
        pass

class EmailNotification(NotificationBase):
    def send(self):
        print(f"Sending email: {self.message}")

class SMSNotification(NotificationBase):
    def send(self):
        print(f"Sending SMS: {self.message}")

class PushNotification(NotificationBase):
    def send(self):
        print(f"Sending push notification: {self.message}")

if __name__ == "__main__":
    notifications = [
        EmailNotification("Hello via email!"),
        SMSNotification("Hello via text!"),
        PushNotification("Hello via app!")
    ]
    
    for notification in notifications:
        notification.send()
