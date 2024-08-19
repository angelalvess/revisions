from abc import ABC, abstractmethod


class Message(ABC):

    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        pass


class Email(Message):

    def send(self):
        print(f'Email: {self.message}')


class SMS(Message):

    def send(self):
        print(f'SMS: {self.message}')


email = Email('Hello, World!')
sms = SMS('Hello, World!')


def notificate(message: Message):
    send_message = message.send()

    if send_message:
        print('Message sent!')
    else:
        print('Message not sent!')


notificate(email)
