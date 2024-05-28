'''
POO - Classes
Em POO, Classes são modelos dos objetos do mundo real representados computacionalmente

Ex> Imagine que voce queira fazer um sistema para automatizar o controle das lampadas de sua casa
Obeserve que existe diversos tipos de dados, int, float, str, mas nao existe o dado lampada

Classes podem ter:
    - Atributos: Representam as carcateristicas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso de uma lâmpada, possivelmente
    iriamos querer saber se ela é 110V ou 220V, se ela é branca, amarela ou outra cor, qual a luminosi
    dade dela, etc...

    - Metodos (funcoes): Representam o comportamento do objeto. Ou seja, as acoes que este objeto pode
    realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente
    iriamos querer no nosso sistema era de ligar ou desligar o sistema.

OBS: NOSSAS classes devem ser feitos com letra inicial maiuscula

OBS: Quando estamos planejando um software, e definimos quais classes teremos que ter no sistema,
chamamos estes objetos que serão mapeados para classes de entidadea. Ex: Lampada
'''
class Lampada:
    pass

lamp = Lampada()
print(type(lamp)) #Agora sim existe um dado lampada
