# class motor:
#     def vel(self, vel = 0):
#         self.vel = vel
#     def acel(self):
#         self.vel += 1
#     def fre(self):
#         self.vel -= 2
#         if self.vel < 0:
#             self.vel = 0
#
# class direção:
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

class carro:
    def rota(self):
        rota = direção.rota()
        vel = motor.vel()

    def vel(self, vel=0):
        self.vel = vel

    def acel(self):
        self.vel += 1

    def fre(self):
        self.vel -= 2
        if self.vel < 0:
                self.vel = 0
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

juq = carro()
print(juq.vel())
juq.acel()
print(juq.vel)
juq.fre()
print(juq.vel)
print(juq.rota())
juq.esq()
print(juq.rota)
juq.dir()
print(juq.rota)
juq.acel()
juq.esq()
print(juq.rota, juq.vel)
juq.acel()
juq.acel()
print(juq.rota, juq.vel)
juq.esq()
juq.esq()
print(juq.rota, juq.vel)
juq.fre()
juq.fre()
juq.dir()
juq.dir()
juq.dir()
print(juq.rota, juq.vel)

