class motor:
    def vel(self, vel):
        self.vel = vel
    def acel(self):
        self.vel += 1
    def fre(self):
        self.vel -= 2
        if self.vel < 0:
            self.vel = 0

class direção:
    def rota(self, rota = 'Norte'):
        self.rota = rota
    def esq(self):
        if self.rota == 'Norte':
            self.rota = 'Oeste'
        elif self.rota == 'Oeste':
            self.rota = 'Sul'
        elif self.rota == 'Sul':
            self.rota = 'Leste'
        else:
            self.rota = 'Norte'
    def dir(self):
        if self.rota == 'Norte':
            self.rota = 'Leste'
        elif self.rota == 'Leste':
            self.rota = 'Sul'
        elif self.rota == 'Sul':
            self.rota = 'Oeste'
        else:
            self.rota = 'Norte'

class Carro:
    def __init__(self, motor, direção):
        self.motor = motor
        self.direção = direção
    def val_vel(self):
        return self.motor.vel
    def acel(self):
        self.motor.acel()
    def fre(self):
        self.motor.fre()
    def praonde(self):
        return direção.rota()
    def esq(self):
        self.direção.esq()
    def dir(self):
        self.direção.dir()
if __name__ == '__main__':
    care = Carro(motor,direção)
    print(care.val_vel())
    care.acel
    care.acel()
    print(care.val_vel())

# class carro:
#     def rota(self):
#         rota = direção.rota()
#         vel = motor.vel()
#
#     def vel(self, vel=0):
#         self.vel = vel
#
#     def acel(self):
#         self.vel += 1
#
#     def fre(self):
#         self.vel -= 2
#         if self.vel < 0:
#                 self.vel = 0
#     def rota(self, rota = 'Norte'):
#         self.rota = rota
#     def esq(self):
#         if self.rota == 'Norte':
#             self.rota = 'Oeste'
#         elif self.rota == 'Oeste':
#             self.rota = 'Sul'
#         elif self.rota == 'Sul':
#             self.rota = 'Leste'
#         else:
#             self.rota = 'Norte'
#     def dir(self):
#         if self.rota == 'Norte':
#             self.rota = 'Leste'
#         elif self.rota == 'Leste':
#             self.rota = 'Sul'
#         elif self.rota == 'Sul':
#             self.rota = 'Oeste'
#         else:
#             self.rota = 'Norte'


