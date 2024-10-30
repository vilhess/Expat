import streamlit as st

def england_page():
    # --- Title Section ---
    st.markdown(
        """
        <div style="border: 2px solid #0044cc; padding: 10px; border-radius: 5px; background-color: #e6f2ff; text-align: center;">
            <h3 style="color: #0044cc; font-weight: bold;">Séjour en Angleterre 🇬🇧</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Partner Universities Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">🏫 Universités Partenaires :</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Display university with an "🔍" button to save name to session state
    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.write("Université de Londres")
    with col2:
        if st.button("🔍", key="london"):
            pass

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.write("Université d'Oxford")
    with col2:
        if st.button("🔍", key="oxford"):
            pass

    # --- Required Documents Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📄 Documents Nécessaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                L'Angleterre ne faisant plus partie de l'Union Européenne 🇪🇺, il te faudra préparer plusieurs documents importants :
            </p>
            <ul style="font-size: large; line-height: 1.6; color: #2E2E2E;">
                <li>Passeport</li>
                <li>Certificat de scolarité (à demander au secrétariat)</li>
                <li>(Compléter plus tard)</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Currency and Bank Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💳 Monnaie et Dépenses :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                La monnaie en Angleterre est la livre sterling (GBP) et non l'EURO. Pour faciliter tes dépenses, veille à disposer d'une 
                carte bancaire compatible (consulte ta banque pour plus d’informations).
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Communication Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📞 Communication :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Pour rester en contact avec ta famille et tes amis sans frais excessifs, assure-toi d'avoir un forfait mobile valable à 
                l'étranger. Informe-toi auprès de ton opérateur pour éviter les frais supplémentaires.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Cost of Living Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💰 Coût de la Vie :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le coût de la vie en Angleterre est légèrement plus élevé qu'en France. Pour ton logement, il est conseillé de 
                (Compléter plus tard).
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Additional Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">ℹ️ Informations Supplémentaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                En cliquant sur les noms des universités partenaires ci-dessus, tu pourras accéder à des informations plus détaillées 
                sur chaque université, y compris les frais de scolarité, les bons plans et autres informations utiles pour ton séjour.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )


import streamlit as st

def usa_page():
    # --- Title Section ---
    st.markdown(
        """
        <div style="border: 2px solid #0044cc; padding: 10px; border-radius: 5px; background-color: #e6f2ff; text-align: center;">
            <h3 style="color: #0044cc; font-weight: bold;">Séjour aux États-Unis 🇺🇸</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Partner Universities Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">🏫 Universités Partenaires :</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Université d'Harvard avec le bouton d'ajout
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write("Université d'Harvard")
    with col2:
        if st.button("🔍", key="harvard"):
            pass

    # Université de New York (NYU) avec le bouton d'ajout
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write("Université de New York (NYU)")
    with col2:
        if st.button("🔍", key="nyu"):
            pass

    # --- Required Documents Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📄 Documents Nécessaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Pour les États-Unis, des formalités administratives strictes sont nécessaires. Assure-toi de disposer des documents suivants :
            </p>
            <ul style="font-size: large; line-height: 1.6; color: #2E2E2E;">
                <li>Passeport valide</li>
                <li>Visa étudiant (type F-1 ou J-1 selon ton programme)</li>
                <li>Certificat de scolarité (à demander au secrétariat)</li>
                <li>Preuve de ressources financières (peut être exigée pour le visa)</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Currency and Bank Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💳 Monnaie et Dépenses :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                La monnaie aux États-Unis est le dollar américain (USD). Il est recommandé de disposer d'une carte bancaire internationale 
                pour éviter les frais de conversion. N'hésite pas à consulter ta banque pour obtenir une carte adaptée aux paiements à 
                l’étranger.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Communication Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📞 Communication :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Les frais de communication peuvent être élevés aux États-Unis. Renseigne-toi auprès de ton opérateur pour savoir s'il propose 
                un forfait international adapté, ou envisage l'achat d'une carte SIM locale à ton arrivée pour rester en contact sans frais 
                excessifs.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Cost of Living Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💰 Coût de la Vie :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le coût de la vie aux États-Unis peut varier selon la ville. New York et Boston, par exemple, sont plus onéreuses que la moyenne. 
                Pour le logement, explore les options de résidences universitaires ou de colocation. Les frais moyens pour les étudiants peuvent 
                être élevés, alors planifie ton budget en conséquence.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Additional Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">ℹ️ Informations Supplémentaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                En cliquant sur les universités partenaires ci-dessus, tu pourras obtenir des informations détaillées, y compris les frais de scolarité, 
                les bons plans pour économiser, ainsi que des conseils pour t'intégrer facilement dans le cadre universitaire américain.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

def canada_page():
    # --- Title Section ---
    st.markdown(
        """
        <div style="border: 2px solid #0044cc; padding: 10px; border-radius: 5px; background-color: #e6f2ff; text-align: center;">
            <h3 style="color: #0044cc; font-weight: bold;">Séjour au Canada 🇨🇦</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Partner Universities Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">🏫 Université Partenaire :</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Université de Montréal avec le bouton d'ajout
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write("Université de Montréal")
    with col2:
        if st.button("🔍", key="montreal"):
            pass

    # --- Required Documents Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📄 Documents Nécessaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Pour étudier au Canada, tu auras besoin de préparer certains documents essentiels :
            </p>
            <ul style="font-size: large; line-height: 1.6; color: #2E2E2E;">
                <li>Passeport valide</li>
                <li>Permis d’études (obligatoire pour les séjours de plus de 6 mois)</li>
                <li>Certificat d'acceptation du Québec (CAQ) si tu étudies au Québec</li>
                <li>Certificat de scolarité (à demander au secrétariat)</li>
                <li>Preuve de ressources financières (exigée pour le permis d’études)</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Currency and Bank Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💳 Monnaie et Dépenses :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                La monnaie au Canada est le dollar canadien (CAD). Vérifie auprès de ta banque que ta carte est compatible avec les 
                transactions internationales, ou envisage d’ouvrir un compte local si tu comptes y séjourner longtemps.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Communication Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📞 Communication :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Pour éviter des frais de communication élevés, renseigne-toi auprès de ton opérateur sur les options internationales, 
                ou envisage l'achat d'une carte SIM canadienne dès ton arrivée. De nombreux forfaits prépayés offrent des données 
                mobiles à prix raisonnable.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Cost of Living Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💰 Coût de la Vie :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le coût de la vie au Canada varie selon les régions. Montréal, bien que plus abordable que d'autres grandes villes nord-américaines, 
                peut être plus coûteuse que certaines villes françaises. Pour le logement, explore les options de résidences universitaires ou 
                de colocation. Planifie ton budget pour couvrir le logement, les frais de scolarité et les dépenses courantes.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Additional Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">ℹ️ Informations Supplémentaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                En cliquant sur l'Université de Montréal, tu accèderas à des informations supplémentaires concernant les frais de scolarité, 
                les bons plans pour économiser et des conseils pratiques pour réussir ton intégration dans la culture québécoise.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

import streamlit as st

def mex_page():
    # --- Title Section ---
    st.markdown(
        """
        <div style="border: 2px solid #0044cc; padding: 10px; border-radius: 5px; background-color: #e6f2ff; text-align: center;">
            <h3 style="color: #0044cc; font-weight: bold;">Séjour au Mexique 🇲🇽</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Partner Universities Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">🏫 Université Partenaire :</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Université Autonome de Mexico (UNAM) avec le bouton d'ajout
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write("Université Autonome de Mexico (UNAM)")
    with col2:
        if st.button("🔍", key="unam"):
            pass

    # --- Required Documents Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📄 Documents Nécessaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Avant ton départ pour le Mexique, assure-toi d'avoir les documents suivants :
            </p>
            <ul style="font-size: large; line-height: 1.6; color: #2E2E2E;">
                <li>Passeport valide</li>
                <li>Visa étudiant (si le séjour dépasse 180 jours)</li>
                <li>Certificat de scolarité (à obtenir auprès du secrétariat)</li>
                <li>Preuve d’assurance santé internationale (fortement recommandée)</li>
            </ul>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Health and Vaccination Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💉 Santé et Vaccinations :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le Mexique ne nécessite pas de vaccinations spécifiques, mais certaines sont conseillées, comme les vaccins contre l’hépatite A et la typhoïde, 
                pour un séjour en toute sérénité. N’oublie pas de vérifier ta couverture santé pour les consultations médicales à l’étranger.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Currency and Bank Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💳 Monnaie et Dépenses :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                La monnaie au Mexique est le peso mexicain (MXN). Il est recommandé de disposer d'une carte bancaire acceptée à 
                l'international. Renseigne-toi auprès de ta banque pour t’assurer que ta carte fonctionne au Mexique ou pour limiter 
                les frais de transaction.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Safety Tips Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">🔒 Conseils de Sécurité :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le Mexique est un pays accueillant, mais comme dans toute grande ville, il est conseillé de rester vigilant. 
                Privilégie les zones bien fréquentées et garde tes effets personnels près de toi. Reste attentif dans les 
                transports en commun et évite de montrer des objets de valeur. Ces précautions permettent de profiter de 
                ton séjour en toute tranquillité !
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Communication Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">📞 Communication :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Pour rester en contact avec tes proches, renseigne-toi sur les options internationales de ton opérateur. 
                Il est aussi possible d'acheter une carte SIM locale avec des forfaits data à prix abordable dès ton arrivée.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Cost of Living Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">💰 Coût de la Vie :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                Le coût de la vie au Mexique est en général plus bas qu’en France, mais il peut varier selon les régions. 
                Pour ton logement, explore les options de résidences universitaires ou de colocation. N'oublie pas de prévoir 
                un budget pour les déplacements, les repas, et les activités locales.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Additional Information Section ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h4 style="color: #2E2E2E;">ℹ️ Informations Supplémentaires :</h4>
            <p style="text-align: justify; font-size: large; color: #2E2E2E;">
                En cliquant sur l'Université Autonome de Mexico (UNAM) ci-dessus, tu trouveras des détails supplémentaires 
                sur le campus, les frais de scolarité, les bons plans pour t'intégrer, et des informations pour découvrir la 
                culture mexicaine.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )