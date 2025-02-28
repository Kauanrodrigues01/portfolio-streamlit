import streamlit as st
from .educacao import show_cursos


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

    icons_path = "https://raw.githubusercontent.com/Kauanrodrigues01/Kauanrodrigues01/refs/heads/main/icons/portfolio"

    skills = [
        ("Python", f"{icons_path}/python-dark.svg"),
        ("Django", f"{icons_path}/django.svg"),
        ("Postgres", f"{icons_path}/postgres-light.svg"),
        ("MySQL", f"{icons_path}/mysql-light.svg"),
        ("AWS", f"{icons_path}/aws-light.svg"),
        ("Docker", f"{icons_path}/docker.svg"),
        ("Git", f"{icons_path}/git.svg"),
        ("GitHub", f"{icons_path}/github-dark.svg"),
        ("VSCode", f"{icons_path}/vscode-light.svg"),
        ("Linux", f"{icons_path}/linux-light.svg"),
        ("Nginx", f"{icons_path}/nginx.svg"),
        ("CSS", f"{icons_path}/css.svg"),
        ("HTML", f"{icons_path}/html.svg"),
        ("Bootstrap", f"{icons_path}/bootstrap.svg"),
        ("Postman", f"{icons_path}/postman.svg")
    ]

    # Adiciona o estilo flexbox com CSS
    st.markdown(
        """
        <style>
            .skills-container {
                display: flex;
                flex-wrap: wrap; /* Faz os ícones quebrarem de linha conforme necessário */
                justify-content: center; /* Alinha os ícones no centro */
                gap: 20px; /* Espaçamento entre os ícones */
            }
            .skill-item {
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            .skill-item img {
                width: 50px;
            }
            .skill-item caption {
                font-size: 10px;
                margin-top: 5px;
                color: #777;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Cria a estrutura de habilidades com flexbox e loop
    skill_html = '<div class="skills-container">'
    for skill, icon in skills:
        skill_html += f'''
            <div class="skill-item">
                <img src="{icon}" alt="{skill}">
                <caption>{skill}</caption>
            </div>
        '''.strip()  # Remove espaços desnecessários ou quebras de linha extras
    skill_html += '</div>'

    # Exibe o HTML gerado
    st.markdown(skill_html, unsafe_allow_html=True)

