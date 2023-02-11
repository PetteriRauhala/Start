# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# =====================================

# KIRJASTOT JA MODUULIT (LIBRARIES AND MODULES)
# ---------------------------------------------

import fitness

# LUOKKAMÄÄRITYKSET (CLASS DEFINITIONS)
# -------------------------------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""
    
    # Oliomudostin eli konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
    
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi painoindeksin laskemiseen
    def painoindeksi(self):
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        return self.bmi

    # Metodi rasvaprosentin laskemiseen (aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(self.bmi,self.ika,self.sukupuoli)
        return self.rasvaprosentti

if __name__ == "__main__":

    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 180, 80, 30, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    # print('painoindeksi on ',kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    