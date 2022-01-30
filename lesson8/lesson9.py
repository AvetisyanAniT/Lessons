class Game:
    # __name='tttttt'
    def __init__(self, level=155555, total_point=0):
        self.level=level
        self.total_point=total_point
        self.__game_start()
      
        
    def __game_start(self):
        print(f' level is {self.level}')
        print(f' points are  {self.total_point}')

class Child_Game(Game):
    pass

ob_game=Game()


# ob=Game(10,10)
# print(ob._level)
child_ob=Child_Game(5)
# ---------------------------------------Abstraction--------------------------------
from abc import abstractmethod

class Vehicle():
    def __init__(self, value=0):
        self.value=value

    @abstractmethod
    def print_vehicle(self):
        pass
   
    # def structure(self):
    #     pass
    @abstractmethod
    def description(self):
        pass


class Car(Vehicle):
    def print_vehicle(self):
        print('It is car')

    def description(self):
        pass

 
class Mini_Car(Car):
    def print_vehicle(self):
        print('It is minicar')

    def description_1(self):
        pass

ob_car=Mini_Car()
ob_car.print_vehicle()


    

# ob=Vehicle('Car')

car_ob=Car()
car_ob.print_vehicle()
minicar_ob=Mini_Car()
minicar_ob.print_vehicle()

a='testetete'
print(len(a))
a=['test','test']
print(len(a))