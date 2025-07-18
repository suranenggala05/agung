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
ELEMENTS_DATA = {
    'H': {'name': 'Hidrogen', 'number': 1, 'mass': 1.008, 'group': 1, 'period': 1, 'category': 'nonlogam-reaktif'},
    'He': {'name': 'Helium', 'number': 2, 'mass': 4.0026, 'group': 18, 'period': 1, 'category': 'gas-mulia'},
    'Li': {'name': 'Litium', 'number': 3, 'mass': 6.94, 'group': 1, 'period': 2, 'category': 'logam-alkali'},
    'Be': {'name': 'Berilium', 'number': 4, 'mass': 9.0122, 'group': 2, 'period': 2, 'category': 'alkali-tanah'},
    'B': {'name': 'Boron', 'number': 5, 'mass': 10.81, 'group': 13, 'period': 2, 'category': 'metaloid'},
    'C': {'name': 'Karbon', 'number': 6, 'mass': 12.011, 'group': 14, 'period': 2, 'category': 'nonlogam-reaktif'},
    'N': {'name': 'Nitrogen', 'number': 7, 'mass': 14.007, 'group': 15, 'period': 2, 'category': 'nonlogam-reaktif'},
    'O': {'name': 'Oksigen', 'number': 8, 'mass': 15.999, 'group': 16, 'period': 2, 'category': 'nonlogam-reaktif'},
    'F': {'name': 'Fluorin', 'number': 9, 'mass': 18.998, 'group': 17, 'period': 2, 'category': 'nonlogam-reaktif'},
    'Ne': {'name': 'Neon', 'number': 10, 'mass': 20.180, 'group': 18, 'period': 2, 'category': 'gas-mulia'},
    'Na': {'name': 'Natrium', 'number': 11, 'mass': 22.990, 'group': 1, 'period': 3, 'category': 'logam-alkali'},
    'Mg': {'name': 'Magnesium', 'number': 12, 'mass': 24.305, 'group': 2, 'period': 3, 'category': 'alkali-tanah'},
    'Al': {'name': 'Aluminium', 'number': 13, 'mass': 26.982, 'group': 13, 'period': 3, 'category': 'logam-pasca-transisi'},
    'Si': {'name': 'Silikon', 'number': 14, 'mass': 28.085, 'group': 14, 'period': 3, 'category': 'metaloid'},
    'P': {'name': 'Fosfor', 'number': 15, 'mass': 30.974, 'group': 15, 'period': 3, 'category': 'nonlogam-reaktif'},
    'S': {'name': 'Belerang', 'number': 16, 'mass': 32.06, 'group': 16, 'period': 3, 'category': 'nonlogam-reaktif'},
    'Cl': {'name': 'Klorin', 'number': 17, 'mass': 35.45, 'group': 17, 'period': 3, 'category': 'nonlogam-reaktif'},
    'Ar': {'name': 'Argon', 'number': 18, 'mass': 39.948, 'group': 18, 'period': 3, 'category': 'gas-mulia'},
    'K': {'name': 'Kalium', 'number': 19, 'mass': 39.098, 'group': 1, 'period': 4, 'category': 'logam-alkali'},
    'Ca': {'name': 'Kalsium', 'number': 20, 'mass': 40.078, 'group': 2, 'period': 4, 'category': 'alkali-tanah'},
    'Sc': {'name': 'Skandium', 'number': 21, 'mass': 44.956, 'group': 3, 'period': 4, 'category': 'logam-transisi'},
    'Ti': {'name': 'Titanium', 'number': 22, 'mass': 47.867, 'group': 4, 'period': 4, 'category': 'logam-transisi'},
    'V': {'name': 'Vanadium', 'number': 23, 'mass': 50.942, 'group': 5, 'period': 4, 'category': 'logam-transisi'},
    'Cr': {'name': 'Kromium', 'number': 24, 'mass': 51.996, 'group': 6, 'period': 4, 'category': 'logam-transisi'},
    'Mn': {'name': 'Mangan', 'number': 25, 'mass': 54.938, 'group': 7, 'period': 4, 'category': 'logam-transisi'},
    'Fe': {'name': 'Besi', 'number': 26, 'mass': 55.845, 'group': 8, 'period': 4, 'category': 'logam-transisi'},
    'Co': {'name': 'Kobalt', 'number': 27, 'mass': 58.933, 'group': 9, 'period': 4, 'category': 'logam-transisi'},
    'Ni': {'name': 'Nikel', 'number': 28, 'mass': 58.693, 'group': 10, 'period': 4, 'category': 'logam-transisi'},
    'Cu': {'name': 'Tembaga', 'number': 29, 'mass': 63.546, 'group': 11, 'period': 4, 'category': 'logam-transisi'},
    'Zn': {'name': 'Seng', 'number': 30, 'mass': 65.38, 'group': 12, 'period': 4, 'category': 'logam-transisi'},
    'Ga': {'name': 'Galium', 'number': 31, 'mass': 69.723, 'group': 13, 'period': 4, 'category': 'logam-pasca-transisi'},
    'Ge': {'name': 'Germanium', 'number': 32, 'mass': 72.630, 'group': 14, 'period': 4, 'category': 'metaloid'},
    'As': {'name': 'Arsen', 'number': 33, 'mass': 74.922, 'group': 15, 'period': 4, 'category': 'metaloid'},
    'Se': {'name': 'Selenium', 'number': 34, 'mass': 78.971, 'group': 16, 'period': 4, 'category': 'nonlogam-reaktif'},
    'Br': {'name': 'Bromin', 'number': 35, 'mass': 79.904, 'group': 17, 'period': 4, 'category': 'nonlogam-reaktif'},
    'Kr': {'name': 'Kripton', 'number': 36, 'mass': 83.798, 'group': 18, 'period': 4, 'category': 'gas-mulia'},
    'Rb': {'name': 'Rubidium', 'number': 37, 'mass': 85.468, 'group': 1, 'period': 5, 'category': 'logam-alkali'},
    'Sr': {'name': 'Stronsium', 'number': 38, 'mass': 87.62, 'group': 2, 'period': 5, 'category': 'alkali-tanah'},
    'Y': {'name': 'Itrium', 'number': 39, 'mass': 88.906, 'group': 3, 'period': 5, 'category': 'logam-transisi'},
    'Zr': {'name': 'Zirkonium', 'number': 40, 'mass': 91.224, 'group': 4, 'period': 5, 'category': 'logam-transisi'},
    'Nb': {'name': 'Niobium', 'number': 41, 'mass': 92.906, 'group': 5, 'period': 5, 'category': 'logam-transisi'},
    'Mo': {'name': 'Molibdenum', 'number': 42, 'mass': 95.96, 'group': 6, 'period': 5, 'category': 'logam-transisi'},
    'Tc': {'name': 'Teknesium', 'number': 43, 'mass': 98, 'group': 7, 'period': 5, 'category': 'logam-transisi'},
    'Ru': {'name': 'Rutenium', 'number': 44, 'mass': 101.07, 'group': 8, 'period': 5, 'category': 'logam-transisi'},
    'Rh': {'name': 'Rodium', 'number': 45, 'mass': 102.91, 'group': 9, 'period': 5, 'category': 'logam-transisi'},
    'Pd': {'name': 'Paladium', 'number': 46, 'mass': 106.42, 'group': 10, 'period': 5, 'category': 'logam-transisi'},
    'Ag': {'name': 'Perak', 'number': 47, 'mass': 107.87, 'group': 11, 'period': 5, 'category': 'logam-transisi'},
    'Cd': {'name': 'Kadmium', 'number': 48, 'mass': 112.41, 'group': 12, 'period': 5, 'category': 'logam-transisi'},
    'In': {'name': 'Indium', 'number': 49, 'mass': 114.82, 'group': 13, 'period': 5, 'category': 'logam-pasca-transisi'},
    'Sn': {'name': 'Timah', 'number': 50, 'mass': 118.71, 'group': 14, 'period': 5, 'category': 'logam-pasca-transisi'},
    'Sb': {'name': 'Antimon', 'number': 51, 'mass': 121.76, 'group': 15, 'period': 5, 'category': 'metaloid'},
    'Te': {'name': 'Telurium', 'number': 52, 'mass': 127.60, 'group': 16, 'period': 5, 'category': 'metaloid'},
    'I': {'name': 'Iodin', 'number': 53, 'mass': 126.90, 'group': 17, 'period': 5, 'category': 'nonlogam-reaktif'},
    'Xe': {'name': 'Xenon', 'number': 54, 'mass': 131.29, 'group': 18, 'period': 5, 'category': 'gas-mulia'},
    'Cs': {'name': 'Sesium', 'number': 55, 'mass': 132.91, 'group': 1, 'period': 6, 'category': 'logam-alkali'},
    'Ba': {'name': 'Barium', 'number': 56, 'mass': 137.33, 'group': 2, 'period': 6, 'category': 'alkali-tanah'},
    'La': {'name': 'Lantanum', 'number': 57, 'mass': 138.91, 'group': 3, 'period': 6, 'category': 'lantanida'},
    'Ce': {'name': 'Serium', 'number': 58, 'mass': 140.12, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Pr': {'name': 'Praseodimium', 'number': 59, 'mass': 140.91, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Nd': {'name': 'Neodimium', 'number': 60, 'mass': 144.24, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Pm': {'name': 'Prometium', 'number': 61, 'mass': 145, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Sm': {'name': 'Samarium', 'number': 62, 'mass': 150.36, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Eu': {'name': 'Europium', 'number': 63, 'mass': 151.96, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Gd': {'name': 'Gadolinium', 'number': 64, 'mass': 157.25, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Tb': {'name': 'Terbium', 'number': 65, 'mass': 158.93, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Dy': {'name': 'Disprosium', 'number': 66, 'mass': 162.50, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Ho': {'name': 'Holmium', 'number': 67, 'mass': 164.93, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Er': {'name': 'Erbium', 'number': 68, 'mass': 167.26, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Tm': {'name': 'Tulium', 'number': 69, 'mass': 168.93, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Yb': {'name': 'Iterbium', 'number': 70, 'mass': 173.05, 'group': None, 'period': 8, 'category': 'lantanida'},
    'Lu': {'name': 'Lutetium', 'number': 71, 'mass': 174.97, 'group': 4, 'period': 6, 'category': 'lantanida'},
    'Hf': {'name': 'Hafnium', 'number': 72, 'mass': 178.49, 'group': 4, 'period': 6, 'category': 'logam-transisi'},
    'Ta': {'name': 'Tantalum', 'number': 73, 'mass': 180.95, 'group': 5, 'period': 6, 'category': 'logam-transisi'},
    'W': {'name': 'Wolfram', 'number': 74, 'mass': 183.84, 'group': 6, 'period': 6, 'category': 'logam-transisi'},
    'Re': {'name': 'Renium', 'number': 75, 'mass': 186.21, 'group': 7, 'period': 6, 'category': 'logam-transisi'},
    'Os': {'name': 'Osmium', 'number': 76, 'mass': 190.23, 'group': 8, 'period': 6, 'category': 'logam-transisi'},
    'Ir': {'name': 'Iridium', 'number': 77, 'mass': 192.22, 'group': 9, 'period': 6, 'category': 'logam-transisi'},
    'Pt': {'name': 'Platina', 'number': 78, 'mass': 195.08, 'group': 10, 'period': 6, 'category': 'logam-transisi'},
    'Au': {'name': 'Emas', 'number': 79, 'mass': 196.97, 'group': 11, 'period': 6, 'category': 'logam-transisi'},
    'Hg': {'name': 'Raksa', 'number': 80, 'mass': 200.59, 'group': 12, 'period': 6, 'category': 'logam-transisi'},
    'Tl': {'name': 'Talium', 'number': 81, 'mass': 204.38, 'group': 13, 'period': 6, 'category': 'logam-pasca-transisi'},
    'Pb': {'name': 'Timbal', 'number': 82, 'mass': 207.2, 'group': 14, 'period': 6, 'category': 'logam-pasca-transisi'},
    'Bi': {'name': 'Bismut', 'number': 83, 'mass': 208.98, 'group': 15, 'period': 6, 'category': 'logam-pasca-transisi'},
    'Po': {'name': 'Polonium', 'number': 84, 'mass': 209, 'group': 16, 'period': 6, 'category': 'metaloid'},
    'At': {'name': 'Astatin', 'number': 85, 'mass': 210, 'group': 17, 'period': 6, 'category': 'nonlogam-reaktif'},
    'Rn': {'name': 'Radon', 'number': 86, 'mass': 222, 'group': 18, 'period': 6, 'category': 'gas-mulia'},
    'Fr': {'name': 'Fransium', 'number': 87, 'mass': 223, 'group': 1, 'period': 7, 'category': 'logam-alkali'},
    'Ra': {'name': 'Radium', 'number': 88, 'mass': 226, 'group': 2, 'period': 7, 'category': 'alkali-tanah'},
    'Ac': {'name': 'Aktinium', 'number': 89, 'mass': 227, 'group': 3, 'period': 7, 'category': 'aktinida'},
    'Th': {'name': 'Torium', 'number': 90, 'mass': 232.04, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Pa': {'name': 'Protaktinium', 'number': 91, 'mass': 231.04, 'group': None, 'period': 9, 'category': 'aktinida'},
    'U': {'name': 'Uranium', 'number': 92, 'mass': 238.03, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Np': {'name': 'Neptunium', 'number': 93, 'mass': 237, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Pu': {'name': 'Plutonium', 'number': 94, 'mass': 244, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Am': {'name': 'Amerisium', 'number': 95, 'mass': 243, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Cm': {'name': 'Kurium', 'number': 96, 'mass': 247, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Bk': {'name': 'Berkelium', 'number': 97, 'mass': 247, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Cf': {'name': 'Kalifornium', 'number': 98, 'mass': 251, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Es': {'name': 'Einsteinium', 'number': 99, 'mass': 252, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Fm': {'name': 'Fermium', 'number': 100, 'mass': 257, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Md': {'name': 'Mendelevium', 'number': 101, 'mass': 258, 'group': None, 'period': 9, 'category': 'aktinida'},
    'No': {'name': 'Nobelium', 'number': 102, 'mass': 259, 'group': None, 'period': 9, 'category': 'aktinida'},
    'Lr': {'name': 'Lawrensium', 'number': 103, 'mass': 262, 'group': 4, 'period': 7, 'category': 'aktinida'},
    'Rf': {'name': 'Rutherfordium', 'number': 104, 'mass': 267, 'group': 4, 'period': 7, 'category': 'logam-transisi'},
    'Db': {'name': 'Dubnium', 'number': 105, 'mass': 268, 'group': 5, 'period': 7, 'category': 'logam-transisi'},
    'Sg': {'name': 'Seaborgium', 'number': 106, 'mass': 271, 'group': 6, 'period': 7, 'category': 'logam-transisi'},
    'Bh': {'name': 'Bohrium', 'number': 107, 'mass': 272, 'group': 7, 'period': 7, 'category': 'logam-transisi'},
    'Hs': {'name': 'Hassium', 'number': 108, 'mass': 270, 'group': 8, 'period': 7, 'category': 'logam-transisi'},
    'Mt': {'name': 'Meitnerium', 'number': 109, 'mass': 276, 'group': 9, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Ds': {'name': 'Darmstadtium', 'number': 110, 'mass': 281, 'group': 10, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Rg': {'name': 'Roentgenium', 'number': 111, 'mass': 280, 'group': 11, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Cn': {'name': 'Kopernisium', 'number': 112, 'mass': 285, 'group': 12, 'period': 7, 'category': 'logam-transisi'},
    'Nh': {'name': 'Nihonium', 'number': 113, 'mass': 284, 'group': 13, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Fl': {'name': 'Flerovium', 'number': 114, 'mass': 289, 'group': 14, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Mc': {'name': 'Moskovium', 'number': 115, 'mass': 288, 'group': 15, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Lv': {'name': 'Livermorium', 'number': 116, 'mass': 293, 'group': 16, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Ts': {'name': 'Tennessin', 'number': 117, 'mass': 294, 'group': 17, 'period': 7, 'category': 'properti-tak-dikenal'},
    'Og': {'name': 'Oganesson', 'number': 118, 'mass': 294, 'group': 18, 'period': 7, 'category': 'properti-tak-dikenal'},
}

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
       
