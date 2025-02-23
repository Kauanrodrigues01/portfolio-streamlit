import streamlit as st


def show():
    st.title("🚀 Meus Projetos")

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
        st.markdown("- Back-end: Django (Python), PostgreSQL, Celery, Redis")
        st.markdown("- Front-end: Bootstrap, Chart.js")
        st.markdown("- Integrações: API Evolution (WhatsApp) e Gemini (IA)")
        st.markdown("- Docker para deploy e escalabilidade")
        st.markdown("🔗[Ver projeto](https://github.com/Kauanrodrigues01/sge)")

    with st.expander("ChatBot com IA - Projeto Python e IA"):
        st.write("Área em construção...")

    with st.expander("Gerenciamento de Alunos - Controle de Mensalidades com Mercado Pago"):
        st.write("Área em construção...")

    with st.expander("Flix App - Aplicativo de Catálogo de Filmes com Streamlit"):
        st.write("Área em construção...")

    with st.expander("Flix API - API para Catálogo de Filmes"):
        st.write("Área em construção...")

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
        st.markdown("- Back-end: Django, Django Rest Framework, PostgreSQL")

    with st.expander("Blog de Receitas - Projeto Django FullStack"):
        st.write("Área em construção...")
