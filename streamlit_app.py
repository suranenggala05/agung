import streamlit as st

#Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda","Kalkulator Kimia Dasar","Soal Hots Kimia Dasar","Catatan"]
)

# ---Menu BERANDA ---
if menu =="Beranda":
    st.title("Kalkulator Kimia Dasar+")
    st.subheader("LPK Kelompok 5 kelas 1B")
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ14t8HA1se2NSlH_HgONi6kDbZaUahw4c7jakCCoCk12S2gShOu9hdyWP7kLw1pdPOe26UfCi4lwEp3X2P4TxeVkOVxgPoJ9peldCVL7k457LyyhM39t5XH5mPbQovaQbp5yeiufXLfd3lk0v8lR_9_pdj_VHoB11Uo4N1JpFHtNGQjwBz14yjEMHMGlY/s16000-rw/tabel%20periodik%20unsur%20kimia.jpg")

