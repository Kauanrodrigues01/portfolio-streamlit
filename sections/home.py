import streamlit as st


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
        col1, col2, col3, col4 = st.columns([1, 2, 4, 1])

        with col1:
            st.write("")  # Espaço vazio para centralização

        with col2:
            st.image("images/perfil.jpg", width=200)  # Foto de perfil

        with col3:  # Conteúdo centralizado
            st.write(
                """
                **Desenvolvedor Back-End** especializado em **Django e Django Rest Framework (DRF)**.
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
    st.markdown("## Habilidades e Ferramentas")
    st.write('')

    skills = [
        ("Python", "images/icons/python-dark.svg"),
        ("Django", "images/icons/django.svg"),
        ("Postgres", "images/icons/postgres-light.svg"),
        ("MySQL", "images/icons/mysql-light.svg"),
        ("AWS", "images/icons/aws-light.svg"),
        ("Docker", "images/icons/docker.svg"),
        ("Git", "images/icons/git.svg"),
        ("GitHub", "images/icons/github-dark.svg"),
        ("VSCode", "images/icons/vscode-light.svg"),
        ("Linux", "images/icons/linux-light.svg"),
        ("Nginx", "images/icons/nginx.svg"),
        ("CSS", "images/icons/css.svg"),
        ("HTML", "images/icons/html.svg"),
        ("Bootstrap", "images/icons/bootstrap.svg"),
        ("Postman", "images/icons/postman.svg")
    ]

    cols = st.columns(len(skills))

    for i, (skill, icon) in enumerate(skills):
        with cols[i]:
            st.image(icon, width=60, caption=skill,)


def show_cursos():
    st.markdown("## Cursos e Certificações")
    st.write('')
    st.write('')

    # Cursos e Certificações
    cursos01 = [
        ("Django Master - Aplicações Web", "45 horas", "Pycodebr", "Ainda-vou-adicionar-o-link"),
        ("Integration Master - Integração de Sistemas", "10 horas", "Pycodebr", "Ainda-vou-adicionar-o-link"),
        ("Django Web Framework e Django Rest Framework (DRF)", "79 horas", "Udemy", "https://www.udemy.com/certificate/UC-41a72004-0486-42c7-b290-150fa0abe3f5/"),
        ("Python 3 do Básico ao Avançado", "141 horas", "Udemy", "https://www.udemy.com/certificate/UC-e1015c77-bfc7-435d-b38a-d5ec084fe54b/"),
    ]

    cursos02 = [
        ("IA Master - Integração com IA, RAG, LangChain, Agents de IA", "20 horas", "Pycodebr", "Ainda-vou-adicionar-o-link"),
        ("AWS Cloud Foundations", "15 horas", "AWS academy", "Ainda-vou-adicionar-o-link"),
        ("Google AI Essentials", "8 horas", "Google", "Ainda-vou-adicionar-o-link"),
        ("Docker: do Básico ao Avançado", "13 horas", "Udemy", "Ainda-vou-adicionar-o-link"),
    ]

    # Dividindo em duas colunas
    col1, col2 = st.columns(2)

    with col1:
        for curso, horas, plataforma, link in cursos01:  # Primeiro grupo de cursos
            st.markdown(f"##### {curso}")
            st.markdown(f"<span style='font-size: 14px;'>Duração: <strong>{horas}</strong></span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'>Plataforma: <strong>{plataforma}</strong></span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'><a href='{link}' target='_blank'>Ver Certificado</a></span>", unsafe_allow_html=True)

            st.markdown("---")  # Linha entre os cursos

    with col2:
        for curso, horas, plataforma, link in cursos02:  # Segundo grupo de cursos
            st.markdown(f"##### {curso}")
            st.markdown(f"<span style='font-size: 14px;'>Duração: <strong>{horas}</strong></span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'>Plataforma: <strong>{plataforma}</strong></span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'><a href='{link}' target='_blank'>Ver Certificado</a></span>", unsafe_allow_html=True)

            st.markdown("---")  # Linha entre os cursos
