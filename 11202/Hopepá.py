class jove:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    def jup(self):
        return 'Olá'

if __name__ == '__main__':
    p = jove('Julio', 35)
    print (p.jup())
    print (p.jup(),',', p.nome,'Tu tens', p.idade, 'anos, né?')