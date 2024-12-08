class Sertifikasi:
    def __init__(self, data, hasil):
        self.data = data
        self.hasil = hasil
        self.data_peserta = {}
        self.total_peserta = 0
        self.rata_rata = 0.0
        self.nilai_tertinggi = ("", 0.0)
        self.nilai_terendah = ("", 100.0)
        self.lulus = []

    def read(self):
        file = open(self.data, 'r')
        lines = file.readlines()
        for line in lines[1:]:
            nama, nilai = line.strip().split(";")
            self.data_peserta[nama.strip('"')] = float(nilai)
        file.close()
        print("Data berhasil dibaca.")

    def hitung_statistik(self):
        self.total_peserta = len(self.data_peserta)
        total_nilai = 0.0  
        for nilai in self.data_peserta.values():
            total_nilai += nilai  
        self.rata_rata = total_nilai / self.total_peserta

        for nama, nilai in self.data_peserta.items():
            if nilai > self.nilai_tertinggi[1]:
                self.nilai_tertinggi = (nama, nilai)
            if nilai < self.nilai_terendah[1]:
                self.nilai_terendah = (nama, nilai)
            if nilai > 80.0:
                self.lulus.append((nama, nilai))

    def tulis_hasil(self):
        file = open(self.hasil, 'w')
        file.write(f"Ketik nama file data : {self.data}\n")
        file.write(f"Ketik nama file hasil: {self.hasil}\n")   
        file.write(f"Total jumlah peserta: {self.total_peserta}\n")
        file.write(f"Rata-rata nilai: {self.rata_rata:.2f}\n")
        file.write(f"Peserta dengan nilai tertinggi: {self.nilai_tertinggi[0]} ({self.nilai_tertinggi[1]:.2f})\n")
        file.write(f"Peserta dengan nilai terendah: {self.nilai_terendah[0]} ({self.nilai_terendah[1]:.2f})\n")
        file.write("=== Daftar peserta LULUS UJI sertifikasi ===\n")
        for nama, nilai in self.lulus:
            file.write(f"{nama} ({nilai:.2f})\n")
        file.close()
        print(f"Hasil perhitungan telah ditulis ke file {self.hasil}")

if __name__ == "__main__":
    data = "sertifikasi.txt"
    hasil = "rekap-data.txt"
    sertifikasi = Sertifikasi(data, hasil)
    sertifikasi.read()
    sertifikasi.hitung_statistik()
    sertifikasi.tulis_hasil()