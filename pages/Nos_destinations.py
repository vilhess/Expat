import streamlit as st
import pandas as pd
from info_pays import england_page, canada_page, usa_page, mex_page

from universités.harvard import harvard
from universités.mexico import mexico
from universités.montreal import montreal
from universités.nyu import nyu
from universités.oxford import oxford
from universités.ucl import ucl

st.set_page_config(layout="wide")


df = pd.read_csv('countries.csv')


if 'london' in st.session_state and st.session_state["london"]:
    ucl()
elif 'oxford' in st.session_state and st.session_state["oxford"]:
    oxford()
elif 'unam' in st.session_state and st.session_state["unam"]:
    mexico()
elif 'harvard' in st.session_state and st.session_state["harvard"]:
    harvard()
elif 'nyu' in st.session_state and st.session_state["nyu"]:
    nyu()
elif 'montreal' in st.session_state and st.session_state["montreal"]:
    montreal()


else:

    # --- Header Section ---
    st.markdown(
        """
        <div style="border: 2px solid #FF0000; padding: 10px; border-radius: 5px; background-color: #FFE6E6; text-align: center;">
            <h2 style="color: #FF0000; font-weight: bold;">Les Pays d'accueil que nous proposons 🌍</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- Introductory Section ---
    st.markdown(
        """
        <div style="margin-top:20px; text-align: center;">
            <h4 style="color: #2E2E2E;">
                Tu pourras ici découvrir les écoles que nous te proposons pays par pays :
            </h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.map(df, size=5000)

    # --- Country Selection Section ---
    st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break for spacing

    col1, col2, col3, col4 = st.columns(4)

    # Buttons with icons for each country
    with col1:
        uk = st.button("🇬🇧 Angleterre", help="Découvre les écoles en Angleterre")
    with col2:
        can = st.button("🇨🇦 Canada", help="Découvre les écoles au Canada")
    with col3:
        usa = st.button("🇺🇸 États-Unis", help="Découvre les écoles aux États-Unis")
    with col4:
        mex = st.button("🇲🇽 Mexique", help="Découvre les écoles au Mexique")

    # --- Page Navigation Logic ---
    if uk:
        england_page()
    if can:
        canada_page()
    if usa:
        usa_page()
    if mex:
        mex_page()