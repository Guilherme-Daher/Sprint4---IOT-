import cv2
import os
 
# --- CONFIGURAÇÃO ---
FACE_CASCADE = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
if FACE_CASCADE.empty():
    print("ERRO FATAL: Arquivo haarcascade_frontalface_default.xml não encontrado.")
    exit()
 
NOME_PESSOA = input("Digite o nome da pessoa a ser cadastrada: ").strip().replace(" ", "_")
 
if not os.path.exists('dataset'):
    os.makedirs('dataset')
 
ids_existentes = [
    int(f.split('.')[0]) for f in os.listdir('dataset') if f.endswith('.jpg') and f.split('.')[0].isdigit()
]
FACE_ID = max(ids_existentes, default=0) + 1
 
AMOSTRAS_NECESSARIAS = 30
 
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("\nERRO: Não foi possível abrir a webcam.")
    exit()
 
existing_images = [
    f for f in os.listdir('dataset')
    if f.startswith(f"{FACE_ID}.") and f.endswith('.jpg')
]
count = len(existing_images)
 
print(f"\nPreparando para coletar amostras para o ID: {FACE_ID} ({NOME_PESSOA})...")
print("Câmera ativada. Olhe para a câmera. Pressione 'q' para sair.")
 
cv2.namedWindow('Capturando Faces - Webcam', cv2.WINDOW_NORMAL)
 
while count < AMOSTRAS_NECESSARIAS + len(existing_images):
    ret, img = cap.read()
    if not ret:
        print("\nAVISO: Stream de vídeo perdido.")
        break
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_crop = gray[y:y + h, x:x + w]
        nome_arquivo = f'dataset/{FACE_ID}.{count}.jpg'
        cv2.imwrite(nome_arquivo, face_crop)
        count += 1
        cv2.putText(img, f"Capturando: {count}/{AMOSTRAS_NECESSARIAS + len(existing_images)}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
 
    cv2.imshow('Capturando Faces - Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
print(f"\nColeta de dados finalizada para {NOME_PESSOA}. Total de amostras salvas: {count}")
cap.release()
cv2.destroyAllWindows()
