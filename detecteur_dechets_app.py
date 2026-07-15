import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Configurer la page mobile
st.set_page_config(page_title="Tri de Déchets - IA", page_icon="♻️")
st.title("♻️ Détecteur de Déchets Intelligent")
st.write("Prenez une photo d'un déchet pour l'analyser en temps réel.")

# Charger le modèle d'IA
@st.cache_resource
def charger_modele():
    interpreter = tf.lite.Interpreter(model_path="model_unquant.tflite")
    interpreter.allocate_tensors()
    return interpreter

try:
    interpreter = charger_modele()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    CLASSES = ["Recyclable", "Non-Recyclable", "Organique", "Vide"]

    # Activer l'appareil photo du téléphone
    img_file = st.camera_input("Prendre une photo du déchet")

    if img_file is not None:
        # Ouvrir et afficher l'image
        image = Image.open(img_file)
        
        # Prétraitement pour le modèle d'IA (taille 224x224)
        image_resized = image.resize((224, 224))
        image_array = np.array(image_resized).astype(np.float32) / 255.0
        image_tensor = np.expand_dims(image_array, axis=0)

        # Lancer la prédiction
        interpreter.set_tensor(input_details[0]['index'], image_tensor)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details[0]['index'])[0]

        # Récupérer les résultats
        meilleur_index = np.argmax(predictions)
        classe_detectee = CLASSES[meilleur_index]
        score_confiance = predictions[meilleur_index]

        # Affichage du verdict
        if score_confiance > 0.70 and classe_detectee != "Vide":
            st.success(f"Résultat : **{classe_detectee}** ({score_confiance*100:.1f}%)")
        else:
            st.warning("⚠️ Aucun déchet clairement identifié. Réessayez !")

except Exception as e:
    st.error(f"Erreur lors de l'analyse : {e}")
