import psycopg2
from pymongo import MongoClient


#Conexao com Postgree
class PGConexao():
    def get_connection(self):
        #Dados de acesso ao banco
        conexao = psycopg2.connect(user="postgres",password="1234", host="127.0.0.1", port="5432", database="prova")
        return conexao

#Conexao com MongoDB
class MongoConexao():
    def connection(self,json):
        try:
            
            #Dados de acesso ao banco
            cliente = MongoClient('localhost', 27017)
            
            #Definindo base de dados
            banco = cliente.prova

            #Definindo collection
            google = banco.musica 
            id = google.insert_one(json).inserted_id
        
        #Tratamento de erro
        except Exception as e:
            print("MongoDB: Oppss! Algum erro aconteceu :/", e)
            print(json)