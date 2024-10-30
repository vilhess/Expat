import streamlit as st
st.set_page_config(layout="wide")

# --- Header Section ---
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.markdown(
        """
        <div style="border: 2px solid #FF0000; padding: 10px; border-radius: 5px; background-color: #FFE6E6; text-align: center;">
            <h2 style="color: #FF0000; font-weight: bold;">Préparer Mon Expat</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )
with col2:
    st.image('static/em.jpg', width=100)  # Ajustement de la taille de l'image

# --- Introductory Section ---
st.markdown(
    """
    <div style="margin-top:20px;">
        <h3 style="text-align: justify; color: #2E2E2E;">
            🎓 <b>Bienvenue !</b> Tu es étudiant de l'EM Normandie, prêt à relever le défi d'une
            expatriation pour valider ton bachelor. Pendant 6 mois, tu étudieras dans l'une de nos 
            <u>écoles partenaires</u> à l'étranger. Cette expérience te permettra de sortir de ta 
            zone de confort, de découvrir de nouvelles cultures et de t’épanouir dans un cadre inédit.
        </h3>
    </div>
    """, 
    unsafe_allow_html=True
)

# --- Information Section ---
st.markdown(
    """
    <div style="margin-top:30px;">
        <h4>🌍 <b>Sur cette plateforme, tu trouveras :</b></h4>
        <ul style="font-size: large; line-height: 1.8; color: #2E2E2E;">
            <li>Les <u>informations détaillées</u> sur chaque destination pour t’aider à choisir celle qui te correspond le mieux.</li>
            <li>Les <u>documents importants</u> à obtenir (passeport, visa, assurances) spécifiques à chaque pays.</li>
            <li>Les <u>vaccinations nécessaires</u> pour certaines destinations, pour un séjour en toute sécurité.</li>
            <li>Des <u>conseils pratiques</u> et des astuces pour vivre sereinement ton expatriation.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Document Storage Section ---
st.markdown(
    """
    <div style="margin-top:20px;">
        <h4>💼 <b>Utilisation de la plateforme pendant ton séjour :</b></h4>
        <p style="text-align: justify; font-size: large; color: #2E2E2E;">
            Cette plateforme te permet également de stocker tous tes documents au format numérique. Ainsi, tu pourras 
            les retrouver en quelques clics, à condition d'avoir une connexion internet. Une solution idéale pour voyager léger !
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Community & Support Section ---
st.markdown(
    """
    <div style="margin-top:20px;">
        <h4>👥 <b>Support et communauté :</b></h4>
        <p style="text-align: justify; font-size: large; color: #2E2E2E;">
            Cette plateforme est maintenue par des anciens étudiants ayant déjà réalisé leur expat, désireux de partager leur 
            expérience pour te guider et te rassurer avant ton départ. N’hésite pas à poser tes questions et à partager tes propres 
            découvertes !
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Footer Section ---
st.markdown(
    """
    <hr style="border:0.5px solid #D3D3D3;">
    <p style="text-align: center; color: #2E2E2E;">
        Bon voyage et profite de cette aventure unique ! 🌏
    </p>
    """,
    unsafe_allow_html=True
)