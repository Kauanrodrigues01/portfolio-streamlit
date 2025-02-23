import streamlit as st
from cursos import show as show_cursos


def show():
    # Nome em destaque
    col1, col2, col3 = st.columns([1, 4, 1])  # Colunas para centralizar o conteúdo da página

    with col1:
        st.write("")

    with col2:
        st.markdown(
            """
            <h1 style="text-align: center;">Kauan Rodrigues Lima</h1>
            """,
            unsafe_allow_html=True
        )

        st.write('')
        st.write('')
        st.write('')
        st.write('')

        # Layout: Foto + Texto sobre mim (Centralizado)
        col1, col2, col3, col4 = st.columns([1, 1, 2, 1])

        with col1:
            st.write("")  # Espaço vazio para centralização

        with col2:
            st.image("images/perfil2.jpg", width=200)  # Foto de perfil

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

    with col3:
        st.write("")


def show_skills_and_tools():
    st.markdown("## Skills e Tools")
    st.write('')

    skills = [
        ("Python", "images/icons/python-dark-icon.svg"),
        ("Django", "images/icons/django-icon.svg"),
        ("Postgres", "images/icons/postgres-light-icon.svg"),
        ("MySQL", "images/icons/mysql-light-icon.svg"),
        ("AWS", "images/icons/aws-light-icon.svg"),
        ("Docker", "images/icons/docker-icon.svg"),
        ("Git", "images/icons/git-icon.svg"),
        ("GitHub", "images/icons/github-dark-icon.svg"),
        ("VSCode", "images/icons/vscode-light-icon.svg"),
        ("Linux", "images/icons/linux-light-icon.svg"),
        ("Nginx", "images/icons/nginx-icon.svg"),
        ("CSS", "images/icons/css-icon.svg"),
        ("HTML", "images/icons/html-icon.svg"),
        ("Bootstrap", "images/icons/bootstrap-icon.svg"),
        ("Postman", "images/icons/postman-icon.svg")
    ]

    cols = st.columns(len(skills))

    for i, (skill, icon) in enumerate(skills):
        with cols[i]:
            st.image(icon, width=60, caption=skill,)
