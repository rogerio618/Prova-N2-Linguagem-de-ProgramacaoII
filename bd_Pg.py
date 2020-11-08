"""1 – Crie um banco de dados no postgres com o nome prova e com a tabela
música. Faça a persistência de dois registros do tipo música no postgres
através do python. Deve conter pelo menos três campos na coleção: id, nome,
autor, gênero"""


import psycopg2
from BD import PGConexao

class ManipulacaoPG():

    #Inserção de dados
    def inserir(self, id, nome, autor, genero):
        
        try:
            #Estabelece conexão com o Bd
            conexao = PGConexao().get_connection()
            cursor = conexao.cursor()

            #Insere os dados na tabela musica
            inserir = """insert into musica (id, nome, autor, genero) values ('{0}','{1}','{2}','{3}')""".format(id, nome, autor, genero)
            cursor.execute(inserir)
            conexao.commit()
            print("PostgreSQL: Cadastro inserido com sucesso!")

        except (Exception, psycopg2.DatabaseError) as error:
            print("PostgreSQL: Algum erro aconteceu :/", error)
        
        finally:
            #Finaliza e encerra a conexão com o Bd
            if (conexao):
                cursor.close()
                conexao.close()
