import streamlit as st
from cursos import show as show_cursos

def show():
    # Nome em destaque
    st.markdown(
        """
        <h1 style="text-align: center;">Kauan Rodrigues Lima</h1>
        """, 
        unsafe_allow_html=True
    )
    
    st.write('')  # Espaço para separar
    st.write('')
    st.write('')
    st.write('')

    # Layout: Foto + Texto sobre mim (Centralizado)
    col1, col2, col3, col4 = st.columns([1, 1, 2, 1])  # Adicionando colunas vazias para centralizar

    with col1:
        st.write("")  # Espaço vazio para centralização

    with col2:
        st.image("images/perfil.jpg", width=200)  # Foto de perfil
    
    with col3:  # Conteúdo centralizado
        st.write(
            """
            Desenvolvedor Back-End especializado em Django e Django Rest Framework (DRF).
            Tenho experiência no desenvolvimento de aplicações web completas, APIs escaláveis 
            e automação de processos. Utilizo **Docker, AWS e GitHub Actions** para otimizar 
            a implantação e manutenção de sistemas.
            
            Minhas soluções vão além do código, trazendo **automação, integração com APIs** 
            e práticas modernas para tornar as aplicações mais eficientes e seguras.
            """
        )

    with col4:
        st.write("")  # Espaço vazio para centralização

    st.write("---")

    show_skills_and_tools()  # Exibição das habilidades e ferramentas

    st.write("---")
    
    show_cursos()  # Exibição dos cursos e certificações


def show_skills_and_tools():
    st.markdown("## Skills e Tools")
    st.write('')
    
    # Imagens representando as habilidades
    skills = [
        ("Python", "images/python-dark-icon.svg"),
        ("Django", "images/django-icon.svg"),
        ("Postgres", "images/postgres-light-icon.svg"),
        ("MySQL", "images/mysql-light-icon.svg"),
        ("AWS", "images/aws-light-icon.svg"),
        ("Docker", "images/docker-icon.svg"),
        ("Git", "images/git-icon.svg"),
        ("GitHub", "images/github-dark-icon.svg"),
        ("VSCode", "images/vscode-light-icon.svg"),
        ("Linux", "images/linux-light-icon.svg"),
        ("Nginx", "images/nginx-icon.svg"),
        ("CSS", "images/css-icon.svg"),
        ("HTML", "images/html-icon.svg"),
        ("Bootstrap", "images/bootstrap-icon.svg"),
        ("Postman", "images/postman-icon.svg")
    ]

    
    cols = st.columns(len(skills))

    for i, (skill, icon) in enumerate(skills):
        with cols[i]:
            st.image(icon, width=60, caption=skill,)