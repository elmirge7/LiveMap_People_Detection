import cv2
from ultralytics import YOLO

# Charger le modèle YOLO
model = YOLO("yolo11s.pt")  

# Définir les chemins des vidéos
video_path1 = "foule1.mp4"
video_path2 = "foule2.mp4"
# video_path3 = "foule3.mp4"

# Ouvrir les vidéos
cap1 = cv2.VideoCapture(video_path1)
cap2 = cv2.VideoCapture(video_path2)
# cap3 = cv2.VideoCapture(video_path3)

# Obtenir les propriétés des vidéos (assumer même résolution)
fps = int(cap1.get(cv2.CAP_PROP_FPS))
width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Définir les fichiers de sortie (optionnel)
output_path1 = "output1.mp4"
output_path2 = "output2.mp4"
# output_path3 = "output3.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out1 = cv2.VideoWriter(output_path1, fourcc, fps, (width, height))
out2 = cv2.VideoWriter(output_path2, fourcc, fps, (width, height))
# out3 = cv2.VideoWriter(output_path3, fourcc, fps, (width, height))

while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    # ret3, frame3 = cap3.read()

    if not ret1 or not ret2:
        break  # Fin d'une des vidéos

    # Détection sur les deux vidéos
    results1 = model(frame1, conf=0.1, iou=0.1)
    results2 = model(frame2, conf=0.1, iou=0.1)
    # results3 = model(frame3, conf=0.1, iou=0.1)

    # Compter les personnes détectées
    count1 = sum(1 for r in results1 for box in r.boxes if int(box.cls) == 0)
    count2 = sum(1 for r in results2 for box in r.boxes if int(box.cls) == 0)
    # count3 = sum(1 for r in results3 for box in r.boxes if int(box.cls) == 0)

    # Annoter les vidéos
    frame1_annotated = results1[0].plot()
    frame2_annotated = results2[0].plot()
    # frame3_annotated = results3[0].plot()

    # Ajouter les textes avec les nombres de personnes détectées
    cv2.putText(frame1_annotated, f"Personnes: {count1}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame2_annotated, f"Personnes: {count2}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #cv2.putText(frame3_annotated, f"Personnes: {count3}", (50, 50), 
    #            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Sauvegarder les vidéos annotées
    out1.write(frame1_annotated)
    out2.write(frame2_annotated)
    # out3.write(frame3_annotated)

    # 🔥 Redimensionner les frames pour éviter l'erreur de concaténation
    frame1_annotated = cv2.resize(frame1_annotated, (640, 360))
    frame2_annotated = cv2.resize(frame2_annotated, (640, 360))
    # frame3_annotated = cv2.resize(frame3_annotated, (640, 360))

    # 🔄 Concaténer horizontalement et afficher
    combined_frame = cv2.hconcat([frame1_annotated, frame2_annotated])
    cv2.imshow("YOLO11 - Deux vidéos en même temps", combined_frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libérer les ressources
cap1.release()
cap2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
