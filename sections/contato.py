import requests
import streamlit as st


def show():
    st.title("📩 Entre em Contato")

    st.write("Preencha o formulário abaixo para entrar em contato comigo. Responderei o mais rápido possível!")

    # Criando o formulário
    with st.form("contact_form"):
        name = st.text_input("Nome", placeholder="Digite seu nome")
        email = st.text_input("E-mail", placeholder="Digite seu e-mail")
        subject = st.text_input("Assunto", placeholder="Digite o assunto")
        message = st.text_area("Mensagem", placeholder="Digite sua mensagem aqui...")

        submit_button = st.form_submit_button("Enviar")

        if submit_button:
            if name and email and message:
                with st.spinner("Enviando mensagem..."):
                    # URL do formulário de envio de e-mail
                    formsubmit_url = st.secrets["links_contato"]["formsubmit"]
                    data = {"name": name, "email": email, "subject": subject, "message": message}

                    response = requests.post(formsubmit_url, data=data)

                    if response.status_code == 200:
                        st.success("✅ Mensagem enviada com sucesso! Entrarei em contato em breve.")
                    else:
                        st.error("❌ Ocorreu um erro ao enviar a mensagem. Tente novamente.")
            else:
                st.warning("⚠️ Preencha todos os campos antes de enviar.")
