class Gempa:

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print('Retak-retak')
        elif 4 <= self.skala <= 6:
            print("Rumah roboh")
        elif self.skala > 6:
            print("Gempa besar berpotensi tsunami")
