'''Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get)
e um método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor
para criar alguma regra.'''

class result():
    def __init__(self, v1):
        self.n1 = v1*2
        self.n2 = v1**2

    def get_result1(self):
        #método self do resultado n1
        return self.n1

    def get_result2(self):
        #método self do resultado n2
        return self.n2

    def set_result1(self, v2):
        #método get do resultado n1
        self.n1 = v2*2

    def set_result2(self, v2):
        #método get do resultado n2
        self.n2 = v2**2

num = result(10)
print(f'O valor multiplicado por dois é igual a {num.get_result1()}\nO valor elevado a dois é igual a {num.get_result2()}')
num2=int(input('Digite um novo valor: '))
num.set_result1(num2)
num.set_result2(num2)
print(f'O novo valor multiplicado por dois é igual a {num.get_result1()}\nE elevado a dois é igual a {num.get_result2()}')


