from Pessoa import *

opcao = int(input("Escolha uma das opções abaixo. \n1 - Cadastrar\n2 - Editar\n3 - Remover\n4 - Consultar\n"))

if opcao == 1:
    Pessoa.cadastro()