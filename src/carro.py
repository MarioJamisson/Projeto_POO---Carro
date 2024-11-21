# Classe Carro criada para representar um carro com atributos e comportamentos.
class Carro:
    def __init__(self, gasMax, pasMax):
        # Construtor da classe, inicializa os atributos do carro: capacidade do tanque (gasMax) e capacidade máxima de passageiros (pasMax).
        self.__pas = 0  # Inicializa o número de passageiros como 0.
        self.__gas = 0  # Inicializa a quantidade de gasolina como 0.
        self.__km = 0   # Inicializa a distância percorrida como 0.
        self.__gasMax = gasMax  # Define o limite máximo de gasolina do carro.
        self.__pasMax = pasMax  # Define o limite máximo de passageiros do carro.
  
    # Método para exibir as informações atuais do carro, como o número de passageiros, quantidade de gasolina e distância percorrida.
    def mostrar_informacoes(self):
        print(f"Numero de passageiros: {self.__pas}, Quantidade de gasolina: {self.__gas}, Distancia percorrida: {self.__km} KM")

    # Método que mostra o quanto o tanque de gasolina está cheio em porcentagem (de 0 a 100).
    def mostrarPorcentagem(self):
        porcentagem = int((self.__gas / self.__gasMax) * 100)  # Calcula a porcentagem de gasolina no tanque.
        print(f"Tanque está {porcentagem}% cheio")  # Exibe a porcentagem do tanque.

    # Método que adiciona um passageiro ao carro, se não exceder a capacidade máxima.
    def entrarCarro(self):
        if self.__pas >= self.__pasMax:  # Se o número de passageiros for maior ou igual ao máximo, exibe uma mensagem de erro.
            print("Erro: quantidade maxima de passageiros atingida")
        else:
            self.__pas += 1  # Caso contrário, adiciona um passageiro.

    # Método que remove um passageiro do carro, se houver passageiros no carro.
    def saiCarro(self):
        if self.__pas > 0:  # Se houver pelo menos um passageiro, remove um.
            self.__pas -= 1
        else:
            print("Erro: Nenhum passageiro no carro")  # Exibe erro caso não haja passageiros para remover.

    # Método para abastecer o carro com gasolina, com verificação de limites.
    def abastecer(self, gaso: int):
        if gaso > self.__gasMax:  # Se a quantidade de gasolina for maior que a capacidade do tanque, exibe erro.
            print("Você ultrapassou a capacidade do tanque em:", gaso - self.__gasMax, "litros.")
            print("Limite de abastecimento atingido. Tanque 100% cheio.")
            self.__gas = self.__gasMax  # O tanque é completado até o limite máximo.
        elif gaso <= 0:  # Se o valor de gasolina for negativo ou zero, exibe erro.
            print("Erro: Quantidade de gasolina inválida.")
        else:
            self.__gas += gaso  # Caso contrário, adiciona a quantidade de gasolina ao tanque.

    # Método para dirigir o carro por uma certa distância, com verificação de combustível e passageiros.
    def dirigir(self, distancia: int):
        if self.__gas <= 0:  # Se não houver gasolina, exibe um erro.
            print("Erro: Não há gasolina suficiente.")
        elif self.__pas <= 0:  # Se não houver passageiros, exibe um erro.
            print("Erro: Não há passageiros no carro.")
        else:
            consumo = min(self.__gas, distancia)  # O carro usa o máximo de gasolina disponível para percorrer a distância.
            self.__gas -= consumo  # Reduz a quantidade de gasolina.
            self.__km += consumo  # Aumenta a distância percorrida.
            if consumo < distancia:  # Se o carro não conseguiu percorrer toda a distância, avisa que ficou sem gasolina.
                print("Ficou sem gasolina, não foi possível completar a viagem.")
