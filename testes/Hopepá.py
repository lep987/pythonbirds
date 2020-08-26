class jove:
    olhos = 2
    def __init__(self, nome = None, idade = 0, *filho):
        self.filho = list (*filho)
        self.nome = nome
        self.idade = idade
    def jup(self):
        return 'Olá'
    @staticmethod
    def julieta():
        return 42
    @classmethod
    def Hoptipá(cls):
        return f'{Leonardo.nome} tem {jove.olhos} olhos.'




if __name__ == '__main__':
    Rodrigo = jove(nome = 'Rodrigo', idade = 30)
    Leonardo = jove(nome ='Leonardo',idade = 20)
    Lorival = jove(nome ='Lorival',idade = 64)
    Thelma = jove (nome = 'Thelma', idade = 59)
    Lorival.filho = Leonardo, Rodrigo
    Thelma.filho = Leonardo, Rodrigo
    for filho in Lorival.filho:
        print (filho.nome, filho.idade)
    print ()
    for filho in Thelma.filho:
        print (filho.nome, filho.idade)
    Leonardo.sobrenome = 'Muniz'
    Rodrigo.sobrenome = 'Luciano'
    Lorival.sobrenome = 'José'
    Thelma.sobrenome = 'Muniz'
    print (Lorival.nome, Lorival.sobrenome)
    print (Rodrigo.nome, Rodrigo.sobrenome)
    print (Leonardo.nome, Leonardo.sobrenome)
    print(isinstance(Rodrigo, juve))
print ()
print (Thelma.__dict__)
print (jove.julieta(), Leonardo.julieta())
print (jove.Hoptipá(), Leonardo.Hoptipá())

