class Camera:
    def __init__(self, brand, filming=False):
        self.brand = brand
        self.filming = filming

    def start_filming(self):
        if self.filming:
            print('Camera is already filming')
            return

        print(f'{self.brand} camera is now filming')
        self.filming = True

    def stop_filming(self):
        if not self.filming:
            print('Camera is not filming')
            return
        print(f'{self.brand} camera stopped filming')
        self.filming = False

    def photo(self):
        if self.filming:
            print('Camera is filming, cannot take a photo')
            return
        print(f'{self.brand} camera took a photo')


c1 = Camera('Canon')
c1.start_filming()
c1.photo()
c1.stop_filming()
c1.photo()

print(c1.filming)


c2 = Camera('Nikon')
print(c2.filming)
c2.photo()
