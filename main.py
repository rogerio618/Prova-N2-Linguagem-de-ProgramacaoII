from Q1 import ManipulacaoPG
from Q3 import ManipulacaoMongo

persistenciaPG = ManipulacaoPG()
persistenciaMongo = ManipulacaoMongo()

print("\n\nInserção de dados na Tabela e Collection de Músicas \n\nInforme os dados abaixo solicitados")
nome = input("Nome: ")
autor = input("Autor: ")
genero = input("Gênero: ")
persistenciaPG.inserir(nome, autor, genero)
persistenciaMongo.inserir(nome, autor, genero)