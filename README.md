# ♻️ Détecteur de Déchets Intelligent — Tri par IA

Une application web d'intelligence artificielle conçue pour classifier instantanément les déchets ménagers à partir d'une simple photo. 

Projet développé dans le cadre de **IndabaX Congo 2026**.

---

## 🌍 Contexte & Vision du Projet

Dans plusieurs villes du Congo (notamment à **Brazzaville** et à **Pointe-Noire**), ainsi que dans de nombreux pays d'Afrique subsaharienne, la gestion et le tri des déchets restent des défis majeurs. L'absence de technologies accessibles pour sensibiliser et assister les citoyens au tri à la source freine le développement du recyclage.

Ce projet a été pensé comme une **solution technologique locale et accessible**, avec l'ambition de :
1. **Faciliter le tri quotidien** en permettant à chacun de savoir instantanément dans quelle catégorie jeter un déchet (*Recyclable*, *Non-Recyclable* ou *Organique*).
2. **Promouvoir l'assainissement urbain** en s'inspirant des modèles réussis sur le continent (comme au Rwanda ou au Sénégal).
3. **Servir de brique logicielle (IA)** destinable à être intégrée plus tard dans des systèmes automatisés, comme des robots ou bacs de collecte intelligents.

---

## 🛠️ Stack Technique

* **Framework Web :** Streamlit
* **Modèle d'IA :** MobileNetV2 (Transfer Learning)
* **Format du Modèle :** TensorFlow Lite (`.tflite`)
* **Langage & Bibliothèques :** Python, NumPy, Pillow, `tflite-runtime`
* **Données d'entraînement :** Dataset d'images classées (Kaggle / TFLite)

---

## 🚀 Fonctionnement de l'Application

1. L'utilisateur ouvre l'application web depuis son téléphone ou son ordinateur.
2. Il prend une photo du déchet via la caméra.
3. L'image est prétraitée (redimensionnée en 224x224 pixels) et analysée en temps réel par le modèle `.tflite`.
4. L'IA affiche la catégorie détectée avec un indice de confiance :
   * ♻️ **Recyclable** (ex: bouteilles plastiques, cartons, canettes)
   * 🗑️ **Non-Recyclable** (ex: plastiques à usage unique souillés)
   * 🍎 **Organique** (ex: restes de nourriture, épluchures)

---

## 👥 Équipe & Remerciements

Projet conçu avec passion pour apporter des solutions concrètes basées sur l'intelligence artificielle au service de nos communautés. 

Merci à l'équipe d'**IndabaX Congo** pour la promotion de l'IA sur le continent !
