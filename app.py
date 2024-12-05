from modelos.restaurante import Restaurante
# aqui ele está importando de modelos.restaurante o que tiver em restaurante

# aqui definimos valores para as variáveis
restaurante_praca = Restaurante('Outback', 'Churrasco')
restaurante_praca.receber_avaliacao('Vinicius', 10)
restaurante_praca.receber_avaliacao('Lucas', 8)
restaurante_praca.receber_avaliacao('Matheus', 2)

# aqui é a função main que vai sempre trazer o metodo abaixo
def main():
    Restaurante.listar_restaurantes()

# aqui definimos a main e damos o nome main() para ela
if __name__ == '__main__':
    main()