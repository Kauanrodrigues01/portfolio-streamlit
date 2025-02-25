import streamlit as st
from streamlit_option_menu import option_menu
from services.assistant import initialize_assistant


# Configuração da página
st.set_page_config(page_title="Portfólio Kauan Rodrigues Lima", layout="wide")
st.logo("images/icons/python-dark.svg")


if st.secrets["assistant"]["enabled"] == "True":
    initialize_assistant()

# # Sidebar com opção de menu
with st.sidebar:
    selected_page = option_menu(
        menu_title="Navegação",
        menu_icon="cast",
        options=["Início", "Projetos", "Contato", "Assistente Virtual"],
        icons=["house", "code", "envelope", "chat"],
    )
    # Informações de contato com ícones
    link_linkedin = st.secrets["links_contato"]["linkedin"]
    link_github = st.secrets["links_contato"]["github"]
    link_instagram = st.secrets["links_contato"]["instagram"]
    link_email = st.secrets["links_contato"]["email"]
    icons_path = "https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/icons/portfolio"
    
    st.write("---")

    st.markdown("### Contato")
    
    html_code = f"""
        <style>
            .contact-links a {{
                color: white;
                text-decoration: none;
                transition: color 0.3s ease;
            }}
            .contact-links a:hover {{
                color: blue;
            }}
        </style>

        <div class="contact-links" style="display: flex; flex-direction: column; gap: 8px;">

            <div style="display: flex; align-items: center; gap: 8px;">
                <img src="{icons_path}/linkedin.svg" width="20">
                <a href="{link_linkedin}" target="_blank">Kauan Rodrigues Lima</a>
            </div>

            <div style="display: flex; align-items: center; gap: 8px;">
                <img src="{icons_path}/github-dark.svg" width="20">
                <a href="{link_github}" target="_blank">Kauanrodrigues01</a>
            </div>

            <div style="display: flex; align-items: center; gap: 8px;">
                <img src="{icons_path}/instagram.svg" width="20">
                <a href="{link_instagram}" target="_blank">kauan_mrl</a>
            </div>

            <div style="display: flex; align-items: center; gap: 8px;">
                <img src="{icons_path}/gmail-dark.svg" width="20">
                <a href="{link_email}" target="_blank">kauanrl09@gmail.com</a>
            </div>

        </div>
    """
    
    html_code = html_code.replace("\n", "").replace("    ", "")
    
    st.markdown(html_code, unsafe_allow_html=True)

if selected_page == "Início":
    from sections.home import show
    show()

elif selected_page == "Projetos":
    from sections.projetos import show
    show()

elif selected_page == "Contato":
    from sections.contato import show
    show()

elif selected_page == "Assistente Virtual":
    from sections.assistente_virtual import show
    show()