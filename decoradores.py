'''
Decaradores
- sao funcoes
- envolvem outras funcoes e aprimoram seus comportamentos
- tambem sao exemplos de Higher Order Fuctional
- sintaxe prorpia, usando "@" (Syntact Sugar / Açucar sintético)

# Decoreators como funcoes (Sintaxe nao recomendada / Sem acucar sintático)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer em conhecer")
        funcao()
        print("Tenha um otimo dia")
    return sendo

def saudacao():
    print("Seja bem vindo ao Geek University")

teste = seja_educado(saudacao)
teste()

def raiva():
    print("Eu te odeio")

raiva_educada = seja_educado(raiva)
raiva_educada()


# Decorators com Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer em conhecer")
        funcao()
        print("Tenha um execlente dia")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")
apresentando()

'''

"""
Site:
---------------------------------------------------------
HOME |   SERVIÇOS      |   PRODUTOS  | ADMINISTRAÇÃO
----------------------------------------------------------
OBS: Nao é um codigo funcional
def checa_login():
    if not request.usuario():
        rediect("https://suaempresa.com)
        
def home(request):
    return 'Pode acessar o home'
    
def servicos(request):
    return 'pode acessar o servicos'
    
def produtos(request):
    return 'pode acessar os produtos'
    
@checa_login
def admin(request):
    return 'Pode acessar o admin'

"""
# OBS: Nao confunda Decorators com Decorators Fuctional

