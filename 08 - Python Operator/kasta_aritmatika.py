#  DOKUMENTASI SAKTI: PRECEDENCE ORDER (KASTA ARITMATIKA MATEMATIKA)
# ==============================================================================
# Rumus Mutlak: Komputer menghitung dari kasta PALING ATAS ke PALING BAWAH.
# Urutan Kasta Aritmatika:
# Kasta 1 (TERTINGGI) : () Tanda Kurung
# Kasta 2             : ** (Pangkat)
# Kasta 3 (Sama Kuat) : * , / , // , %  (Perkalian, Pembagian, Floor Div, Modulus)
# Kasta 4 (TERENDAH)  : + , - (Penjumlahan, Pengurangan)
# NOTE: Jika kastanya SAMA KUAT, komputer ngitung dari KIRI ke KANAN.
# ==============================================================================

# ------------------------------------------------------------------------------
# KASUS 1: Pembuktian Perkalian (*) vs Penjumlahan (+)
# ------------------------------------------------------------------------------
# * (Kasta 3) lebih tinggi dari + (Kasta 4). Jadi 3 * 2 dihitung duluan.
kasus_1 = 5 + 3 * 2
print("KASUS 1 (5 + 3 * 2)   -> Hasil harusnya 11")
print("Hasil di Terminal     :", kasus_1)
print("-" * 40)


# ------------------------------------------------------------------------------
# KASUS 2: Pembuktian Kekuatan Mutlak Tanda Kurung ()
# ------------------------------------------------------------------------------
# Meskipun ada *, tanda kurung () adalah Kasta Raja (Tertinggi). 
# Maka 5 + 3 wajib dihitung duluan, baru hasilnya dikali 2.
kasus_2 = (5 + 3) * 2
print("KASUS 2 ((5 + 3) * 2) -> Hasil harusnya 16")
print("Hasil di Terminal     :", kasus_2)
print("-" * 40)


# ------------------------------------------------------------------------------
# KASUS 3: Pembuktian Kasta Setara (Ribut dari Kiri ke Kanan)
# ------------------------------------------------------------------------------
# Operator % (Modulus) dan * (Perkalian) itu kastanya SAMA KUAT (Kasta 3).
# Jalur hitungnya: 10 % 3 dulu (sisa 1), baru hasil 1 dikali 4 (1 * 4).
kasus_3 = 10 % 3 * 4
print("KASUS 3 (10 % 3 * 4)  -> Hasil harusnya 4")
print("Hasil di Terminal     :", kasus_3)
print("-" * 40)


# ------------------------------------------------------------------------------
# KASUS 4: Eksperimen Gabungan Ribet (Kurung ➡️ Pangkat ➡️ Kali)
# ------------------------------------------------------------------------------
# Alur Otak Komputer:
# 1. Hitung di dalam kurung dulu: (1 + 2) = 3
# 2. Hitung pangkat: 3 ** 2 (3 pangkat 2) = 9
# 3. Terakhir hitung perkalian: 2 * 9 = 18
kasus_4 = 2 * (1 + 2) ** 2
print("KASUS 4 (2 * (1 + 2) ** 2) -> Hasil harusnya 18")
print("Hasil di Terminal          :", kasus_4)