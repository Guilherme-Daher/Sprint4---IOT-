# C:\Users\Guilherme Daher\Desktop\sprint3-IOT\code\Sprint3--IOT\1_trainer.py
import cv2
import numpy as np
import os
from PIL import Image

# --- CONFIGURAÇÃO ---
# ESTA LINHA SÓ FUNCIONARÁ APÓS A INSTALAÇÃO DO opencv-contrib-python!
RECOGNIZER = cv2.face.LBPHFaceRecognizer_create()
FACE_CASCADE = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
PATH = 'dataset'
if not os.path.exists('trainer'):
    os.makedirs('trainer')
 
def get_images_and_labels(path):
    # Encontra todos os arquivos .jpg na pasta dataset
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    face_samples = []
    ids = []
    for image_path in image_paths:
        # Pega a imagem e converte para escala de cinza
        # 'L' garante que a imagem é tratada como preto e branco, essencial para o LBPH
        pil_image = Image.open(image_path).convert('L') 
        img_numpy = np.array(pil_image, 'uint8')
 
        # Extrai o ID do nome do arquivo (espera: ID.N.jpg)
        face_id = int(os.path.split(image_path)[-1].split(".")[0])
        face_samples.append(img_numpy)
        ids.append(face_id)
    return face_samples, ids
 
print("Iniciando treinamento... Aguarde.")
 
faces, ids = get_images_and_labels(PATH)
 
# --- VERIFICAÇÃO DE SEGURANÇA ---
if not faces:
    print("\n[ERRO FATAL] Nenhuma imagem de rosto válida encontrada na pasta 'dataset'.")
    print("O treinamento não pode ser realizado. Verifique se o '0_dataset_creator.py' salvou as imagens corretamente.")
    exit()
 
# O comando de treinamento da IA (se a biblioteca estiver correta, ele funciona aqui)
RECOGNIZER.train(faces, np.array(ids))
 
# Salva o modelo treinado (O arquivo trainer.yml é criado aqui)
RECOGNIZER.write('trainer/trainer.yml')
 
print(f"\n[SUCESSO] Treinamento concluído. {len(np.unique(ids))} usuários treinados.")
print("Modelo salvo em 'trainer/trainer.yml'.")