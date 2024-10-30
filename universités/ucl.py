import streamlit as st 
import pandas as pd
from utils import insert_commentaire, get_df_comments

def ucl():
    st.session_state.london = True
    if st.button('Retour'):
        st.session_state.pop('london')
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.markdown(
            '<h1 style="color: #5DADE2; text-align: center;">Université de Londres (UCL)</h1>', 
            unsafe_allow_html=True
        )
        st.markdown('<h2><a href="https://www.ucl.ac.uk/" target="_blank" style="text-decoration:none; color:#2E2E2E;">🔗 Site officiel de l\'Université de Londres</a></h2>', unsafe_allow_html=True)
    with col2:
        st.image('static/ucl.jpg', width=500)

    # --- Qualité de l'enseignement ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">🎓 Qualité de l'Enseignement</h2>
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                L’Université de Londres est une institution prestigieuse, connue pour son excellence académique 
                et sa renommée mondiale. Les programmes y sont rigoureux et orientés vers la recherche, offrant aux 
                étudiants une éducation de haute qualité avec des enseignants de renommée internationale. UCL est classée 
                parmi les meilleures universités du monde, ce qui en fait un choix de premier ordre pour ceux qui cherchent 
                à élargir leurs connaissances et compétences dans un environnement académique d’exception.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Localisation et Quartier ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">📍 Localisation et Quartier</h2>
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                Située au cœur de Londres, UCL est idéalement placée dans le quartier de Bloomsbury, connu pour son 
                charme académique et culturel. Ce quartier abrite plusieurs bibliothèques célèbres, musées et parcs 
                qui en font un lieu de vie inspirant pour les étudiants. Cependant, Londres est une ville où le 
                coût de la vie est élevé, particulièrement en termes de logement et d’alimentation, avec un loyer 
                mensuel moyen pour une chambre autour de 1 200 à 1 500 €.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Options de Cours ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">📚 Options de Cours</h2>
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                À UCL, tu as la possibilité de suivre un large éventail de cours, notamment dans des disciplines telles que :
                <ul>
                    <li>Computer Science</li>
                    <li>Économie</li>
                    <li>Droit</li>
                    <li>Gestion</li>
                </ul>
                Ces programmes sont conçus pour offrir aux étudiants une approche multidisciplinaire et développer des 
                compétences pratiques ainsi que théoriques.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Frais de Scolarité ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">💰 Frais de Scolarité</h2>
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                Les frais de scolarité pour les étudiants de l'Université de Londres s’élèvent à environ 3 000 € 
                par semestre. Bien que ces frais soient significatifs, ils incluent l'accès à des ressources pédagogiques 
                de haute qualité, des installations modernes et des opportunités de réseautage avec des experts de l'industrie.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Coût de la Vie et Logement ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">🏠 Coût de la Vie et Logement</h2>
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                Vivre à Londres implique des dépenses conséquentes, notamment pour le logement, la nourriture et le transport. 
                Le loyer moyen pour une chambre à proximité de l'université se situe entre 1 200 et 1 500 € par mois. Pour ceux 
                cherchant une option plus abordable, il est possible de se loger un peu plus loin du campus et d’utiliser le 
                réseau de transport bien développé de Londres. Le coût de la vie peut également varier selon les habitudes 
                personnelles, mais il est recommandé de prévoir un budget pour le quotidien et les sorties culturelles, très 
                fréquentes dans cette ville.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Conclusion ---
    st.markdown(
        """
        <div style="margin-top:20px;">
            <p style="font-size: large; color: #2E2E2E; line-height: 1.6;">
                En résumé, l'Université de Londres (UCL) offre une opportunité unique de vivre une expérience académique 
                enrichissante dans l'une des villes les plus dynamiques au monde. Avec ses programmes diversifiés, sa 
                réputation mondiale, et son emplacement au cœur de Londres, UCL est un choix idéal pour les étudiants 
                motivés par l'excellence académique et culturelle.
            </p>
        </div>
        """, unsafe_allow_html=True
    )


    df = get_df_comments("ucl")
    df = pd.DataFrame(df)
    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">⭐️ Commentaires</h2>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    st.markdown(
        """
        <div style="margin-top:20px;">
            <h2 style="color: #2E2E2E;">✍🏼 Laisser un commentaire</h2>
        </div>
        """, unsafe_allow_html=True
    )
    année = st.number_input("Année d'expat", 2023, 2024, value=2024, step=1)
    commentaire = st.text_input('Votre commentaire', "")
    options = st.text_input('Vos options choisies', "")

    if st.button('Ajouter le commentaire'):
    # Vérifier que les champs ne sont pas vides
        if commentaire and options:
            # Créer un nouveau DataFrame avec le commentaire
            insert_commentaire("ucl", année, commentaire, options)
            # Afficher un message de succès
            st.success('Commentaire ajouté avec succès !')
            st.rerun()
        else:
            st.error("Veuillez remplir tous les champs.")
            st.rerun()






    