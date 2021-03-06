'''
No Python, o comportamento dos operadores é defenido por métodos especiais.
vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''

class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<class 'Retangulo({self.x},{self.y})'>"

    def __add__(self,other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x,novo_y)
    
    def __lt__(self,other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True

    def __gt__(self,other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True

r1 = Retangulo(10,20)
r2 = Retangulo(10,20)
r3 = r1 + r2

print(r3>r1)