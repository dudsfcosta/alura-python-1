# aula extra sobre formatações
# ======================== Formatação genérica ======================== #

print("Tentativa {} de {}".format(1, 3))
# output: Tentativa 1 de 3
# usando a formatação {}, {}, {...}, {} os argumentos disponíveis serão usados em sequência.

print("Tentativa {1} de {0}".format(1, 3))
# output: Tentativa 3 de 1
# usando a formatação {0}, {1}, {...}, {n} os argumentos disponíveis serão usados de acordo com o placeholder.

# ======================== Formatação de pontos flutuantes ======================== #

print("R$ {}".format(1.599846))
# output: R$ 1.59

print("R$ {:f}".format(1.59))
# output: R$ 1.590000

print("R$ {:.2f}".format(1.599846))
# output: R$ 1.60

print("R$ {:.2f}".format(1.5))
# output: R$ 1.50

# Numa situação onde queremos que o ponto fique sempre no mesmo local, ou seja, ele deve ser o quinto caractere.
# Para essa formatação, precisamos dizer quantos caracteres o número terá no máximo, no nosso caso são 7 (4 números,
# mais o ponto, mais as duas casas decimais). Então vamos passar o valor 7 dentro das chaves também:
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))
# output: R$ 1234.50
# output: R$    1.50
# Ou seja, dos 7 caracteres, os três últimos serão o ponto mais dois números das casas decimais. Agora espaços
# ficam na frente quando um número for menor! Deixando o ponto sempre como quinto caractere. Se quisermos preencher os
# espaços em branco com zeros, é só passar um 0 antes do 7:
print("R$ {:07.2f}".format(1.5))
# output: R$ 0001.50

# ======================== Formatação de pontos flutuantes ======================== #

print("R$ {:07d}".format(4))
# output: R$ 0000004
print("Data {:02d}/{:02d}".format(9, 4))
# output: Data 09/04
print("Data {:02d}/{:02d}".format(19, 11))
# output: Data 19/11
