import streamlit as st
import pandas as pd
import os

# === PAGE CONFIGURATION ===
st.set_page_config(page_title="Suivi Joueuse RMBB", layout="centered")

# === STYLE MODERNE ===
st.markdown("""
<style>
body, .stApp {
    background-color: #e0e0e0;
    color: black;
    font-family: 'Segoe UI', sans-serif;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

h1 {
    text-align: center;
    color: #003366;
    font-weight: 700;
    margin-bottom: 10px;
}

h4 {
    color: #003366;
    margin-bottom: 10px;
    border-left: 5px solid #0055a5;
    padding-left: 8px;
}

.stButton>button {
    background-color: #003366;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    width: 100%;
    transition: all 0.2s ease-in-out;
}

.stButton>button:hover {
    background-color: #0055a5;
    transform: scale(1.02);
}

.success-msg {
    text-align: center;
    font-weight: bold;
    color: #003366;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# === TITRE ===
st.title("Suivi de la Charge - RMBB 🏀")

# === NOM Joueuse ===
joueuse = st.text_input("👤 Nom et prénom de la joueuse")

# === ÉTAT DU JOUR ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>🧠 État du jour</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    etat_mental = st.slider("Mental", 0, 10, 5)
with col2:
    etat_physique = st.slider("Physique", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# === ÉVALUATION ENTRAÎNEMENT ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>💪 Évaluation de l’entraînement</h4>", unsafe_allow_html=True)
entrainement = st.slider("Échelle de Borg (0 = très facile, 10 = effort maximal)", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# === COMMENTAIRE ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>📝 Commentaire libre</h4>", unsafe_allow_html=True)
commentaire = st.text_area("Comment t’es-tu sentie aujourd’hui ?", "")
st.markdown('</div>', unsafe_allow_html=True)

# === ENREGISTREMENT ===
if st.button("💾 Enregistrer mes données"):
    if not joueuse:
        st.error("⚠️ Merci d’entrer ton nom avant d’enregistrer.")
    else:
        file_path = "suivi_joueuse.csv"
        df_new = pd.DataFrame({
            "Joueuse": [joueuse],
            "Etat_Mental": [etat_mental],
            "Etat_Physique": [etat_physique],
            "Evaluation_Entrainement": [entrainement],
            "Commentaire": [commentaire]
        })

        if os.path.exists(file_path):
            df_new.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df_new.to_csv(file_path, index=False)

        st.success("✅ Données enregistrées avec succès !")
        st.markdown("<div class='success-msg'>Merci pour ta participation 💙</div>", unsafe_allow_html=True)
