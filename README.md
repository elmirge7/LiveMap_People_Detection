# LiveMap_People_Detection
Projet réalisé lors du CrunchTime 2025 organisé par l'UTBM.
L'idée était d'attribuer une zone sur un carte à une caméra et de compter le nombre de personnes dans cette zone.

# 📡 YOLO Affluence Tracker

Ce projet utilise **YOLO** pour détecter en temps réel le nombre de personnes dans une vidéo ou un flux de caméra. Il offre plusieurs fonctionnalités :
- **Analyse en direct avec une caméra** (`camera.py`)
- **Comparaison du nombre de personnes entre deux vidéos** (`compvideo.py`)
- **Affichage en direct des données sur une carte interactive** (`server.py` avec `index.html`)

---

## 🚀 Installation

### 1️⃣ Prérequis
Assurez-vous d'avoir installé :
- **Python 3.8+**
- **pip** (gestionnaire de paquets Python)

### 2️⃣ Cloner le projet
```sh
git clone https://github.com/ton-repo/yolo-affluence-tracker.git
cd yolo-affluence-tracker```

### 3️⃣ Installer les dépendances
```sh
pip install -r requirements.txt
```

### 4️⃣ Télécharger le modèle YOLO
```sh
wget https://github.com/ultralytics/assets/releases/download/v8/yolov8n.pt -O yolo.pt
```
Ou placez un modèle YOLO (`.pt`) dans le dossier du projet. #la version n est disponible dans le projet

---

## 🎥 Utilisation

### 🔴 1️⃣ Lancer l'analyse avec la caméra (`camera.py`)

Ce script active la webcam et affiche en direct le nombre de personnes détectées.

```sh
python camera.py
```
### 🎞️ 2️⃣ Comparer le nombre de personnes entre deux vidéos (`compvideo.py`)

Ce script compare le nombre de personnes détectées dans deux vidéos différentes.

```sh
python compvideo.py
```

### 🗺️ 3️⃣ Visualiser les données sur une carte interactive (`server.py`)

Ce script lance un **serveur Flask** qui met à jour une carte en direct en fonction du nombre de personnes détectées.

```sh
python server.py
```

`python server.py`

Ensuite, ouvrez un navigateur et accédez à :  
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📁 Structure du projet

```
📂 yolo-affluence-tracker  
├── 📄 camera.py           # Détection en direct via webcam  
├── 📄 compvideo.py        # Comparaison de l'affluence entre deux vidéos  
├── 📄 server.py           # Serveur Flask + carte interactive  
├── 📂 templates  
│   ├── 📄 index.html      # Page web pour afficher la carte  
├── 📄 requirements.txt    # Liste des dépendances Python  
├── 📄 README.md           # Documentation du projet
```

---

## 🛠️ Dépendances

Ce projet utilise :

- **Flask** (serveur web)
- **Flask-CORS** (gestion des requêtes CORS)
- **OpenCV** (traitement des images)
- **Ultralytics YOLO** (modèle d'IA pour la détection)
- **Threading** (exécution parallèle)

Installez toutes les dépendances avec :

```
pip install -r requirements.txt
```


---

## 💡 Améliorations possibles

🔹 Intégration avec une base de données pour stocker l'affluence  
