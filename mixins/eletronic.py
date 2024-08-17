from log_class import LogPrintMixin


class Eletronic:

    def __init__(self, name):
        self.name = name
        self.on = False

    def turn_on(self):
        if not self.on:
            self.on = True

    def turn_off(self):
        if self.on:
            self.on = False


class Laptop(Eletronic, LogPrintMixin):

    def turn_on(self):
        super().turn_on()

        if self.on:
            msg = f'{self.name} turned on'
            self.log_suceess(msg)

    def turn_off(self):
        super().turn_off()

        if not self.on:
            msg = f'{self.name} turned off'
            self.log_suceess(msg)
