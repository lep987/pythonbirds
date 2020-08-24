class motor:
    def vel(self, vel = 0):
        self.vel = vel
    def acel(self):
        self.vel += 1
    def fre(self):
        self.vel -=2
        if motor.vel < 0:
            motor.vel = 0
motor = motor()
print(motor.vel())
motor.acel()
print(motor.vel)
motor.fre()
print(motor.vel)
motor.acel()
motor.acel()
motor.acel()

print(motor.vel)
motor.fre()
motor.fre()
motor.fre()

print(motor.vel)

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

direção = direção()
direção.esq()
print(direção.rota)
direção.dir()
print(direção.rota)
direção.esq()
print(direção.rota)
direção.dir()
print(direção.rota)
direção.esq()
print(direção.rota)
direção.dir()
direção.dir()
direção.dir()
print(direção.rota)

