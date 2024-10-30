import streamlit as st 

def mexico():
    st.session_state.mexico = True
    if st.button('Retour'):
        st.session_state.pop('mexico')
        st.rerun()
    st.title("Université de Mexico")