import streamlit as st
import pandas as pd

df = pd.read_csv("vendas_5000_linhas.csv")


df["regiao"] = df["regiao"].str.upper()

df["total_venda"] = df["quantidade"]*df["preco_unitario"]

taxas = {
    "Boleto": 0.025,
    "Crédito": 0.05,
    "Pix": 0,
    "Débito": 0.05
}

df["taxa_pagamento"] = df["forma_pagamento"].map(taxas)

impostos = {
    "Eletrônicos": 0.075,
    "Móveis": 0.05,
    "Acessórios": 0.025
}

df["imposto_pago"] = df["categoria"].map(impostos)


df["lucro_total"] = (df["total_venda"] - (df["total_venda"]*df["taxa_pagamento"]) - (df["total_venda"]*df["imposto_pago"])).round(2)

# st.write(df["categoria"].unique())
# st.write(df["forma_pagamento"].unique())
st.dataframe(df)