import streamlit as st 

def oxford():
    st.session_state.oxford = True
    if st.button('Retour'):
        st.session_state.pop('oxford')
        st.rerun()
    st.title("Université d'Oxford")