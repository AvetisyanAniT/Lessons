class Game:
    # __name='tttttt'
    def __init__(self, level, total_point=0):
        self.level=level
        self.total_point=total_point

        # self.name=self.__name
        # self.game_start()
        
    def game_start(self):
        print(f' level is {self.level}')
        print(f' points are  {self.total_point}')

class Mini_Game(Game):
    def __init__(self,  level=1,total_point=0, age=3):
        Game.__init__(self, level=1, total_point=0)
        self.age=age
        print(self.level)

    def game_start1(self):
        print(f'{self.level}')
        print(f' points are  {self.total_point}')
 
class New_Mini(Mini_Game):
    def __init__(self, color='blue'):
        super().__init__()
        self.color=color
    

new_ob=New_Mini()
print(new_ob.age)
print(new_ob.color)

# print(new_ob.age)
# new_ob.game_start()
# # ob=Game()

