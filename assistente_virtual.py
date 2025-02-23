import streamlit as st
from streamlit_chat import message


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
    
    # Definindo respostas básicas para algumas perguntas comuns
    if "habilidades" in user_input:
        return "As habilidades de Kauan incluem: Django, Python, DRF, SQL, APIs RESTful, e muito mais."
    elif "projetos" in user_input:
        return "Kauan desenvolveu projetos como sistemas de gestão de estoque, APIs RESTful, e um sistema de agendamento."
    elif "contato" in user_input:
        return "Você pode entrar em contato com Kauan pelo email: kauan@example.com."
    else:
        return "Desculpe, não entendi sua pergunta. Tente perguntar sobre habilidades, projetos ou contato."

# Função para exibir o conteúdo do assistente virtual
def show():
    # Inicializa o estado das mensagens
    st.session_state.setdefault('past', [])
    st.session_state.setdefault('generated', [])

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
    input_message = st.text_input("Digite sua pergunta:", key="user_input", help="Exemplo: Quais são as habilidades do Kauan?")
    
    st.button("Enviar", on_click=on_input_change)

    # Botão para limpar o histórico de mensagens
    st.button("Limpar mensagens", on_click=on_btn_click)
