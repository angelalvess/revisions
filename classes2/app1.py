class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def running(self, volante):
        if volante == 'right':
            print('Car is running with the right steering wheel')
        elif volante == 'left':
            print('Car is running with the left steering wheel')
        else:
            print('Car is running')

    def stop(self, speed):
        if speed == 0:
            print('Car is stopped')
        else:
            print('Car is running')


fusca = Car('Volkswagen', 'Fusca')

fusca.running('right')
fusca.stop(10)
print(fusca.make)
print(fusca.model)
