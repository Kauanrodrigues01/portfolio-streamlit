import streamlit as st


FORMACOES = [
    {
        'nome': 'Técnico em Desenvolvimento de Sistemas',
        'instituicao': 'EEEP Adolfo Ferreira de Sousa',
        'carga_horaria': '1540 horas',
        'periodo': '2023 - 2025',
        'descricao': 'Curso técnico focado em programação, bancos de dados, programação orientada a objetos, desenvolvimento web, redes de computadores, segurança da informação, qualidade e testes de software e entre outros.',
        'certificado_link': None
    },
]


def show():
    # Nome em destaque
    col1, col2, col3 = st.columns([1, 4, 1])  # Colunas para centralizar o conteúdo da página

    with col2:
        st.markdown(
            """
            <h1>🎓 Educação</h1>
            """,
            unsafe_allow_html=True
        )
        
        st.write('')
        st.write('')
        
        show_formacoes()  # Exibição das formações
        
        st.write('')
        st.write('')
        
        show_cursos()  # Exibição dos cursos e certificações

        


def show_formacoes():
    st.markdown('## Formações')
    
    st.write('')
    st.write('')
    
    for formacao in FORMACOES:
        with st.container():
            st.subheader(f'{formacao['nome']} ({formacao['periodo']})')
            st.write(f'**Instituição:** {formacao['instituicao']}')
            st.write(f'**Carga Horária:** {formacao['carga_horaria']}')
            st.write(f'**Período:** {formacao['periodo']}')
            st.write(f'**Descrição:** {formacao['descricao']}')

            if formacao['certificado_link']:
                st.markdown(f'[📜 Ver Certificado]({formacao['certificado_link']})', unsafe_allow_html=True)

            st.write('---')  # Separador entre formações


def show_cursos():
    st.markdown('## Cursos e Certificações')
    st.write('')
    st.write('')

    # Cursos e Certificações
    cursos01 = [
        ('Django Master - Aplicações Web', '45 horas', 'Pycodebr', 'Ainda-vou-adicionar-o-link'),
        ('Integration Master - Integração de Sistemas', '10 horas', 'Pycodebr', 'Ainda-vou-adicionar-o-link'),
        ('Django Web Framework e Django Rest Framework (DRF)', '79 horas', 'Udemy', 'https://www.udemy.com/certificate/UC-41a72004-0486-42c7-b290-150fa0abe3f5/'),
        ('Python 3 do Básico ao Avançado', '141 horas', 'Udemy', 'https://www.udemy.com/certificate/UC-e1015c77-bfc7-435d-b38a-d5ec084fe54b/'),
    ]

    cursos02 = [
        ('IA Master - Integração com IA, RAG, LangChain, Agents de IA', '20 horas', 'Pycodebr', 'Ainda-vou-adicionar-o-link'),
        ('AWS Cloud Foundations', '15 horas', 'AWS academy', 'Ainda-vou-adicionar-o-link'),
        ('Google AI Essentials', '8 horas', 'Google', 'Ainda-vou-adicionar-o-link'),
        ('Docker: do Básico ao Avançado', '13 horas', 'Udemy', 'https://www.udemy.com/certificate/UC-11245ba7-611e-4881-9493-25a872612d16/'),
        ('Segurança em Aplicações Web', '7,5 horas', 'Udemy', 'Ainda-vou-adicionar-o-link'),
    ]

    # Dividindo em duas colunas
    col1, col2 = st.columns(2)

    with col1:
        for curso, horas, plataforma, link in cursos01:  # Primeiro grupo de cursos
            st.markdown(f'##### {curso}')
            st.markdown(f'<span style="font-size: 14px;">Duração: <strong>{horas}</strong></span>', unsafe_allow_html=True)
            st.markdown(f'<span style="font-size: 14px;">Plataforma: <strong>{plataforma}</strong></span>', unsafe_allow_html=True)
            st.markdown(f'<span style="font-size: 14px;"><a href="{link}" target="_blank">Ver Certificado</a></span>', unsafe_allow_html=True)

            st.markdown('---')  # Linha entre os cursos

    with col2:
        for curso, horas, plataforma, link in cursos02:  # Segundo grupo de cursos
            st.markdown(f'##### {curso}')
            st.markdown(f'<span style="font-size: 14px;">Duração: <strong>{horas}</strong></span>', unsafe_allow_html=True)
            st.markdown(f'<span style="font-size: 14px;">Plataforma: <strong>{plataforma}</strong></span>', unsafe_allow_html=True)
            st.markdown(f'<span style="font-size: 14px;"><a href="{link}" target="_blank">Ver Certificado</a></span>', unsafe_allow_html=True)

            st.markdown('---')  # Linha entre os cursos