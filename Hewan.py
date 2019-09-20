class Hewan(object):
  def __init__ (self, a, k, m):
    self.ayam = a
    self.kucing = k
    self.merpati = m
    
  def jumlahHewan(self):
    return self.ayam + self.kucing + self.merpati
    
  def cetakData(self):
    print("Ayam\t: ", self.ayam)
    print("Kucing\t: ", self.kucing)
    print("Merpati\t: ", self.merpati)
    
  def cetakJH(self):
    print("Total dari semua hewan diatas\t= ", self.jumlahHewan())
    
class WarnaHewan(Hewan):
  def __init__ (self, a, k, m, w):
    self.ayam = a
    self.kucing = k
    self.merpati = m
    self.warna = w
  def cetakData(self):
    print("Ayam\t: ", self.ayam)
    print("Kucing\t: ", self.kucing)
    print("Merpati\t: ", self.merpati)
    print("Warna dari semua hewan diatas adalah", self.warna)
  
def main():
  wh1 = WarnaHewan (17, 3, 20, "Putih")
  
  wh1.cetakData()
  wh1.cetakJH()

if __name__ == "__main__":
  main()
