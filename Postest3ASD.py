#Nurul Asmita(2309116073)
#Program Pendataan Toko Olahraga

class Node:
    def __init__(self, toko_olahraga):
        self.data = toko_olahraga
        self.next = None

class PendataanTokoOlahraga:
    def __init__(self):
        self.head = None

    # Fungsi menambahkan data barang di awal linked list
    def tambah_di_awal(self, toko_olahraga):
        new_node = Node(toko_olahraga)
        new_node.next = self.head
        self.head = new_node
        print("*****Barang berhasil ditambahkan di awal linked list*****\n")

    # Fungsi menambahkan data barang di akhir linked list
    def tambah_di_akhir(self, toko_olahraga):
        new_node = Node(toko_olahraga)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print("*****Barang berhasil ditambahkan di akhir linked list*****\n")

    # Fungsi menambahkan data barang di antara node
    def tambah_di_antara(self, kode_barang_sebelum, toko_olahraga):
        new_node = Node(toko_olahraga)
        current = self.head
        while current:
            if current.data.kode_barang == kode_barang_sebelum:
                new_node.next = current.next
                current.next = new_node
                print("*****Barang berhasil ditambahkan di antara node*****\n")
                return
            current = current.next
        print("*****Barang dengan kode", kode_barang_sebelum, "tidak ditemukan*****\n")

    # Fungsi menghapus data barang di awal linked list
    def hapus_di_awal(self):
        if not self.head:
            print("Tidak ada barang yang tersimpan\n")
            return
        self.head = self.head.next
        print("*****Barang pertama berhasil dihapus*****")

    # Fungsi menghapus data barang di akhir linked list
    def hapus_di_akhir(self):
        if not self.head:
            print("Tidak ada barang yang tersimpan\n")
            return
        if not self.head.next:
            self.head = None
            print("*****Barang terakhir berhasil dihapus*****")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        print("*****Barang terakhir berhasil dihapus*****")

    # Fungsi menghapus data barang di antara node
    def hapus_di_antara(self, kode_barang_sebelum, kode_barang):
        if not self.head:
            print("Tidak ada barang yang tersimpan\n")
            return
        if self.head.data.kode_barang == kode_barang:
            self.head = self.head.next
            print("*****Barang berhasil dihapus*****")
            return
        current = self.head
        while current.next:
            if current.next.data.kode_barang == kode_barang:
                current.next = current.next.next
                print("*****Barang berhasil dihapus*****")
                return
            current = current.next
        print("*****Barang dengan kode", kode_barang, "tidak ditemukan*****")

    # Fungsi menampilkan data barang
    def lihat_barang(self):
        if not self.head:
            print("Tidak ada barang yang tersimpan\n")
            return
        current = self.head
        while current:
            print(f"Kode Barang: {current.data.kode_barang}")
            print(f"Nama Barang: {current.data.nama_barang}")
            print(f"Harga Barang: {current.data.harga_barang}")
            print(f"Stok Barang: {current.data.stok_barang}")
            print(f"Kategori: {current.data.kategori}")
            print()
            current = current.next

        # Fungsi untuk mengatur penyortiran menggunakan Quick Sort
    def quick_sort(self, arr, ascending=True):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        less, equal, greater = [], [], []
        for element in arr:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        if ascending:
            return self.quick_sort(less, ascending) + equal + self.quick_sort(greater, ascending)
        else:
            return self.quick_sort(greater, ascending) + equal + self.quick_sort(less, ascending)

    # Fungsi untuk melakukan penyortiran pada linked list
    def sort(self, attribute, ascending=True):
        arr = []
        current = self.head
        while current:
            if attribute == "kode_barang":
                arr.append(current.data.kode_barang)
            elif attribute == "nama_barang":
                arr.append(current.data.nama_barang)
            elif attribute == "harga_barang":
                arr.append(current.data.harga_barang)
            elif attribute == "stok_barang":
                arr.append(current.data.stok_barang)
            elif attribute == "kategori":
                arr.append(current.data.kategori)
            current = current.next
        arr = self.quick_sort(arr, ascending)
        sorted_list = PendataanTokoOlahraga()
        for item in arr:
            current = self.head
            while current:
                if attribute == "kode_barang" and current.data.kode_barang == item:
                    sorted_list.tambah_di_akhir(current.data)
                elif attribute == "nama_barang" and current.data.nama_barang == item:
                    sorted_list.tambah_di_akhir(current.data)
                elif attribute == "harga_barang" and current.data.harga_barang == item:
                    sorted_list.tambah_di_akhir(current.data)
                elif attribute == "stok_barang" and current.data.stok_barang == item:
                    sorted_list.tambah_di_akhir(current.data)
                elif attribute == "kategori" and current.data.kategori == item:
                    sorted_list.tambah_di_akhir(current.data)
                current = current.next
        return sorted_list

