import streamlit as st

#Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda","Kalkulator Kimia Dasar","Soal Hots Kimia Dasar"]
)

# ---Menu BERANDA ---
if menu =="Beranda":
    st.title("Asiknya Meghitung dan Mempermudah dalam Kimia Dasar")
    st.subheader("LPK Kelompok 5 kelas 1B")
    st.image("https://photos.app.goo.gl/bYz51d4fvKGc1SLE6.png",width=400)

