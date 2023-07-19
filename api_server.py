#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI
import json
from zeep import Client

app = FastAPI()

# URL do WSDL da API
url = 'https://uniquechic.com.br/api/v2_soap?wsdl=1'

# Credenciais
username = 'powerbi'
api_key = 'NadZtD7bHZkbYzBHM82Dp7'

# Função para obter os detalhes dos produtos
def get_products():
    client = Client(url)
    try:
        # Chamar o método de login para obter o sessionId
        session_id = client.service.login(username, api_key)

        # Chamar o método catalogProductList com o sessionId e o filtro, usando a visualização de loja padrão
        result = client.service.catalogProductList(sessionId=session_id, storeView='default', filters={})

        # Exibir os detalhes de alguns produtos (por exemplo, os primeiros 10 produtos)
        products_info = []
        for idx, product in enumerate(result):
            if idx >= 10:  # Limite para 10 produtos apenas para teste
                break

            product_id = product.product_id
            sku = product.sku
            name = product.name

            # Montar o objeto com as informações dos produtos (somente ID, SKU e Nome)
            product_info = {
                'Product ID': product_id,
                'SKU': sku,
                'Name': name,
            }
            products_info.append(product_info)

        return products_info

    except Exception as e:
        return {'error': f"Erro ao obter informações dos produtos: {e}"}

@app.get("/get_products")
def get_products_route():
    return get_products()


# In[ ]:




