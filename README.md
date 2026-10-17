# Exibidor de Níveis Coloridos

Script simples em Python que exibe no terminal cinco níveis (de "Muito baixo" a "Muito alto"), cada um com uma cor diferente, usando a biblioteca [colorama](https://pypi.org/project/colorama/).

## Como funciona

A função `exibir_nivel(nivel)` recebe um número inteiro de 1 a 5 e imprime a descrição correspondente, já colorida. Se o valor estiver fora desse intervalo, mostra uma mensagem de erro.

| Nível | Descrição            | Cor      |
|-------|----------------------|----------|
| 1     | Muito baixo (crítico)| Vermelho |
| 2     | Baixo                | Amarelo  |
| 3     | Médio                | Verde    |
| 4     | Alto                 | Ciano    |
| 5     | Muito alto           | Azul     |

As descrições ficam na lista `niveis`, e `Style.RESET_ALL` é aplicado ao final de cada impressão para que a cor não "vaze" para o restante do terminal.

## Requisitos

- Python 3.x
- colorama

## Instalação

```bash
pip install colorama
```

## Como executar

Salve o código em um arquivo (por exemplo, `app.py`) e execute:

```bash
python app.py
```

## Exemplo de saída

```
Nível 1: Muito baixo (crítico)   (em vermelho)
Nível 2: Baixo                   (em amarelo)
Nível 3: Médio                   (em verde)
Nível 4: Alto                    (em ciano)
Nível 5: Muito alto              (em azul)
```

## Uso da função

```python
exibir_nivel(3)   # imprime "Nível 3: Médio" em verde
exibir_nivel(9)   # imprime "Nível inválido. Por favor, insira um nível entre 1 e 5."
```

## Estrutura do código

- `niveis`: lista com os textos e cores de cada nível.
- `exibir_nivel(nivel)`: escolhe e imprime o texto correspondente ao nível informado.
- Ao final do arquivo, a função é chamada para os níveis de 1 a 5 como demonstração.