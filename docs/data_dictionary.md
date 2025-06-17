# **Base de Vendas (Tabela fato) -> "base_vendas_clean.csv"**

| Coluna       | Tipo    | Descrição                                    |
| ------------ | ------- | -------------------------------------------- |
| ID\_VENDA    | Texto   | Identificador único da venda (UUID).         |
| DATA\_VENDA  | Date    | Data em que a venda foi efetuada.            |
| CLIENTE\_ID  | Inteiro | Código do cliente.                           |
| ANO\_MES     | Texto   | Ano e mês em que foi realizada a compra.     |
| VALOR\_TOTAL | Decimal | Valor total da venda (limpo de separadores) |
| CIDADE | Texto | Cidade do cliente que realizou a compra
| ESTADO | Texto | Unidade federativa
| NOME_CLIENTE | Texto | Nome do cliente que realizou a compra
| PRODUTO_ID | Inteiro | Identificador único do produto
| PRODUTO_NOME | Texto | Nome do produto
| VALOR_UNITARIO | Decimal | Valor unitário do produto
| QUANTIDADE | Inteiro | Quantidade de itens comprados
| CANAL_VENDA | Texto | Meio o qual foi feita a compra
| DEVOLVIDA | Texto | Coluna binária que indica </br> se a compra foi devolvida ou não
------------------------------------------------------------------------
<br>
<br>
<br>

# **DimProduto (Tabela dimensão) → “DimProduto”**
| Coluna       | Tipo    | Descrição                                    |
| ------------ | ------- | -------------------------------------------- |
| PRODUTO_ID | Inteiro	|Identificador único do produto	|
|ProdutoNome |	Texto	| Nome do produto	PRODUTO_NOME |
|ValorUnitario| Decimal| 	Preço unitário padrão do produto |
--------------------------------------------------------------

<br>
<br>
<br>

# **DimVendedor (Tabela dimensão) → “DimVendedor”**
| Coluna        | Tipo    | Descrição                                     |
| ------------- | ------- | --------------------------------------------- |
| VENDEDOR_ID   | Inteiro | Identificador único do vendedor               |
| NOME_VENDEDOR  | Texto   | Nome do vendedor              |
| CANAL_VENDA    | Texto   | Canal de venda principal associado  |
--------------------------------------------------------------
<br>
<br>
<br>

# **DimCliente (Tabela dimensão) → “DimCliente”**
| Coluna       | Tipo    | Descrição                                       |
| -------------| ------- | ----------------------------------------------- |
| CLIENTE_ID   | Inteiro | Identificador único do cliente                  |
| NOME_CLIENTE  | Texto   | Nome do cliente                |
| CIDADE       | Texto   | Cidade de residência do cliente       |
| ESTADO       | Texto   | Unidade federativa de residência      |
--------------------------------------------------------------
<br>
<br>
<br>


# **DimData (Tabela dimensão) → “DimData”**
| Coluna     | Tipo     | Descrição                                              |
| ---------- | -------- | ------------------------------------------------------ |
| Date       | Date     | Data completa sem hora     |
--------------------------------------------------------------
