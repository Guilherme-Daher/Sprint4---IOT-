# 🧠 Projeto de Reconhecimento Facial com OpenCV

Este projeto implementa um sistema de reconhecimento facial utilizando Python e OpenCV. Ele permite cadastrar rostos via webcam, treinar um modelo LBPH e realizar autenticação facial em tempo real.

---

## 👥 Integrantes

- Guilherme Daher – 98611  
- Gabriel Toledo – 551654  
- Gustavo Akio – 550241  
- Gabriel Freitas – 550187  
- Heitor Nobre – 551539
  
---

## 📌 Objetivo

Criar um sistema simples e funcional de reconhecimento facial que possa identificar usuários previamente cadastrados com base em imagens capturadas pela webcam. Realizando uma integração entre as Sprints de Physical Computing (IoT & IoB) e Mobile Development.

---

## ⚙️ Instalação

1. Clone o repositório ou copie os arquivos do projeto.
2. Instale as dependências: ```bash
'pip install opencv-python numpy pillow' e 'pip install -r requirements.txt'


## Execução:

- Para capturar rostos: 'python 0_dataset_creator.py'
- Treinar modelo: 'python 1_trainer.py' - Execute pelo menos de 3 a 5 vezes, para garantir de entendimento do sistema com a face do User
- Para rodar a API: 'python api.py'

- **obs: No arquivo 'face_recognizer.py' edite e Adicione novos IDS:
 ID_NOMES = {
    1: "Guilherme Daher",
    2: Memphis Depay (Exemplo)
}

## Atenção!!!
- Quando executar a API, preste atenção na URL que ela retorna, a mesma deve ser substituída no projeto de Android para que haja integração e compatibilidade.
