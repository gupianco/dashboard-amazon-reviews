class animal:
    def __init__(self,patas,peso):
        self.patas = patas
        self.pelo = peso
    
    def andar(self):
        print('andando...')


class cachorro(animal):
    def latir(self):
        print('latindo...')


cachorro1 = cachorro(4,10)
