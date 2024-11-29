from Mathematic.basic_math_op import penjumlahan, pengurangan, perkalian, pembagian, perpangkatan, prime

def run_math_operation(res):
    if res == "operasi_matematika_penjumlahan":
        penjumlahan()
    elif res == "operasi_matematika_pengurangan":
        print("Stella :", pengurangan())
    elif res == "operasi_matematika_perkalian":
        print("Stella :", perkalian())
    elif res == "operasi_matematika_pembagian":
        print("Stella :", pembagian())
    elif res == "operasi_matematika_perpangkatan":
        print("Stella :", perpangkatan())
    elif res == "cek_bilangan_prima":
        prime()

# def sifat_bilangan(res):