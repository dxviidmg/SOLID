"""
El principio de sustitución de Liskov establece que una clase secundaria debe ser sustituible por su clase principal.
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')

#    print('contact', contact)

    sms_notification = SMS(contact.phone)
#    print('sms_notification', sms_notification)

    email_notification = Email(contact.email)
#    print('email_notification', email_notification)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.notification = email_notification
    notification_manager.send('Hi John')