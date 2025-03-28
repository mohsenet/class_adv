# Encapsulating Using Polymorphism: Another Example

Here's another example demonstrating polymorphism through method overriding, similar to your payment processor example but with a different domain:

```python
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
```

**Key polymorphic concepts demonstrated:**
1. All notification types inherit from `NotificationBase`
2. Each subclass implements its own version of the `send()` method
3. The client code can treat all notifications uniformly through the base class interface
4. The actual behavior is determined at runtime based on the object's type

This follows the same pattern as your payment example, just with a different domain (notifications instead of payments). The polymorphic behavior allows you to add new notification types without changing the code that sends them.
