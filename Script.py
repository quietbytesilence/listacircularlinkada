import os

def limpar_terminal(pause=False):
    """
    Limpa o terminal. Se 'pause' for True, pede ao usuário para pressionar <ENTER> antes de limpar.
    """
    if pause:
        input('Pressione <ENTER> para continuar.')  # Pausa e espera o usuário pressionar <ENTER>
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal de acordo com o sistema operacional

class Node:
    def __init__(self, data):
        """
        Inicializa um nó com dados e aponta para o próximo nó.
        """
        self.data = data  # Dados armazenados no nó
        self.next = None  # Referência ao próximo nó, inicialmente None

class ListaCircularSimplesmenteEncadeadaNaoOrdenada:
    def __init__(self):
        """
        Inicializa a lista circular simplesmente encadeada não ordenada.
        """
        self.last = None  # O último nó da lista, inicialmente None

    def add_at_end(self, data):
        """
        Adiciona um novo nó com os dados fornecidos no final da lista.
        """
        new_node = Node(data)  # Cria um novo nó com os dados fornecidos
        if self.last is None:  # Se a lista estiver vazia
            self.last = new_node  # O novo nó é o único e último nó
            self.last.next = self.last  # O nó aponta para ele mesmo, formando um ciclo
        else:
            new_node.next = self.last.next  # Novo nó aponta para o primeiro nó
            self.last.next = new_node  # O último nó agora aponta para o novo nó
            self.last = new_node  # O novo nó é agora o último nó

    def add_at_start(self, data):
        """
        Adiciona um novo nó com os dados fornecidos no início da lista.
        """
        new_node = Node(data)  # Cria um novo nó com os dados fornecidos
        if self.last is None:  # Se a lista estiver vazia
            self.last = new_node  # O novo nó é o único e último nó
            self.last.next = self.last  # O nó aponta para ele mesmo, formando um ciclo
        else:
            new_node.next = self.last.next  # Novo nó aponta para o antigo primeiro nó
            self.last.next = new_node  # O último nó agora aponta para o novo nó

    def remove(self, data):
        """
        Remove todos os nós com o valor especificado.
        """
        if self.last is None:  # Se a lista estiver vazia
            print("Lista está vazia")  # Informa que a lista está vazia
            return

        current = self.last.next  # Começa a busca do início da lista
        prev = self.last  # O nó anterior ao nó atual
        removed = False  # Flag para verificar se algum nó foi removido

        while True:
            if current.data == data:  # Se encontrou o nó com 'data'
                if current == self.last:  # Se o nó a ser removido é o último
                    if current.next == self.last:  # Se é o único nó na lista
                        self.last = None  # Lista se torna vazia
                    else:
                        prev.next = current.next  # O nó anterior agora aponta para o próximo do nó removido
                        self.last = prev  # O último nó é o nó anterior ao removido
                elif current == self.last.next:  # Se o nó a ser removido é o primeiro
                    self.last.next = current.next  # O último nó aponta para o próximo do nó removido
                else:  # Se o nó a ser removido está no meio
                    prev.next = current.next  # O nó anterior aponta para o próximo do nó removido
                removed = True  # Marca que um nó foi removido

                if current == current.next:  # Se a lista se tornou vazia
                    self.last = None
                    break

                current = current.next  # Move para o próximo nó
            else:
                prev = current  # Atualiza o nó anterior
                current = current.next  # Move para o próximo nó

            if prev == self.last:  # Se retornou ao início da lista
                break

        if removed:
            print(f"Todos os elementos com valor {data} foram removidos.")  # Informa que os elementos foram removidos
        else:
            print(f"Elemento {data} não encontrado na lista.")  # Informa que o elemento não foi encontrado

    def clear(self):
        """
        Esvazia a lista completamente.
        """
        if self.last is None:  # Se a lista já estiver vazia
            print("A lista já está vazia.")
        else:
            self.last = None  # Define o último nó como None, efetivamente esvaziando a lista
            print("A lista foi esvaziada.")

    def display(self):
        """
        Exibe todos os nós da lista.
        """
        if self.last is None:  # Se a lista estiver vazia
            print("Lista está vazia")  # Informa que a lista está vazia
            return
        current = self.last.next  # Começa a exibição do início da lista
        primeiro = True
        while True:
            if primeiro:
                print('Head'); primeiro = False
                print(f"--> {hex(id(current))} - Valor: {current.data}, next: {hex(id(current.next))}")  # Exibe o endereço, valor e o próximo nó
            else:
                print(f"--> {hex(id(current))} - Valor: {current.data}, next: {hex(id(current.next))}")  # Exibe o endereço, valor e o próximo nó
            current = current.next  # Move para o próximo nó
            if current == self.last.next:  # Se retornou ao início da lista
                break

def menu():
    """
    Exibe um menu para interação com a lista circular e processa a escolha do usuário.
    """
    cll = ListaCircularSimplesmenteEncadeadaNaoOrdenada()  # Cria uma nova lista circular

    while True:
        limpar_terminal(True)  # Limpa o terminal e espera o usuário pressionar <ENTER>
        print("\n--- Menu ---")
        print("1. Adicionar no fim")
        print("2. Adicionar no início")
        print("3. Exibir lista")
        print("4. Remover elemento por valor")
        print("5. Esvaziar lista")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")  # Solicita ao usuário para escolher uma opção
        
        if escolha == '1':
            valor = input("Digite o valor para adicionar no fim: ")  # Solicita o valor para adicionar no fim
            cll.add_at_end(valor)  # Adiciona o valor no fim da lista
        elif escolha == '2':
            valor = input("Digite o valor para adicionar no início: ")  # Solicita o valor para adicionar no início
            cll.add_at_start(valor)  # Adiciona o valor no início da lista
        elif escolha == '3':
            cll.display()  # Exibe todos os nós da lista
        elif escolha == '4':
            valor = input("Digite o valor do elemento a ser removido: ")  # Solicita o valor do nó a ser removido
            cll.remove(valor)  # Remove todos os nós com o valor especificado
        elif escolha == '5':
            cll.clear()  # Esvazia a lista completamente
        elif escolha == '6':
            print("Saindo...")  # Informa que o programa está saindo
            break
        else:
            print("Opção inválida! Escolha novamente.")  # Informa que a opção escolhida é inválida

# Executar o menu
menu()  # Chama a função menu para iniciar o programa
