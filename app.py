
import streamlit as st
import os
import base64

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Le Journal - AGBANWA ATCHA Affo", 
    page_icon="📰", 
    layout="centered"
)

# --- DESIGN BLANC & STYLE JOURNALISTE ÉLÉGANT (CSS) ---
st.markdown("""
    <style>
    /* Fond blanc pour toute l'application */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Style du bouton de téléchargement */
    .stButton>button {
        background-color: #111111;
        color: white;
        border: 1px solid #111111;
        border-radius: 4px;
        font-weight: bold;
        padding: 10px 20px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #333333;
        border-color: #333333;
        color: white;
    }
    
    /* Pied de page sobre style presse */
    .footer {
        text-align: center;
        padding: 30px 10px;
        font-size: 13px;
        color: #666666;
        border-top: 1px solid #eeeeee;
        margin-top: 60px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* STYLE DU LOGO RETRO / PRESSE */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    .logo-badge {
        width: 100px;
        height: 100px;
        background-color: #111111;
        border: 3px solid #d4af37; /* Ligne dorée élégante */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .logo-text {
        color: #d4af37; /* Texte doré */
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        letter-spacing: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE DE L'APPLICATION ---

# Affichage du logo généré en HTML/CSS (Vos initiales : AA)
st.markdown("""
    <div class="logo-container">
        <div class="logo-badge">
            <span class="logo-text">AA</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- TITRES PRINCIPAUX (FORCÉS EN NOIR POUR LE MODE SOMBRE) ---
st.markdown("<h1 style='text-align: center; color: #111111; font-family: Georgia, serif; font-weight: 700; font-size: 2.5rem; margin-top: 10px;'>Les chroniques du fils du pays Affo</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555555; font-family: Georgia, serif; font-style: italic; font-weight: normal;'>Journal d'actualités, d'analyses et d'informations</h4>", unsafe_allow_html=True)

# Ligne fine de séparation de journal
st.markdown("<hr style='border: 0; border-top: 2px solid #111111; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# Message d'accueil
st.markdown("""
<div style='text-align: center; font-family: "Georgia", serif; font-size: 1.1rem; line-height: 1.6; color: #333333;'>
    <strong>Bienvenue dans votre journal.</strong><br>
    Sélectionnez l'une de nos chroniques ou éditions ci-dessous pour la lire directement ou la télécharger en version PDF.
</div>
""", unsafe_allow_html=True)

st.write("") # Espace de respiration

# --- GESTION DES ARTICLES / ÉDITIONS (Fichiers PDF) ---
articles_disponibles = {
    "Chronique 1 : le TGOGO de Kodjo": "cours1.pdf",
    "Chronique 2 : Notre Afrique": "cours2.pdf"
}

# Menu déroulant de sélection d'articles
choix = st.selectbox("👉 Sélectionnez une publication :", list(articles_disponibles.keys()))
fichier_pdf = articles_disponibles[choix]

st.write("") # Espace de respiration

# --- AFFICHAGE ET TÉLÉCHARGEMENT ---
if os.path.exists(fichier_pdf):
    
    # Lecture du fichier PDF
    with open(fichier_pdf, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger l'article (PDF)",
        data=PDFbyte,
        file_name=fichier_pdf,
        mime='application/pdf'
    )
    
    st.write("---")
    
    # Lecteur PDF intégré
    st.markdown("<h3 style='font-family: Georgia, serif; color: #111111;'>📖 Lecture de l'édition</h3>", unsafe_allow_html=True)
    base64_pdf = base64.b64encode(PDFbyte).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf" style="border: 1px solid #eeeeee; border-radius: 4px;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.warning(f"⚠️ Cette chronique n'est pas encore disponible dans nos archives.")

# --- SECTION : CONTACT & ÉCRITURE ---
st.write("---")
st.markdown("<h3 style='font-family: Georgia, serif; color: #111111; text-align: center;'>📬 Contact & Réaction</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666666; font-style: italic;'>Une question, une suggestion ou une proposition d'article ? Écrivez-nous !</p>", unsafe_allow_html=True)

# Formulaire de contact interactif
with st.form("contact_form", clear_on_submit=True):
    nom = st.text_input("Votre Nom")
    email = st.text_input("Votre adresse Email")
    message = st.text_area("Votre Message / Commentaire")
    
    submit_button = st.form_submit_button(label="📨 Envoyer le message")
    
    if submit_button:
        if nom and email and message:
            st.success(f"Merci {nom} ! Votre message a bien été simulé. (Une fois le site en ligne, nous pourrons le lier à votre boîte mail).")
        else:
            st.error("Veuillez remplir tous les champs avant d'envoyer.")

# --- PIED DE PAGE PERSONNALISÉ ---
st.markdown("""
    <div class="footer">
        Journal numérique conçu par <strong>AGBANWA ATCHA Affo</strong> © 2026<br>
        Tous droits réservés.
    </div>
""", unsafe_allow_html=True)
