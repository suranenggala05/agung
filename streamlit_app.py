import streamlit as st

#Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda","Kalkulator Kimia Dasar","Soal Hots Kimia Dasar","Catatan"]
)

# ---Menu BERANDA ---
if menu =="Beranda":
    st.title("Asiknya Meghitung dan Mempermudah dalam Kimia Dasar")
    st.subheader("LPK Kelompok 5 kelas 1B")
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geografi.org%2F2023%2F07%2Ftabel-periodik-unsur-kimia-dan.html&psig=AOvVaw1vSoW_TsTitTdP-ch0dyyH&ust=1752481246051000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjo1M2zuY4DFQAAAAAdAAAAABAE",width=400)

