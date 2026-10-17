from colorama import Fore, Style

def exibir_nivel(nivel):
    if nivel == 1:
        print(niveis[0] + Style.RESET_ALL)
    elif nivel == 2:
        print(niveis[1] + Style.RESET_ALL)
    elif nivel == 3:
        print(niveis[2] + Style.RESET_ALL)
    elif nivel == 4:
        print(niveis[3] + Style.RESET_ALL)
    elif nivel == 5:
        print(niveis[4] + Style.RESET_ALL)
    else:
        print("Nível inválido. Por favor, insira um nível entre 1 e 5.")

niveis = ['Nível 1: ' + Fore.RED + "Muito baixo (crítico)",
          'Nível 2: ' + Fore.YELLOW + "Baixo",
          'Nível 3: ' + Fore.GREEN + "Médio",
          'Nível 4: ' + Fore.CYAN + "Alto",
          'Nível 5: ' + Fore.BLUE + "Muito alto"]
exibir_nivel(1)
exibir_nivel(2)
exibir_nivel(3)
exibir_nivel(4)
exibir_nivel(5)
