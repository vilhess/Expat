import streamlit as st 

def montreal():
    st.session_state.montreal = True
    if st.button('Retour'):
        st.session_state.pop('montreal')
        st.rerun()
    st.title('Université de Montreal')