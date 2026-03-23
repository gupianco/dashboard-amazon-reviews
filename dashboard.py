import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Dashboard de Reviews - Amazon Echo 2',
    page_icon='🌟',
    layout='wide'
)

df = pd.read_csv('arquivos/reviews_limpo.csv')

st.sidebar.header("🔍 Filtros")

cor_disponivel = sorted(df['Cor do produto'].unique())
cor_selecionada = st.sidebar.multiselect('Cor do produto', cor_disponivel, default=cor_disponivel)

usuario_disponivel = sorted(df['Usuário Verificado'].unique())
tipo_usuario = st.sidebar.multiselect('Tipo de usuário', usuario_disponivel, default=usuario_disponivel)

rating_min = st.sidebar.selectbox(
    'Rating mínimo',
    [1, 2, 3, 4, 5]
)

df_filtrado = df[
    (df['Cor do produto'].isin(cor_selecionada)) &
    (df['Usuário Verificado'].isin(tipo_usuario)) &
    (df['Avaliação'] >= rating_min)
]

st.title("🌟 Dashboard de Reviews - Amazon Echo 2")

col1, col2, col3, col4 = st.columns(4)

col1.metric("⭐ Média de avaliações", round(df_filtrado['Avaliação'].mean(), 2))
col2.metric("📦 Total de avaliações", df_filtrado.shape[0])
col3.metric(
    "⭐ Nota mais comum",
    df_filtrado['Avaliação'].mode()[0]
)
col4.metric('✅ % Verificados',
    round((df_filtrado['Usuário Verificado'] == 'Compra Verificada').mean() * 100, 2)            
)

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        st.subheader('📊 Distribuição das Avaliações')

        fig1 = px.histogram(
            df_filtrado,
            x='Avaliação',
            nbins=5,
            text_auto=True
        )

        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico.")

with col_graf2:
    if not df_filtrado.empty:
        st.subheader('🎨 Avaliação por Cor do Produto')

        df_cor = df_filtrado.groupby('Cor do produto')['Avaliação'].mean().reset_index()

        fig2 = px.bar(
            df_cor,
            x='Cor do produto',
            y='Avaliação',
            labels={
                'Cor do produto': 'Cor',
                'Avaliação': 'Média de Avaliação'
            }
        )

        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        st.subheader('👤 Avaliação por Tipo de Usuário')

        df_user = df_filtrado.groupby('Usuário Verificado')['Avaliação'].mean().reset_index()

        fig3 = px.bar(
            df_user,
            x='Usuário Verificado',
            y='Avaliação'
        )

        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico.")

with col_graf4:
    if not df_filtrado.empty:
        st.subheader('📈 Evolução das Avaliações')

        df_filtrado['Data de Avaliação'] = pd.to_datetime(df_filtrado['Data de Avaliação'])

        df_tempo = df_filtrado.groupby(
            df_filtrado['Data de Avaliação'].dt.to_period('M'))['Avaliação'].mean().reset_index()

        df_tempo['Data de Avaliação'] = df_tempo['Data de Avaliação'].astype(str)

        fig4 = px.line(
            df_tempo,
            x='Data de Avaliação',
            y='Avaliação'
        )

        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico.")

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)