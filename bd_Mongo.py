""" Crie um banco de dados no mongo com o nome prova e com a coleção
música. Faça a persistência de dois registros do tipo música no mongo através
do python. Deve conter pelo menos três campos na coleção: nome, autor,
gênero"""


from BD import MongoConexao
from pymongo import MongoClient

class ManipulacaoMongo():

    #Inserção de dados
    def inserir(self, nome, autor, genero):
        
        #Estabelece conexão com o Banco de Dados
        conexao = MongoConexao()

        #Insere os dados na collection
        inserir = {'nome' : nome, 'autor' : autor, 'genero' : genero}
        conexao.connection(inserir)
        print("MongoDB: Cadastro inserido com sucesso!")
