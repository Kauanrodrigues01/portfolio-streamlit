import streamlit as st

def show():
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
            st.markdown(f"<span style='font-size: 14px;'>Duração: {horas}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'>Plataforma: {plataforma}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'><a href='{link}' target='_blank'>Ver Certificado</a></span>", unsafe_allow_html=True)

            st.markdown("---")  # Linha entre os cursos

    with col2:
        for curso, horas, plataforma, link in cursos02:  # Segundo grupo de cursos
            st.markdown(f"##### {curso}")
            st.markdown(f"<span style='font-size: 14px;'>Duração: {horas}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'>Plataforma: {plataforma}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='font-size: 14px;'><a href='{link}' target='_blank'>Ver Certificado</a></span>", unsafe_allow_html=True)

            st.markdown("---")  # Linha entre os cursos
