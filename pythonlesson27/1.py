class Tech():
    def __init__(self,mark,speed,user):
        self.mark = mark
        self.speed = speed
        self.user = user
class Rocket(Tech):
    def about_rocket(self):
        print(f'Марка ракеты - {self.mark.title()}\n Скорость ракеты {self.speed}\n Водитель {self.user}')
class Machine(Tech):
    def about_machine(self):
        print(f'Марка машины - {self.mark.title()}\n Скорость машины {self.speed}\n Водитель {self.user}')
do_use = str(input('Введите - 1, если хотите полететь или 2 если хотите поехать: '))
do_rocket = Rocket('Bemba','100.000 km\s','Vlada')
do_machine = Machine('Mercedes','150 km\s','Daniel')
if do_use == '1':
    print(do_rocket.about_rocket())
elif do_use == '2':
    print(do_machine.about_machine())
else:
    print('Вы не ввели указанную цыфру!')