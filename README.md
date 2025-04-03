
# Wimoveis_webscrapping

## 📌 Descrição

Este projeto utiliza o Selenium para automatizar a busca por imóveis no site **Wimóveis**. Ele coleta informações relevantes sobre os imóveis encontrados, como **título, preço, metragem, quantidade de quartos e suítes**, e salva os dados em um banco de dados MySQL.



##### Observação: As bibliotecas necessárias podem ser vistas no requirements.txt


### 🔧 Configuração da Busca

Configure os parâmetros de busca diretamente no código, ajustando as variáveis conforme necessário:

```python
TIPO = 'APARTAMENTO'
MODALIDADE = 'VENDA'
ESTADO = 'DF'
CIDADE = 'BRASILIA / PLANO PILOTO'
BAIRRO = 'ASA NORTE'
QUARTOS = '1'
VALOR = '2000000'
ENDERECO = 'sqn 115'
