import mysql.connector
def Conectar_banco():
        return mysql.connector.connect(  
        host="localhost",
        user="github",
        password="$$$$",
        database="loja"
    )

def Buscar_produto_por_nome():
        
        cnx = Conectar_banco()
        cursor = cnx.cursor()
        nome_produto = input("Digite o nome do produto:").strip()
        consultar_sgbd = "SELECT * FROM produtos WHERE LOWER(nome) = LOWER(%s)"
        cursor.execute(consultar_sgbd, (nome_produto,))
        resultado = cursor.fetchall()
        
        if resultado:
                for linha in resultado:
                        id_produto, nome, quantidade, preco = linha 
                        print(f"""O Produto possui as seguintes características:
                                    Id : {id_produto}
                                    Nome: {nome}
                                    Quantidade:{quantidade}
                                    Preço: {preco}""")
inicio = Conectar_banco()
busca = Buscar_produto_por_nome()
    
        
        else:
                print("Produto não encontrado no estoque")

              
