# C:\...\Sprint3--IOT\code\Sprint3--IOT\api.py

from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
# --- IMPORTANTE: Importa a lógica do arquivo face_recognizer.py ---
from face_recognizer import process_image_for_recognition 

# Inicializa o aplicativo Flask
app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate_face():
    """
    Endpoint consumido pelo App Mobile (React Native) via HTTP POST.
    Recebe o JSON com o campo 'image' (em Base64).
    """
    data = request.json
    if not data or 'image' not in data:
        return jsonify({"authenticated": False, "error": "Nenhuma imagem enviada"}), 400

    # 1. Decodificar a imagem Base64
    try:
        image_data = base64.b64decode(data['image'])
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception:
        return jsonify({"authenticated": False, "error": "Formato de imagem inválido"}), 400

    if img is None:
        return jsonify({"authenticated": False, "error": "Falha ao decodificar a imagem"}), 400

    # 2. CHAMAR A LÓGICA DE RECONHECIMENTO EFICIENTE (O CÉREBRO)
    result = process_image_for_recognition(img)

    # 3. Tomar a Decisão, Registrar a Ação e Responder (INTEGRAÇÃO IOB)
    if result['authenticated']:
        # AÇÃO/FLUXO de Sucesso (Registro de Presença, Login, etc.)
        log_message = f"SUCESSO: {result['user']} autenticado. Confiança: {result['confidence']}"
        print(log_message)

        # Retorna o nome de quem foi reconhecido para o App Mobile
        return jsonify({
            "authenticated": True, 
            "user": result['user'],
            "confidence": result['confidence'],
            "message": "Login Autorizado"
        })
    else:
        # AÇÃO/FLUXO de Falha (Alerta de Tentativa, Login Negado)
        log_message = f"FALHA: Rosto {result['user']} detectado, mas autenticação negada. Confiança: {result['confidence']}"
        print(log_message)

        return jsonify({
            "authenticated": False, 
            "user": result['user'],
            "confidence": result['confidence'],
            "error": "Acesso Negado ou Face Não Cadastrada."
        })

# Inicia o servidor da API
if __name__ == '__main__':
    print("=======================================================")
    print("SERVIDOR DE AUTENTICAÇÃO FACIAL (IOB) INICIADO.")
    print("ACESSO EXTERNO: http://[SEU IP REAL]:5000/authenticate")
    print("=======================================================")
    # host='0.0.0.0' permite que o seu celular acesse o servidor na mesma rede.
    app.run(host='0.0.0.0', port=5000, debug=True)
 