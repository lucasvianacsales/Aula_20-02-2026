import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dados_lojas = {
    "meses": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"],
    "Loja 1": [3000, 3500, 4000, 1200, 1600, 3500],
    "Loja 2": [2500, 3000, 3800, 1500, 2000, 3200],
    "Loja 3": [4000, 4200, 3900, 2000, 2500, 4100]
}

df = pd.DataFrame(dados_lojas)

st.title("Análise de Lojas")
st.divider()

loja = st.selectbox("Escolha a loja:", ["Loja 1", "Loja 2", "Loja 3", "Todas as lojas"])

if st.button("Mostrar Dados"):

    if loja != "Todas as lojas":

        st.subheader(f"Dados de {loja}")
        st.dataframe(df[["meses", loja]])

        total = df[loja].sum()
        st.markdown(f"Faturamento total (R$): {total}")

        st.subheader(f"Gráfico de {loja}")

        plt.figure()
        plt.plot(df["meses"], df[loja], marker="o")
        plt.xlabel("Meses")
        plt.ylabel("Vendas mensais (R$)")
        plt.grid(True)
        st.pyplot(plt)

    else:


        df["Total Mensal"] = df["Loja 1"] + df["Loja 2"] + df["Loja 3"]

        st.subheader("Dados de todas as lojas")
        st.dataframe(df[["meses", "Total Mensal"]])

        total_geral = df["Total Mensal"].sum()
        st.markdown(f"Faturamento total geral (R$): {total_geral}")

        st.subheader("Gráfico de todas as lojas")

        plt.figure()
        plt.plot(df["meses"], df["Total Mensal"], marker="o")
        plt.xlabel("Meses")
        plt.ylabel("Vendas totais mensais (R$)")
        plt.grid(True)
        st.pyplot(plt)