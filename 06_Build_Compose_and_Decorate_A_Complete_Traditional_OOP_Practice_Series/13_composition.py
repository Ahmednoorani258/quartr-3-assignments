# 13. Composition
 
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:

    def start(self):
        return "Engine started!"

    def stop(self):
        return "Engine stopped!"


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        return self.engine.start()

    def stop_engine(self):
        return self.engine.stop()


engine = Engine()
car = Car(engine)

print(car.start_engine())