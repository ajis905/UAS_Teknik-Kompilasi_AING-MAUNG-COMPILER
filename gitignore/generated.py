def tambah(a, b):
    return (a + b)
def main():
    print("=== Ujian Akhir AING MAUNG ===")
    angka_awal = 1
    while angka_awal <= 3:
        print("Iterasi ke-")
        print(angka_awal)
        angka_awal = (angka_awal + 1)
    tes_optimasi = ((10 * 5) + 2)
    if tes_optimasi > 50:
        print("Optimasi Matematika Berhasil!")
    else:
        print("Gagal Optimasi")
    hasil = tambah(10, 20)
    print("Hasil Tambah:")
    print(hasil)
main()