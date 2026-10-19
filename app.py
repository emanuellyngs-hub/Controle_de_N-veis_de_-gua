from colorama import Fore, Style, init

init(autoreset=True)  # Inicializa o colorama para que as cores sejam resetadas automaticamente após cada print 

# Lista com as mensagens dos níveis de água
mensagens = ["Nível muito baixo: situação crítica!", "Nível baixo.", "Nível médio: situação normal.", "Nível alto.", "Nível muito alto: situação de alerta!"]

## Função que escolhe a cor conforme o nível 
def escolher_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

### Define o nível atual do reservatório (de 1 a 5)
nivel_atual = 1 #poderá ser alterado para testar diferentes níveis

##### Exibir a situação no terminal
if nivel_atual >= 1 and nivel_atual <= 5:
    mensagem = mensagens[nivel_atual - 1]
    cor = escolher_cor(nivel_atual)

print(f"Nível atual do reservatório: {nivel_atual}")
print(f"Mensagem: {mensagem}")
print(f"Cor: {cor}")
print(f"Mensagem com colorida e sublinhado: {cor}{Style.BRIGHT}{mensagem}{Style.RESET_ALL}")