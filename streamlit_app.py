import streamlit as st

#Sidebar Menu
menu = st.sidebar.selectbox(
    "Pilih menu",
    ["Beranda","Kalkulator Kimia Dasar","Tabel Periodik Unsur","Soal-soal Kimia Dasar","Catatan"]
)

# ---Menu BERANDA ---
if menu =="Beranda":
    st.title("Kalkulator Kimia Dasar")
    st.header("Pengertian Kimia")
   
#--- Menu Tabel Periodik Unsur ---
if menu =="Tabel Periodik Unsur":                               

elif menu == "Kalkulator Kimia Dasar":
    st.title("Kalkulator Kimia Dasar")
    st.subheader("Pilih Rumus yang Akan Dihitung")

    rumus = st.selectbox("Pilih Rumus", [
        "Massa Jenis",
        "Massa Mol",
        "Konsentrasi Molar",
        "Konsentrasi Molal",
        "Hukum Avogadro",
        "Hukum Boyle",
        "Hukum Charles",
        "Tekanan Gas Ideal",
        "Energi Ikatan",
        "Persen Massa"
    ])

    if rumus == "Massa Jenis":
        massa = st.number_input("Massa (gram)")
        volume = st.number_input("Volume (cm³)")
        if st.button("Hitung"):
            hasil = massa / volume if volume != 0 else 0
            st.success(f"Massa Jenis: {hasil} g/cm³")

    elif rumus == "Massa Mol":
        massa = st.number_input("Massa Zat (gram)")
        Mr = st.number_input("Massa Molekul Relatif (Mr)")
        if st.button("Hitung"):
            hasil = massa / Mr if Mr != 0 else 0
            st.success(f"Mol: {hasil} mol")

    elif rumus == "Konsentrasi Molar":
        mol = st.number_input("Jumlah Mol (mol)")
        volume_l = st.number_input("Volume (liter)")
        if st.button("Hitung"):
            hasil = mol / volume_l if volume_l != 0 else 0
            st.success(f"Konsentrasi: {hasil} M")

    elif rumus == "Konsentrasi Molal":
        mol = st.number_input("Jumlah Mol Zat Terlarut (mol)")
        massa_pelarut = st.number_input("Massa Pelarut (kg)")
        if st.button("Hitung"):
            hasil = mol / massa_pelarut if massa_pelarut != 0 else 0
            st.success(f"Konsentrasi: {hasil} mol/kg")

    elif rumus == "Hukum Avogadro":
        V1 = st.number_input("Volume 1 (L)")
        n1 = st.number_input("Mol 1 (mol)")
        n2 = st.number_input("Mol 2 (mol)")
        if st.button("Hitung"):
            V2 = (n2 / n1) * V1 if n1 != 0 else 0
            st.success(f"Volume 2: {V2} L")

    elif rumus == "Hukum Boyle":
        P1 = st.number_input("Tekanan 1 (atm)")
        V1 = st.number_input("Volume 1 (L)")
        P2 = st.number_input("Tekanan 2 (atm)")
        if st.button("Hitung"):
            V2 = (P1 * V1) / P2 if P2 != 0 else 0
            st.success(f"Volume 2: {V2} L")

    elif rumus == "Hukum Charles":
        V1 = st.number_input("Volume 1 (L)")
        T1 = st.number_input("Suhu 1 (K)")
        T2 = st.number_input("Suhu 2 (K)")
        if st.button("Hitung"):
            V2 = (V1 * T2) / T1 if T1 != 0 else 0
            st.success(f"Volume 2: {V2} L")

    elif rumus == "Tekanan Gas Ideal":
        n = st.number_input("Jumlah Mol (mol)")
        T = st.number_input("Suhu (K)")
        V = st.number_input("Volume (L)")
        R = 0.0821  # Konstanta Gas Ideal
        if st.button("Hitung"):
            P = (n * R * T) / V if V != 0 else 0
            st.success(f"Tekanan: {P} atm")

    elif rumus == "Energi Ikatan":
        jumlah_ikatan = st.number_input("Jumlah Ikatan")
        energi_per_ikatan = st.number_input("Energi per Ikatan (kJ/mol)")
        if st.button("Hitung"):
            energi = jumlah_ikatan * energi_per_ikatan
            st.success(f"Energi Total: {energi} kJ/mol")

    elif rumus == "Persen Massa":
        massa_zat = st.number_input("Massa Zat (gram)")
        massa_larutan = st.number_input("Massa Larutan (gram)")
        if st.button("Hitung"):
            persen = (massa_zat / massa_larutan) * 100 if massa_larutan != 0 else 0
            st.success(f"Persen Massa: {persen} %")
            
elif menu == "Soal-soal Kimia Dasar":
    st.title("Soal-Soal Kimia Dasar")
    st.subheader("Silakan pilih soal atau materi yang ingin diakses:")

    pilihan_soal = st.selectbox("Pilih File:", [
        "Latihan Soal kimia dasar mudah (Google Docs)",
        "Latihan Soal kimia dasar 2025 (PDF)",
        "Latihan Soal kimia (Google Drive)"
    ])
       
