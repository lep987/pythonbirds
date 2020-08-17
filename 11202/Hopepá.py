class jove:
    def __init__(self, *filho, nome = None, idade = 0):
        self.idade = idade
        self.nome = nome
        self.filho = list (filho)
    def jup(self):
        return 'Olá'

if __name__ == '__main__':
    Leonardo = jove(nome ='Leonardo',idade = 20)
    Lorival = jove(Leonardo,nome ='Lorival',idade = 64)
    print (Leonardo.jup(), Leonardo.nome)
    print (Leonardo.jup(), Lorival.nome)
    for filho in Lorival.filho:
        print (filho.nome, filho.idade)
    Lorival.sobrenome = 'José'
    print (Lorival.nome, Lorival.sobrenome)
print (Lorival.__dict__)
