from abc import abstractmethod

class Lessons():
    def __init__(self):
        pass

    @abstractmethod
    def lesson_duration(self):
        pass

    @abstractmethod
    def lesson_description(self):
        pass

    @abstractmethod
    def lesson_points(self):
        pass

class My_Lesson(Lessons):
    def lesson_duration(self, quantity):
        duration = 2 * quantity
        print(f'Lesson duration: {duration}')

    def lesson_description(self, description):
        print(f'Lesson description: {description}')

    def lesson_points(self, points):
        with open('points.txt', 'w+') as f:
            f.write(f'Lesson points: {points}')

obj_lesson1 = My_Lesson()
obj_lesson1.lesson_duration(3)
obj_lesson1.lesson_description("Really great lesson")
obj_lesson1.lesson_points("10")