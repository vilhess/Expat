import streamlit as st 

def nyu():
    st.session_state.nyu = True
    if st.button('Retour'):
        st.session_state.pop('nyu')
        st.rerun()
    st.title('Université de New York')