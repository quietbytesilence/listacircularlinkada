# Dados de Teste
data = ["Gustavo", "Ingrid", "Paulo", "Jailson", "Patrick", "Eduardo"]

def mostrar():
    pointers = [hex(id(i)) for i in data]
    print("\n" * 5)
    for c, valor, end in zip(range(len(data)), data, pointers):
        print(f"Endereço: {end} | Valor: {valor} | Next: {pointers[c + 1] if c + 1 < len(pointers) else pointers[0]}")

def adicionar_inicio(valor):
    data.insert(0, valor)

def adicionar_fim(valor):
    data.append(valor)

def esvaziar_lista():
    data.clear() #Como o código é demonstrativo, a lista é limpa.

def remover_item(valor):
    data.remove(valor) if valor in data else print("Valor não encontrado na lista.")

while True:
    print(f"""
[0] - Sair
[1] - Adicionar no Início
[2] - Adicionar no Fim
[3] - Remover Item
[4] - Esvaziar Lista
[5] - Ver lista
    """)
    opt = input("Digite a opção desejada: ")    
    match opt:
        case '0': exit()
        case '1': adicionar_inicio(input("Digite o valor a ser adicionado no início: "))
        case '2': adicionar_fim(input("Digite o valor a ser adicionado no fim: "))
        case '3': remover_item(input("Digite o valor a ser removido: "))
        case '4': esvaziar_lista()
        case '5': mostrar()
        case _: print('Opção Inválida')

