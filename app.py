import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Portfólio Kauan Rodrigues Lima", page_icon="images/icon.png", layout="wide")

# Sidebar com opção de menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navegação",
        options=["Início", "Projetos", "Assistente Virtual"],
        icons=["house", "code", "chat"],
        menu_icon="cast",
        default_index=0
    )

    st.write('---')

    # Informações de contato
    st.markdown("### Contato")
    st.write("LinkedIn: [Kauan Rodrigues Lima](https://www.linkedin.com/in/kauan-rodrigues-lima-727486321/)")
    st.write("GitHub: [Kauanrodrigues01](https://github.com/Kauanrodrigues01)")
    st.write("Instagram: [kauan_mrl](https://www.instagram.com/kauan_mrl/)")

# Importação dinâmica das páginas
if selected == "Início":
    import home
    home.show()

elif selected == "Projetos":
    import projetos
    projetos.show()

elif selected == "Assistente Virtual":
    import assistente_virtual
    assistente_virtual.show()
