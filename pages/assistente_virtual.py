import streamlit as st
from streamlit_chat import message
from services.assistant import initialize_assistant

if st.secrets["assistant"]["enabled"] == "True":
    assistant = initialize_assistant()
else:
    assistant = None


# Função que lida com a mudança no campo de entrada
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    # Resposta do bot dependendo da pergunta
    response = get_bot_response(user_input)
    st.session_state.generated.append(response)


# Função para limpar o histórico de mensagens
def on_btn_click():
    st.session_state.past = []
    st.session_state.generated = []


# Função para gerar a resposta do chatbot
def get_bot_response(user_input):
    user_input = user_input.lower()

    response = assistant.send_message(user_input)
    return response


# Função para exibir o conteúdo do assistente virtual
def show():
    # Inicializa o estado das mensagens
    st.session_state.setdefault('past', [])
    st.session_state.setdefault('generated', [])

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.write("")

    with col2:

        # Título da página
        st.title("Assistente Virtual de Kauan")

        st.write("")

        message("Olá! Eu sou o assistente virtual de Kauan. Como posso ajudar você?", key="welcome")
        message("Você pode perguntar sobre as habilidades de Kauan, projetos que ele desenvolveu, habilidades que ele possui, como entrar em contato.", key="help")
        message("Digite sua pergunta abaixo para começar.", key="prompt")

        # Exibição do histórico de mensagens
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
            message(st.session_state['generated'][i], key=f"{i}_bot")

        # Entrada do usuário
        input_message = st.text_input("Digite sua pergunta:", key="user_input", help="Exemplo: Quais são as habilidades do Kauan?", on_change=on_input_change)

        # st.button("Enviar", on_click=on_input_change)

        # Botão para limpar o histórico de mensagens
        st.button("Limpar mensagens", on_click=on_btn_click)

    with col3:
        st.write("")


show()
