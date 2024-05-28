def comer(comida,eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente se vive só uma vez'
    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8:
        return f'Dormi muito, estou atrasado'
    else:
        return f'Continuo cansado após dormir {num_horas} horas'

def eh_engracado(pessoa):
    #pass
    comediantes  = ['Jim Carrey','Bozo']
    if pessoa in comediantes:
        return True
    return False