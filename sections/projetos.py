import streamlit as st


def show():
    col1, col2, col3 = st.columns([1, 4, 1])  # Colunas para centralizar o conteúdo da página

    with col1:
        st.write("")

    with col2:
        st.title("Projetos Desenvolvidos")

        st.write("")

        st.write("Aqui estão alguns dos projetos que desenvolvi ao longo do meu aprendizado como desenvolvedor. Cada projeto foi uma oportunidade de aprender novas tecnologias, práticas de programação e trabalhar em desafios reais.")

        st.write("")

        # SGE
        with st.expander("Sistema de Gestão de Estoque (SGE) - Projeto Django FullStack"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write("")
            with col2:
                st.image("images/projetos/sge/dashboard.png", width=800)
            with col3:
                st.write("")
            st.write("O SGE é uma plataforma para gerenciar estoques de maneira eficiente, controlando produtos, fornecedores e movimentações de entradas e saídas. Utiliza inteligência artificial para sugerir reposição de estoque e otimizar a gestão, além de gerar gráficos e métricas sobre vendas e produtos.")
            st.write("Tecnologias utilizadas:")
            st.markdown("- Back-end: Python, Django, PostgreSQL, Celery, Redis")
            st.markdown("- Front-end: Bootstrap, Chart.js")
            st.markdown("- Integrações: API Evolution (WhatsApp) e Gemini (IA)")
            st.markdown("- Docker para deploy e escalabilidade")
            st.markdown("🔗[Ver projeto](https://github.com/Kauanrodrigues01/sge)")

        # CHATBOT COM IA
        with st.expander("ChatBot com IA - Projeto Python e IA"):
            st.write("Área em construção...")

        # GESTÃO DE ALUNOS
        with st.expander("Gerenciamento de Alunos - Controle de Mensalidades com Mercado Pago"):
            st.write("Área em construção...")

        # FLIX APP
        with st.expander("Flix App - Web App de Catálogo de Filmes com Streamlit"):
            st.write("Área em construção...")

        # FLIX API
        with st.expander("Flix API - API para Catálogo de Filmes"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write("")
            with col2:
                st.image("images/projetos/flix-api/swagger.png", width=800)
            with col3:
                st.write("")

            st.write("O Flix API é uma API para gerenciar um catálogo de filmes, com funcionalidades de CRUD, busca, filtros e autenticação de usuários. Com documentação interativa, facilita o desenvolvimento de aplicações front-end e integrações com outras plataformas.")

            st.write("A API foi projetada para ser simples e eficiente, oferecendo funcionalidades completas, como:")
            st.markdown("- Cadastro e gerenciamento de filmes, gêneros, atores, avaliações.")
            st.markdown("- Busca de filmes por título, gênero, popularidade, data de lançamento.")
            st.markdown("- Autentificação de usuários com JWT.")
            st.markdown("- Documentação interativa com Swagger.")

            st.write("Tecnologias utilizadas:")
            st.markdown("- Back-end: Django, Django Rest Framework, PostgreSQL")
            st.markdown("- Docker gerenciamento de containers")
            st.markdown("🔗[Ver projeto](https://github.com/Kauanrodrigues01/flix-api)")

        # TEACHERHUNT
        with st.expander("Teacherhunt - API de Busca de Professores Particulares"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write("")
            with col2:
                st.image("images/projetos/teacherhunt/swagger.jpeg", width=800)
            with col3:
                st.write("")
            st.write("O Teacherhunt é uma API para conectar alunos e professores particulares de forma rápida e prática. Com filtros de busca, avaliações e chat integrado, facilita a contratação de aulas particulares.")
            st.write("A API foi projetada para facilitar o dia a dia de estudantes e educadores, oferecendo funcionalidades completas, como:")
            st.markdown("- Cadastro e gerenciamento de professores e alunos.")
            st.markdown("- Busca de professores por matéria de interesse.")
            st.markdown("- Agendamento, aceitação e cancelamento de aulas.")
            st.markdown("- Avaliações e favoritos para professores.")
            st.markdown("- Redefinição de senha e ativação de conta por email.")
            st.markdown("- Autentificação e recuperação de contas com JWT.")
            st.markdown("- Documentação interativa com Swagger.")
            st.write("Tecnologias utilizadas:")
            st.markdown("- Back-end: Django, Django Rest Framework, PostgreSQL, Docker")

        # BLOG DE RECEITAS
        with st.expander("Blog de Receitas - Projeto Django FullStack"):
            st.write("Área em construção...")

        # ALURA SPACE
        with st.expander("Alura Space - Projeto Django FullStack"):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write("")
            with col2:
                st.image("images/projetos/aluraspace/home.png", width=800)
            with col3:
                st.write("")

            st.write("Alura Space é uma aplicação Django desenvolvida durante a formação da Alura sobre python e Djnago, essa aplicação permite: gerenciar e compartilhar imagens. É uma galeria de imagens que permite aos usuários fazer upload, editar, buscar, favoritar e curtir imagens. Além disso, os usuários podem gerenciar seus perfis, visualizar suas imagens e interagir com o conteúdo através de likes e favoritos.")

            st.write("")

            st.write("Principal funcionalidades:")
            st.markdown("- Cadastro e autenticação de usuários.")
            st.markdown("- Gestão de imagens: upload, edição, busca, favoritos, curtidas.")
            st.markdown("- Busca e filtros de imagens por categoria, nome e autor.")
            st.markdown("- Perfis de usuários com informações e imagens favoritas.")

            st.write("")

            st.write("Tecnologias utilizadas:")
            st.markdown("- Back-end: Python, Django")
            st.markdown("- Front-end: HTML, CSS, JavaScript")

            st.write("")

            st.write("🔗[Ver projeto](https://github.com/Kauanrodrigues01/Django-S3-crud/blob/main/README.md)")

    with col3:
        st.write("")
