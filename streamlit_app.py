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
elif menu == "Kalkulator Kimia Dasar":
    st.title("Kalkulator Kimia Dasar")
    st.subheader("Pilih Rumus yang Akan Dihitung")

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

    def buat_pdf(judul, isi):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=judul, ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=isi)
        buffer = io.BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return buffer

    if rumus == "Massa Jenis":
        massa = st.number_input("Massa (gram)")
        volume = st.number_input("Volume (cm³)")
        if st.button("Hitung"):
            hasil = massa / volume if volume != 0 else 0
            st.success(f"Massa Jenis: {hasil} g/cm³")
            isi = f"Massa: {massa} gram\nVolume: {volume} cm³\nMassa Jenis: {hasil} g/cm³"
            st.download_button("Download PDF", data=buat_pdf("Massa Jenis", isi), file_name="massa_jenis.pdf", mime="application/pdf")

    elif rumus == "Massa Mol":
        massa = st.number_input("Massa Zat (gram)")
        Mr = st.number_input("Massa Molekul Relatif (Mr)")
        if st.button("Hitung"):
            hasil = massa / Mr if Mr != 0 else 0
            st.success(f"Mol: {hasil} mol")
            isi = f"Massa: {massa} gram\nMr: {Mr}\nMol: {hasil} mol"
            st.download_button("Download PDF", data=buat_pdf("Massa Mol", isi), file_name="massa_mol.pdf", mime="application/pdf")

    elif rumus == "Konsentrasi Molar":
        mol = st.number_input("Mol zat (mol)")
        volume_l = st.number_input("Volume (liter)")
        if st.button("Hitung"):
            hasil = mol / volume_l if volume_l != 0 else 0
            st.success(f"Konsentrasi: {hasil} M")
            isi = f"Mol: {mol} mol\nVolume: {volume_l} L\nMolaritas: {hasil} M"
            st.download_button("Download PDF", data=buat_pdf("Konsentrasi Molar", isi), file_name="konsentrasi_molar.pdf", mime="application/pdf")

    elif rumus == "Konsentrasi Molal":
        mol = st.number_input("Mol zat (mol)")
        massa_pelarut = st.number_input("Massa Pelarut (kg)")
        if st.button("Hitung"):
            hasil = mol / massa_pelarut if massa_pelarut != 0 else 0
            st.success(f"Konsentrasi: {hasil} mol/kg")
            isi = f"Mol: {mol} mol\nMassa Pelarut: {massa_pelarut} kg\nMolalitas: {hasil} mol/kg"
            st.download_button("Download PDF", data=buat_pdf("Konsentrasi Molal", isi), file_name="konsentrasi_molal.pdf", mime="application/pdf")

    elif rumus == "Hukum Avogadro":
        V1 = st.number_input("Volume 1 (L)")
        n1 = st.number_input("Mol 1 (mol)")
        n2 = st.number_input("Mol 2 (mol)")
        if st.button("Hitung"):
            V2 = (n2 / n1) * V1 if n1 != 0 else 0
            st.success(f"Volume 2: {V2} L")
            isi = f"V1: {V1} L\nn1: {n1} mol\nn2: {n2} mol\nV2: {V2} L"
            st.download_button("Download PDF", data=buat_pdf("Hukum Avogadro", isi), file_name="avogadro.pdf", mime="application/pdf")

    elif rumus == "Hukum Boyle":
        P1 = st.number_input("Tekanan 1 (atm)")
        V1 = st.number_input("Volume 1 (L)")
        P2 = st.number_input("Tekanan 2 (atm)")
        if st.button("Hitung"):
            V2 = (P1 * V1) / P2 if P2 != 0 else 0
            st.success(f"Volume 2: {V2} L")
            isi = f"P1: {P1} atm\nV1: {V1} L\nP2: {P2} atm\nV2: {V2} L"
            st.download_button("Download PDF", data=buat_pdf("Hukum Boyle", isi), file_name="boyle.pdf", mime="application/pdf")

    elif rumus == "Hukum Charles":
        V1 = st.number_input("Volume 1 (L)")
        T1 = st.number_input("Suhu 1 (K)")
        T2 = st.number_input("Suhu 2 (K)")
        if st.button("Hitung"):
            V2 = (V1 * T2) / T1 if T1 != 0 else 0
            st.success(f"Volume 2: {V2} L")
            isi = f"V1: {V1} L\nT1: {T1} K\nT2: {T2} K\nV2: {V2} L"
            st.download_button("Download PDF", data=buat_pdf("Hukum Charles", isi), file_name="charles.pdf", mime="application/pdf")

    elif rumus == "Tekanan Gas Ideal":
        n = st.number_input("Mol (mol)")
        T = st.number_input("Suhu (K)")
        V = st.number_input("Volume (L)")
        R = 0.0821
        if st.button("Hitung"):
            P = (n * R * T) / V if V != 0 else 0
            st.success(f"Tekanan: {P} atm")
            isi = f"n: {n} mol\nT: {T} K\nV: {V} L\nP: {P} atm"
            st.download_button("Download PDF", data=buat_pdf("Tekanan Gas Ideal", isi), file_name="gas_ideal.pdf", mime="application/pdf")

    elif rumus == "Energi Ikatan":
        jumlah_ikatan = st.number_input("Jumlah Ikatan")
        energi_per_ikatan = st.number_input("Energi per Ikatan (kJ/mol)")
        if st.button("Hitung"):
            energi = jumlah_ikatan * energi_per_ikatan
            st.success(f"Energi Total: {energi} kJ/mol")
            isi = f"Jumlah Ikatan: {jumlah_ikatan}\nEnergi/Ikatan: {energi_per_ikatan} kJ/mol\nEnergi Total: {energi} kJ/mol"
            st.download_button("Download PDF", data=buat_pdf("Energi Ikatan", isi), file_name="energi_ikatan.pdf", mime="application/pdf")

    elif rumus == "Persen Massa":
        massa_zat = st.number_input("Massa Zat (gram)")
        massa_larutan = st.number_input("Massa Larutan (gram)")
        if st.button("Hitung"):
            persen = (massa_zat / massa_larutan) * 100 if massa_larutan != 0 else 0
            st.success(f"Persen Massa: {persen} %")
            isi = f"Massa Zat: {massa_zat} gram\nMassa Larutan: {massa_larutan} gram\nPersen Massa: {persen} %"
            st.download_button("Download PDF", data=buat_pdf("Persen Massa", isi), file_name="persen_massa.pdf", mime="application/pdf")
