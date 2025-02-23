import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Portfólio Kauan Rodrigues Lima", page_icon="images/icon.png", layout="wide")

# Sidebar com opção de menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navegação",  
        options=["Início", "Projetos", "Contato"],  
        icons=["house", "code", "envelope"],  
        menu_icon="cast",  
        default_index=0  
    )

# Importação dinâmica das páginas
if selected == "Início":
    import home
    home.show()

elif selected == "Projetos":
    import projetos
    projetos.show()

elif selected == "Contato":
    import contato
    contato.show()
