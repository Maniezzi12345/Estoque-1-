import mysql.connector

def buscar_produto_por_nome(nome_produto):
    # banco de dados fictício
    cnx = mysql.connector.connect(
        host="localhost",
        user="git",
        password="****",
        database="loja"
    )
    
    cursor = cnx.cursor()
    consulta_sgbd = "SELECT * FROM produtos WHERE LOWER(nome) = LOWER(%s)"
    cursor.execute(consulta_sgbd, (nome_produto,))
    

    resultado = cursor.fetchall()


    if resultado:
        for linha in resultado:
            id_produto,nome,quantidade,preco = linha 
            print(f"Id: {id_produto}")
            print(f"Nome: {nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço: {preco}")

    else:
        print("Produto não encontrado")
    

    cursor.close()
    cnx.close()


nome_produto = input("Digite o nome do produto: ").strip()
buscar_produto_por_nome(nome_produto)
