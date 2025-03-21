import cv2
from ultralytics import YOLO

# Charger le modèle YOLO11
model = YOLO("yolo11s.pt")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erreur: Impossible de capturer l'image")
        break

    # Effectuer la détection d'objets
    results = model(frame)  # Faire une prédiction sur l'image

    # Compter le nombre de personnes détectées
    num_people = 0
    for r in results:
        for box in r.boxes:
            if r.names[int(box.cls)] == "person":  # Vérifier si l'objet détecté est une personne
                num_people += 1

    # Annoter l'image avec les détections
    annotated_frame = results[0].plot()

    # Afficher le nombre de personnes détectées
    cv2.putText(annotated_frame, f"Personnes: {num_people}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Afficher l'image
    cv2.imshow("YOLO11 - Comptage de personnes", annotated_frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
