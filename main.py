import cv2

# Carrega o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Verifica se o XML foi carregado corretamente
if face_cascade.empty():
    print("Erro ao carregar o Haar Cascade XML.")
    exit()

# Lê o vídeo gravado (substitua pelo nome do seu arquivo)
cap = cv2.VideoCapture('VIdeoSprint3.mp4')

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Função dummy para trackbars
def nothing(x):
    pass

# Cria janela e sliders para ajustar parâmetros
cv2.namedWindow('Detector de Rosto')
cv2.createTrackbar('Scale (%)', 'Detector de Rosto', 110, 200, nothing)       # scaleFactor (110 = 1.1)
cv2.createTrackbar('Min Neighbors', 'Detector de Rosto', 5, 20, nothing)      # minNeighbors
cv2.createTrackbar('Min Size', 'Detector de Rosto', 30, 200, nothing)         # minSize

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lê os valores dos sliders
    scale_percent = cv2.getTrackbarPos('Scale (%)', 'Detector de Rosto')
    min_neighbors = cv2.getTrackbarPos('Min Neighbors', 'Detector de Rosto')
    min_size = cv2.getTrackbarPos('Min Size', 'Detector de Rosto')

    # Converte o valor de scale_percent para scaleFactor
    scale_factor = scale_percent / 100.0

    # Detecta rostos
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(min_size, min_size)
    )

    # Desenha retângulos e texto
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Rosto detectado", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Exibe número de rostos detectados e parâmetros
    cv2.putText(frame, f"Rostos: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(frame, f"ScaleFactor: {scale_factor:.2f}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(frame, f"MinNeighbors: {min_neighbors}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(frame, f"MinSize: {min_size}", (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow('Detector de Rosto', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()