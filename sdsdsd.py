class Carrin:
    def vel(self, vel=0):
        self.vel = vel
    def acel(self):
        self.vel += 1
    def fre(self):
        self.vel -= 2
        if self.vel < 0:
            self.vel = 0
    def rota(self, rota = ''):
        self.rota = rota
    def esq(self):
        if self.rota == 'Norte':
            self.rota = 'Oeste'
        elif self.rota == 'Oeste':
            self.rota = 'Sul'
        elif self.rota =='Sul':
            self.rota = 'Leste'
        else:
            self.rota = 'Norte'
    def dir(self):
        if self.rota == 'Norte':
            self.rota = 'Leste'
        elif self.rota == 'Leste':
            self.rota = 'Sul'
        elif self.rota =='Sul':
            self.rota = 'Oeste'
        else:
            self.rota = 'Norte'

if __name__ == '__main__':
    j=Carrin()
    print(j.vel())
    j.acel()
    print(j.vel)
    j.acel()
    print(j.vel)
    j.fre()
    print(j.vel)
    j.rota('Leste')
    print(j.rota)
    j.esq()
    print(j.rota)
    j.dir()
    print(j.rota)
    j.dir()
    print(j.rota,j.vel)
    j.acel(), j.esq()
    print(j.rota,j.vel)