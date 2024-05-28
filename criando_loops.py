'''
Criando sua propria versao de loop
for num in [1,2,3,4,5]:
#Por de baixo dos panos esta acontecendo:
iter([1,2,3,4,5])

for letra in "Geek Uni":
#Por de baixo dos panos esta acontecendo:
iter("Geek Uni")


'''
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
meu_for("Geek University")
num = [5,6,7,8]
meu_for(num)
