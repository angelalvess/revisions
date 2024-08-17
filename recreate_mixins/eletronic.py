from log_class import LogPrintMixin


class Eletronic:

    def __init__(self, name):
        self.name = name
        self.on = False

    def turn_on(self):
        if not self.on:
            self.on = True

    def turn_of(self):
        if self.on:
            self.on = False


class Laptop(Eletronic, LogPrintMixin):

    def turn_on(self):
        super().turn_on()

        if self.on:
            msg = f'{self.name} turn on'
            self.log_sucess(msg)

    def turn_of(self):
        super().turn_of()

        if not self.on:
            msg = f'{self.name} turn on'
            self.log_error(msg)
