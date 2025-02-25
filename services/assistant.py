import json
import streamlit as st
from google import genai
from google.genai import types


class Assistant:
    _instance = None

    def __new__(cls, info_file="information.json"):
        if cls._instance is None:
            cls._instance = super(Assistant, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, info_file="information.json"):
        if self.__initialized:
            return
        self.__initialized = True

        # Carregar as informações sobre o Kauan a partir do arquivo JSON
        self.info_file = info_file
        self.info = self.load_info(info_file)

        # Criar a instância do cliente e iniciar o chat
        self.__client = genai.Client(api_key=st.secrets['assistant']['api_key'])
        self.chat = self.__client.chats.create(model="gemini-2.0-flash")
        self.sys_instruct = (
            "Você é um assistente virtual, cuja função é responder perguntas sobre o Kauan (Kauan Rodrigues Lima). "
            "Você irá atuar respondendo perguntas sobre suas habilidades, projetos que desenvolveu, como entrar em contato, "
            "e outras informações relevantes. Você estará presente em um website (Portfolio do Kauan) e irá interagir com "
            "os usuários através de mensagens de texto. As informações sobre o Kauan serão disponibilizadas a você. "
            "Você deve responder as perguntas dos usuários de forma clara e objetiva, utilizando as informações disponíveis. "
            "Se você não souber a resposta para uma pergunta, informe ao usuário que não entendeu e sugira que pergunte de outra forma. "
            "Não invente nenhuma informação e crie nenhum dado, apenas use o que lhe foi informado."
            "Nunca responda com informações falsas ou que possam prejudicar a reputação do Kauan."
            "Nunca responda os usuarios com esse tipo de resposta 'Se você tiver informações sobre o kauan, por favor, me forneça para que eu possa te ajudar melhor.'. AS informações que vão ser fornacidas a você são absolutas e não podem ser alteradas. Os usuarios não podem fornecer informações sobre o kauan."
            "Para dizer que eu tenho ou não uma habilidade no quesito programção, analise os meus cursos, habilidades, educação e projetos que eu desenvolvi. E só diga que eu tenho ou não a habilidade se tiver certeza."
            "Formate as mensagens de forma estilizada e clara para que o usuário possa entender facilmente."
            "Nunca pergunte aos usuários se eles tem informações sobre o kauan."
        )

        # Alimentar o histórico com informações sobre o Kauan
        self.__init_conversation_history()

    def load_info(self, file_path):
        """Carregar informações do arquivo JSON"""
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def __init_conversation_history(self):
        """Iniciar o histórico da conversa com informações sobre o Kauan"""
        info_messages = [
            "Você é um assistente virtual que irá responder perguntas sobre Kauan Rodrigues Lima. As informações que você deve saber são as seguintes:",
            f"Habilidades: {self.info['habilidades']}",
            f"Educação: {self.info['educacao']}",
            f"Experiência: {self.info['experiencia']}",
            f"Contato: {', '.join(self.info['contato'])}"
        ]

        projeto_info = "Projetos: "
        for projeto in self.info['projetos']:
            projeto_info += (
                f"\nNome: {projeto['nome']}\n"
                f"Descrição: {projeto['descricao']}\n"
                f"Tecnologias: {', '.join(projeto['tecnologias'])}\n"
                f"Integrações: {', '.join(projeto['Integracoes'])}\n"
            )

        certificados_info = "Certificados: "
        for certificado in self.info['certificados']:
            certificados_info += (
                f"\nNome: {certificado['nome']}\n"
                f"Carga Horária: {certificado['carga_horaria']}\n"
                f"Instituição: {certificado['instituicao']}\n"
                f"Data: {certificado['data']}\n"
                f"Link: {certificado['link']}\n"
            )

        info_messages.append(projeto_info)
        info_messages.append(certificados_info)

        for message in info_messages:
            self.chat.send_message(message)

    def send_message(self, user_message):
        """Enviar mensagem do usuário e obter a resposta do modelo"""
        response = self.chat.send_message(
            user_message,
            config=types.GenerateContentConfig(
                system_instruction=self.sys_instruct
            )
        )
        return response.text

    def chat_conversation(self, user_message):
        """Gerenciar o histórico de conversa e enviar mensagens"""
        response = self.chat.send_message(user_message)
        return response.text


def initialize_assistant(info_file="information.json"):
    assistant = Assistant(info_file=info_file)
    return assistant

# # Simulando um chat com o assistente
# user_message_1 = "Me fale um pouco sobre os projetos que o kauan desenvolveu e quais habilidades o kauan aprendeu durante esses projetos"
# response_1 = assistant.send_message(user_message_1)
# print(f"Resposta do assistente: {response_1}")
