import streamlit as st
from services.assistant import initialize_assistant


# Configuração da página
st.set_page_config(page_title="Portfólio Kauan Rodrigues Lima", layout="wide")
st.logo("images/icons/python-dark.svg")


if st.secrets["assistant"]["enabled"] == "True":
    initialize_assistant()

pages = [
    st.Page("pages/home.py", title="Início", default=True),
    st.Page("pages/projetos.py", title="Projetos"),
    st.Page("pages/contato.py", title="Contato"),
    st.Page("pages/assistente_virtual.py", title="Assistente Virtual")
]

pg = st.navigation(pages, position="sidebar", expanded=True)

pg.run()

# # Sidebar com opção de menu
with st.sidebar:
    # selected = option_menu(
    #     menu_title="Navegação",
    #     menu_icon="layout-sidebar",
    #     options=["Início", "Projetos", "Contato", "Assistente Virtual"],
    #     icons=["house", "code", "person", "chat"],
    #     default_index=0
    # )

    # Informações de contato com ícones
    link_linkedin = st.secrets["links_contato"]["linkedin"]
    link_github = st.secrets["links_contato"]["github"]
    link_instagram = st.secrets["links_contato"]["instagram"]
    link_email = st.secrets["links_contato"]["email"]

    st.markdown("### Contato")

    col1, col2 = st.columns([1, 8], gap="small")
    with col1:
        st.image("images/icons/linkedin.svg", width=20)
    with col2:
        st.write(f"[Kauan Rodrigues Lima]({link_linkedin})")

    col1, col2 = st.columns([1, 8], gap="small")
    with col1:
        st.image("images/icons/github-dark.svg", width=20)
    with col2:
        st.write(f"[Kauanrodrigues01]({link_github})")

    col1, col2 = st.columns([1, 8], gap="small")
    with col1:
        st.image("images/icons/instagram.svg", width=20)
    with col2:
        st.write(f"[kauan_mrl]({link_instagram})")

    col1, col2 = st.columns([1, 8], gap="small")
    with col1:
        st.image("images/icons/gmail-dark.svg", width=20)
    with col2:
        st.write(f"[kauanrl09@gmail.com]({link_email})")
