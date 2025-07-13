import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
#Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu"
    ["Beranda", "Kalkulator Kimia Dasar", "Soal Hots Kimia Dasar"}
)

# ---Menu BERANDA ---
if menu =="Beranda"
    st.title("Asiknya Meghitung dan Mempermudah dalam Kimia Dasar")
    st.subheader("LPK Kelompok 5 kelas 1B")

