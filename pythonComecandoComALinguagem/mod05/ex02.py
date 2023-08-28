# Temos o seguinte código:
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3

# Que imprime:
# 1
# 4
# 7
# 10

for contador in range(1,11,3):
    print(contador)

# o valor z em range(x,y,z) define os "steps", a quantidade de valores incrementados ao contador usado