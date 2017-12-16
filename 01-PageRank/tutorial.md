Snakes and Ladders é um famoso jogo de tabuleiro em que a cada rodada um jogador joga uma moeda não viciada e avança 1 casa se obtiver cara ou avança 2 casas se obtiver coroa. Se o jogador para no pé da escada, então ele imediatamente sobe para o topo da escada. Se o jogador cai na boca de um cobra então ele imediatamente escorrega para o rabo. O jogador sempre inicia no quadrado de número 1. O jogo termina quando ele atinge o quadrado de número 36.

## Método
Para o problema do Snakes and Ladders fizemos a implementação em Python das casas onde havia uma cobra ou uma escada na função shift(), que indica para onde deve ir o jogador que pare em uma delas:

(imagem da shift())

E implementamos também funções para calcular a cadeia de Markov e o Power Method:

(imagem das duas funções)

## A)

Para poder obter o diagrama de estados da cadeia de Markov, rodamos o script que fizemos e este foi o resultado:

(imagem da cadeia de markov)

## B)

Para calcular a distribuição estacionária da cadeia de Markov, rodamos nosso script de Power method 100 vezes, passando a cadeia e o número de vezes desejado na função `power_method(M,100)`

O resultado para cada posição do tabuleiro foi este:

(imagem do .txt que diz a chance de cada posição)

É possível ver que para a última posição do tabuleiro (#36) a chance de chegar (e vencer) a longo prazo é de 0.04101%.

Podemos também ver que as posições mais acessadas são #29, #16 e #4, sendo a posição #29 a mais acessada de todas.
