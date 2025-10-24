import cv2
import numpy as np
import os
 
# --- CONFIGURAÇÃO LBPH (Trainer e Nomes) ---
RECOGNIZER = cv2.face.LBPHFaceRecognizer_create()
try:
    RECOGNIZER.read('trainer/trainer.yml')
except cv2.error:
    print("ALERTA: Arquivo 'trainer/trainer.yml' não encontrado. Rodando em modo DETECÇÃO.")
    RECOGNIZER = None  # Desativa o reconhecimento se não houver modelo
 
FACE_CASCADE = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
THRESHOLD = 80  # Quanto menor a distância, maior a confiança
 
# Mapeamento de IDs para nomes
ID_NOMES = {
    1: "Guilherme Daher",
    2: "Memphis Depay",
    # Adicione mais IDs conforme necessário
}
 
def process_image_for_recognition(img):
    """
    Executa a detecção e o reconhecimento facial.
    Retorna nome, confiança e status de autenticação.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )
 
    if len(faces) == 0:
        return {
            "authenticated": False,
            "user": "Nenhuma Face Detectada",
            "confidence": None
        }
 
    # Seleciona a maior face detectada
    (x, y, w, h) = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]
 
    if RECOGNIZER is None:
        return {
            "authenticated": True,
            "user": "Rosto Detectado (Sem ID)",
            "confidence": 100
        }
 
    face_roi = gray[y:y + h, x:x + w]
    id_predict, confidence = RECOGNIZER.predict(face_roi)
 
    print(f"[DEBUG] ID reconhecido: {id_predict}, Confiança: {confidence}")
 
    if confidence < THRESHOLD:
        user_name = ID_NOMES.get(id_predict, "Desconhecido")
        return {
            "authenticated": True,
            "user": user_name,
            "confidence": round(confidence, 2)
        }
    else:
        return {
            "authenticated": False,
            "user": "Face não reconhecida",
            "confidence": round(confidence, 2)
        }