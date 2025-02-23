import streamlit as st

def show():
    st.title("🚀 Meus Projetos")

    projetos = [
        {"nome": "Sistema de Gestão de Estoque", "descricao": "Sistema completo com Django, Celery e Redis.", "link": "#"},
        {"nome": "Gerenciamento de Alunos", "descricao": "Controle de mensalidades com integração do Mercado Pago.", "link": "#"},
        {"nome": "API para E-commerce", "descricao": "API escalável usando Django Rest Framework.", "link": "#"}
    ]

    for projeto in projetos:
        with st.expander(projeto["nome"]):
            st.write(projeto["descricao"])
            st.markdown(f"[🔗 Ver projeto]({projeto['link']})")