class TokoOlahraga:
    def __init__(self, kode_barang, nama_barang, harga_barang, stok_barang, kategori):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.stok_barang = stok_barang
        self.kategori = kategori

# Fungsi main program pendataan Toko Olahraga
def main():
    toko_olahraga = PendataanTokoOlahraga()

    while True:
        print("=" * 5, "Menu Toko Olahraga", "=" * 5)
        print("=" * 30, "\n")
        print("1. Tambah Barang di Awal")
        print("2. Tambah Barang di Akhir")
        print("3. Tambah Barang di Antara Node")
        print("4. Hapus Barang di Awal")
        print("5. Hapus Barang di Akhir")
        print("6. Hapus Barang di Antara Node")
        print("7. Lihat Barang")
        print("8. Sort Barang")
        print("9. Keluar")

        pilihan = input("Pilih menu yang diinginkan: ")

        if pilihan == '1':
            kode_barang = input("Masukkan kode barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            stok_barang = int(input("Masukkan stok barang: "))
            kategori = input("Masukkan kategori barang: ")
            barang_baru = TokoOlahraga(kode_barang, nama_barang, harga_barang, stok_barang, kategori)
            toko_olahraga.tambah_di_awal(barang_baru)
        elif pilihan == '2':
            kode_barang = input("Masukkan kode barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            stok_barang = int(input("Masukkan stok barang: "))
            kategori = input("Masukkan kategori barang: ")
            barang_baru = TokoOlahraga(kode_barang, nama_barang, harga_barang, stok_barang, kategori)
            toko_olahraga.tambah_di_akhir(barang_baru)
        elif pilihan == '3':
            kode_barang_sebelum = input("Masukkan kode barang sebelum: ")
            kode_barang = input("Masukkan kode barang: ")
            nama_barang = input("Masukkan nama barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            stok_barang = int(input("Masukkan stok barang: "))
            kategori = input("Masukkan kategori barang: ")
            barang_baru = TokoOlahraga(kode_barang, nama_barang, harga_barang, stok_barang, kategori)
            toko_olahraga.tambah_di_antara(kode_barang_sebelum, barang_baru)
        elif pilihan == '4':
            toko_olahraga.hapus_di_awal()
        elif pilihan == '5':
            toko_olahraga.hapus_di_akhir()
        elif pilihan == '6':
            kode_barang_sebelum = input("Masukkan kode barang sebelum: ")
            kode_barang = input("Masukkan kode barang: ")
            toko_olahraga.hapus_di_antara(kode_barang_sebelum, kode_barang)
        elif pilihan == '7':
            toko_olahraga.lihat_barang()
        elif pilihan == '8':
            attribute = input("Masukkan atribut untuk penyortiran (kode_barang/nama_barang/harga_barang/stok_barang/kategori): ")
            order = input("Pilih urutan penyortiran (ascending/descending): ")
            ascending = order.lower() == 'ascending'
            sorted_list = toko_olahraga.sort(attribute, ascending)
            print("\nBarang setelah disortir:")
            sorted_list.lihat_barang()
        elif pilihan == '9':
            print("*****Pendataan di Toko Olahraga telah selesai*****")
            return
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.\n")

main()

