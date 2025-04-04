
# 🏡 Web Scraping de Imóveis - DF Imóveis

Este projeto utiliza o **Selenium** para automatizar a busca por imóveis no site [DF Imóveis]. Ele coleta informações relevantes sobre os imóveis encontrados, como **título, preço, metragem, quantidade de quartos e suítes**, os organiza em um `DataFrame` e os insere em um banco de dados **MySQL**.

🛠️ Fluxo do script:
> Acessa o site → Preenche os filtros → Busca os imóveis → Coleta dados → Insere no banco.


## 🚀 Funcionalidades

- Seleção de filtros personalizados na página de busca do site
- Coleta de links de imóveis com base nos filtros escolhidos.
- Acesso individual a cada anúncio e extração das seguintes informações:
  - 🏷️ Título  
  - 💰 Preço  
  - 📏 Metragem  
  - 🛏️ Quartos  
  - 🛁 Suítes  
  - 📝 Descrição  
  - 🔗 Link do anúncio
- Inserção automática dos dados no banco de dados MySQL (`tb_imoveis`).

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Selenium
- Pandas
- SQLAlchemy
- dotenv
- MySQL 


## ✅ Requisitos

- Python instalado
- Google Chrome + ChromeDriver (na pasta ou adicionado ao `PATH`)
- Banco de dados MySQL rodando localmente ou em um servidor
- Variáveis de ambiente configuradas (.env) para conexão com o banco de dados:

```ENV
            HOST=localhost
            PORT=3306
            USER=seu_usuario
            PASSWORD=sua_senha
            DATABASE=nome_do_banco

```
  
- Bibliotecas instaladas via `requirements.txt'

  



## 🗃️ Estrutura da Tabela tb_imoveis
A tabela pode ser criada usando o script **create_db_imoveis.sql** e terá este formato: 


### Estrutura da Tabela `tb_imoveis`

| Coluna    | Tipo                          |
|-----------|-------------------------------|
| id        | INT AUTO_INCREMENT PRIMARY KEY|
| titulo    | VARCHAR                       |
| preco     | FLOAT                         |
| metragem  | VARCHAR                       |
| quartos   | VARCHAR                       |
| suites    | VARCHAR                       |
| descricao | VARCHAR                       |
| link      | VARCHAR                       |



## 🔧 Configuração da Busca

Configure os parâmetros de busca diretamente no código, ajustando as variáveis conforme necessário. Abaixo estão os filtros utilizados:
| PARÂMETRO       | EXEMPLO                   |
|-----------------|---------------------------|
| `TIPO`          | `APARTAMENTO`             |
| `MODALIDADE`    | `VENDA`                   |
| `ESTADO`        | `DF`                      |
| `CIDADE`        | `BRASILIA / PLANO PILOTO` |
| `BAIRRO`        | `ASA NORTE`               |
| `QUARTOS`       | `1`                       |
| `VALOR_MAXIMO`  | `2000000`                 |
| `ENDERECO`      | `sqn 115`                 |

