import psycopg2
from BD import Conexao

class Manipulacao():

    #Inserção de cadastro
    def inserir(self, cpf, nome, email):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            inserir = """insert into pessoas (cpf, nome, email) values ('{0}','{1}','{2}')""".format(cpf, nome, email)
            cursor.execute(inserir)
            conexao.commit()
            print("Cadastro inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    #Busca por nome de cadastros ativos
    def busca_nome(self, nome):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where nome like '%{0}%' and status = 1".format(nome)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(" ERROR:/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca por e-mail de cadastros ativos
    def busca_email(self, email):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where email like '%{0}%' and status = 1".format(email)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(" ERROR :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Verifica CPF existente no Bd
    def busca_cpf(self, cpf):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where cpf = '{0}'".format(cpf)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            if len(pessoas) >= 1:
                return True
            else:
                return False
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(" ERROR :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    #Busca por CPF de cadastros ativos
    def busca_pessoa_cpf(self, cpf):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where cpf like '%{0}%' and status = 1".format(cpf)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(" ERROR :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca de todos os cadastros inativos
    def busca(self):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where status = 0"
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(" ERROR :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
