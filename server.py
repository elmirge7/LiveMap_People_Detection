import threading
import time
from ultralytics import YOLO
import cv2
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask import make_response

app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Charger le modèle YOLO
model = YOLO("yolo11s.pt")

# Définir les flux vidéo avec leurs coordonnées GPS
videos = [
    {"path": "foule1.mp4", "gps": (47.639190, 6.863430)},
    {"path": "foule2.mp4", "gps": (47.638597, 6.860930)},  
    {"path": "foule3.mp4", "gps": (47.638051, 6.863580)},  
]

# Stocker les données d'affluence
affluence_data = {video["gps"]: 0 for video in videos}

# Fonction pour traiter une vidéo et mettre à jour les données
def process_video(video):
    cap = cv2.VideoCapture(video["path"])
    total_people = 0
    frame_count = 0

    for _ in range(1):  # On analyse 5 frames
        ret, frame = cap.read()
        if not ret:
            break  

        # YOLO detection
        results = model(frame, conf=0.1, iou=0.1)
        people_count = sum(1 for r in results for box in r.boxes if int(box.cls) == 0)
        total_people += people_count
        frame_count += 1

    cap.release()

    # Calcul du nombre moyen de personnes
    avg_people = total_people // max(frame_count, 1)

    # Mise à jour des données d'affluence
    affluence_data[video["gps"]] = avg_people
    print(f"📊 Mise à jour pour {video['gps']}: {avg_people} personnes détectées")

# Fonction de mise à jour de l'affluence avec des threads
def update_affluence():
    while True:
        print("🔄 Mise à jour en cours...")
        threads = []

        for video in videos:
            # Démarrer un thread pour chaque vidéo
            thread = threading.Thread(target=process_video, args=(video,))
            threads.append(thread)
            thread.start()

        # Attendre que tous les threads soient terminés
        for thread in threads:
            thread.join()

        print("📊 Données mises à jour :", affluence_data)
        time.sleep(3)  # Attendre 3 secondes avant la mise à jour suivante

# Démarrer la mise à jour en arrière-plan
threading.Thread(target=update_affluence, daemon=True).start()

# Route pour afficher la carte
@app.route("/")
def index():
    return render_template("index.html")

# Route API pour envoyer les données d'affluence
@app.route("/data")
def data():
    response = make_response(jsonify([{"lat": gps[0], "lon": gps[1], "count": count} for gps, count in affluence_data.items()]))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response

if __name__ == "__main__":
    print("🚀 Serveur Flask démarré !")
    app.run(debug=True, port=5000)
