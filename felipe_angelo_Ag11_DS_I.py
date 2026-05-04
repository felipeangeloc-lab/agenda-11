from colorama import Fore, Style

# Inicializa a biblioteca  colorama 


def exibir_alerta(nivel):

    # Inicializa cada com sua respctiva cor e texto em função de cada nível 

    if nivel == 1:
        cor = Fore.RED
        mensagem = "Muito baixo (crítico)"
    elif nivel == 2:
        cor = Fore.YELLOW
        mensagem = "Baixo"
    elif nivel == 3:
        cor = Fore.GREEN
        mensagem = "Médio"
    elif nivel == 4:
        cor = Fore.CYAN
        mensagem = "Alto"
    elif nivel == 5:
        cor = Fore.BLUE
        mensagem = "Muito alto (alerta)"
   

    # Exibe em função de cada item chamado da lista (níveis)
    
    print("Nível", nivel, ":", cor, mensagem)

def main():
    
    # Simula o níveis em função da lista
    
    print("--- MONITORAMENTO DO RESERVATÓRIO ---")

    # Lista de níveis para o teste
    niveis = [1, 2, 3, 4, 5]

    for n in niveis:
        exibir_alerta(n)

    
# Chama programa principal

main()