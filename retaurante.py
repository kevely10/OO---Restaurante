class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome.title()  #.title() deixa a primeira letra maiuscula
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)}  |  {"Categoria".ljust(25)}  |  {"Status".ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)}  |  {restaurante.categoria.ljust(25)}  |  {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_restaurantes(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('praça','Gurmet')
restaurante_praca.alternar_restaurantes()
restaurante_pizza = Restaurante ('pizza','Italiana')

Restaurante.listar_restaurantes()