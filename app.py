from modelo.restaurante import Restaurante

Restaurante_praca = Restaurante('praça',  'gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('japa', 'japonesa')

restaurante_mexicano.alternar_estado()


def main():
    pass

if __name__== '_main_':
    main()