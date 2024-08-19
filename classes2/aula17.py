class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(f"Calling {name} at {self.phone}")


call = CallMe("123456789")
call('Angel')
