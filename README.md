# lab_cryptografia
# 🔐 Crypto Hybrid System

Este projeto é uma aplicação web desenvolvida com **Flask** que implementa um **Sistema de Criptografia Híbrida**. O objetivo é demonstrar a integração de algoritmos de criptografia simétrica (AES) e assimétrica (RSA) para garantir a segurança e a eficiência no tratamento de dados.

## 🚀 Sobre o Projeto

A criptografia híbrida combina o melhor de dois mundos:
1.  **Criptografia Simétrica (Fernet/AES):** Utilizada para cifrar a mensagem original de forma rápida.
2.  **Criptografia Assimétrica (RSA):** Utilizada para cifrar a chave simétrica, permitindo que ela seja transmitida ou armazenada com segurança, sendo decifrada apenas por quem possui a chave privada correspondente.

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **Flask:** Framework web para o backend e rotas.
* **Cryptography:** Biblioteca robusta para implementação dos protocolos de segurança.
* **HTML5/CSS3:** Para a interface de usuário (Front-end).
* **Git/GitHub:** Para controle de versionamento.

## 📂 Estrutura de Pastas

```text
crypto-hybrid-system/
├── static/              # Arquivos CSS e estilização
├── templates/           # Arquivos HTML (Jinja2)
├── venv/                # Ambiente virtual (não enviado ao git)
├── app.py               # Servidor Flask e gerenciamento de rotas
├── crypto_utils.py      # Lógica matemática e funções criptográficas
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Regras de exclusão para o Git
