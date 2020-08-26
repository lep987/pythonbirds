from testes.Hopepá import jove
class juve(jove):
    pass

if __name__ == '__main__':
    j = juve(nome = 'Leonardo', idade = 0)
    print(j.nome, j.idade)
    j.idade = 20
    print(j.nome, j.idade)
    j.sobrenome = 'Muniz'
    print(j.nome, j.sobrenome, 'tem', j.idade, 'anos')
