# Importa a classe Carro
from src.carro import Carro

# Cria uma instância do carro com capacidade máxima de gasolina e passageiros
carro1 = Carro(gasMax=100, pasMax=2)

# Exibe o status do carro (passageiros, gasolina e km)
carro1.mostrar_informacoes()
carro1.mostrarPorcentagem()

# Adiciona passageiros
carro1.entrarCarro()
carro1.entrarCarro()

# Exibe o status do carro após adicionar passageiros
carro1.mostrar_informacoes()
carro1.mostrarPorcentagem()

#Remove passageiros
carro1.saiCarro()

# Exibe o status do carro após remover passageiros
carro1.mostrar_informacoes()
carro1.mostrarPorcentagem()

# Abastece o carro, mas não ultrapassa a capacidade do tanque
carro1.abastecer(250)

# Dirige o carro por 30 km
carro1.dirigir(30)

# Exibe o status final do carro
carro1.mostrar_informacoes()
carro1.mostrarPorcentagem()
