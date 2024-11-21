
# Projeto Carro

Este projeto simula o funcionamento de um carro com controle de passageiros, combustível e quilometragem. Ele oferece um conjunto de comandos para interagir com o carro, como embarcar, desembarcar, abastecer, e dirigir. O objetivo é gerenciar esses atributos e garantir que o carro só execute as ações possíveis dentro de seus limites.

## Funcionalidades

1. **Controle de Passageiros**: Você pode embarcar e desembarcar passageiros, respeitando o limite máximo de ocupantes.
2. **Abastecimento de Combustível**: O tanque do carro pode ser abastecido, mas não pode ultrapassar o limite máximo de combustível.
3. **Dirigir**: O carro pode ser dirigido, consumindo combustível e aumentando a quilometragem, mas só se houver passageiros e combustível suficientes.
4. **Exibição de Estado**: O estado atual do carro pode ser visualizado, incluindo o número de passageiros, quantidade de combustível e quilômetros percorridos.

## Comandos

### `mostrar_informacoes(self)`

Mostra o estado atual do carro.

Exemplo de saída:
```
pass: 0, gas: 0, km: 0
```

### `mostrar_porcentagem(self)`

Mostra a porcentagem atual do tanque do carro.

Exemplo de saída:
```
tanque: 0% cheio
```

### `__init__`

Inicializa o carro para o estado inicial:
- Tanque vazio.
- 0 passageiros.
- 0 quilômetros percorridos.
- Máximo de 2 passageiros.
- Máximo de 100 litros de gasolina.

### `entrarCarro(self)`

Embarca uma pessoa no carro, se não ultrapassar o número máximo de passageiros.

**Exemplo:**
- Se houver 2 passageiros, o comando não terá efeito e mostrará a mensagem: 
  ```
  fail: limite de pessoas atingido
  ```

### `saiCarro(self)`

Desembarca uma pessoa do carro.

**Exemplo:**
- Se não houver ninguém no carro, a mensagem será:
  ```
  fail: nao ha ninguem no carro
  ```

### `abastecer(self, gaso)`

Abastece o tanque com a quantidade de litros especificada.

**Exemplo:**
- Se tentar abastecer além do limite do tanque, o excesso será descartado e o tanque será preenchido até o máximo de 100 litros.

### `dirigir(self, distancia)`

Dirige o carro pela distância especificada.

- O carro só pode ser dirigido se houver passageiros e combustível suficiente.
- Se não houver passageiros, a mensagem será:
  ```
  fail: nao ha ninguem no carro
  ```
- Se o tanque estiver vazio, a mensagem será:
  ```
  fail: tanque vazio
  ```
- Se não houver combustível suficiente para a distância inteira, o carro dirigirá o máximo possível e exibirá:
  ```
  fail: tanque vazio após andar {qtd} km
  ```

---

## Estrutura do Projeto

Este projeto é organizado da seguinte forma:

```
/src
    /carro.py  # Contém a classe Carro e a lógica principal
/test
    /teste.py  # Testes automatizados para validar a funcionalidade da classe Carro
```

---

## Como Rodar o Projeto

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd Projeto_POO---Carro
   ```

2. **Instalar as dependências (nao necessario)**:

   Instale as dependências usando `pip`:

   ```bash
   pip install -r requirements.txt
   ```
---

## Como Funciona o Código

### Classe `Carro`

A classe `Carro` possui os seguintes atributos e métodos:

#### Atributos:
- `pass`: número atual de passageiros.
- `passMax`: número máximo de passageiros.
- `gas`: quantidade atual de gasolina no tanque.
- `gasMax`: capacidade máxima do tanque de combustível.
- `km`: quilômetros percorridos.

#### Métodos:
- `entrarCarro`: Adiciona um passageiro ao carro (se não exceder o limite de passageiros).
- `saiCarro`: Remove um passageiro do carro (não permite que o número de passageiros seja negativo).
- `abastecer`: Abastece o carro com a quantidade de gasolina fornecida, sem ultrapassar o limite do tanque.
- `dirigir`: Dirige o carro pela distância especificada, consumindo gasolina e aumentando a quilometragem.
- `mostrar_informacoes`: Mostra o estado atual do carro (passageiros, gasolina e quilometragem).
- `mostrar_porcentagem`: Mostra a porcentagem atual do tanque.

---

## Testes

O código foi testado usando o arquivo test.py para garantir que as funcionalidades funcionem corretamente. O teste está localizado na pasta `/test`.

### Testes Principais:
1. Testar a entrada de passageiros.
2. Testar a saída de passageiros.
3. Testar o abastecimento de combustível.
4. Testar a direção do carro, incluindo a verificação de passageiros e combustível.
5. Testar as mensagens de erro para casos de falhas, como quando não há combustível ou passageiros.

---

## Contribuições

Se você quiser contribuir para o projeto, fique à vontade para abrir um **pull request**. Certifique-se de que os testes estejam funcionando antes de enviar.

---

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
