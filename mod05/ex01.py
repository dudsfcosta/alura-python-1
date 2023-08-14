# Temos o seguinte loop usando while:

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1

# Qual das opções abaixo possui o mesmo resultado usando for .. range?
# Resposta correta: alternativa a
for contador in range(1,11):
    print(contador)

# o intervalo(x,y) na função range funciona com x sendo incluído no intervalo, e y sendo excluído.
# logo, teríamos que range = [x,y[