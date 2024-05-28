'''
Teste de memoria com generators
'''
# Funcao usando lista (1244 MB/ Geek 550mB)
# def fibbonaci(max):
#     nums = []
#     a,b = 0,1
#     while len(nums) < max:
#         nums.append(b)
#         a,b = b, a+b
#     return nums
#
# for n in fibbonaci(50000):
#     print(n)

# Funcao usando geradores (1120 Mb/ Geek 3Mb)
def fibbonaci(max):
    a,b,contador = 0,1,0
    while contador < max:
        a,b = b, a+b
        yield a
        contador +=1
for n in fibbonaci(100000):
    print(n)