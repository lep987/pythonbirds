class pessoa():
    olhos = 2
    idade = 31
    def jove(self, nome = None):
        self.nome = nome

    def juve(self):
        return f'Olá, '

j = pessoa()
j.jove(nome = 'Leonardo')
print(j.nome, j.idade)
print(j.olhos)

class julho(pessoa):
    olhos = 3
    idade = 28
    pass

c = julho()
c.jove('Julho')
print(c.nome, c.idade)
print(c.olhos)