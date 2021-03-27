from random import randint

class Beaner:
    def __init__(self):
        self.red = "\U0001F534"
        self.yellow = "\U0001F7E1"
        self.green = "\U0001F7E2"
        self.blue = "\U0001F535"
        self.radioactive = "\U00002622" 
        self.black = "\U000026AB"
        self.white = "\U000026AA"
        self.purple = "\U0001F7E3"
        self.orange = "\U0001F7E0"
        self.brown = "\U0001F7E4"

        self.sabores = [
            "Picanha " + self.red, 
            "Pimenta Preta " + self.black, 
            "Meleca " + self.green, 
            "Podrão " + self.yellow, 
            "Algodão Doce" + self.purple, 
            "Cereja " + self.red, 
            "Minhoca " + self.brown,
            "Sujeira " + self.brown,
            "Cera " + self.yellow,
            "Grama " + self.green,
            "Azeitona " + self.green,
            "Limão " + self.green,
            "Ovo Podre " + self.yellow,
            "Salsicha " + self.red,
            "Sabonete " + self.blue,
            "Cerveja " + self.yellow,
            "Tutti-Fruti " + self.purple,
            "Vômito " + self.green,
            "Melancia " + self.red,
            "Césio-137 " + self.blue,
            "Coquinha Gelada " + self.red,
            "Desodorante " + self.white,
            "Farofa Pronta Yoki " + self.yellow,
            "Kaiser " + self.yellow,
            "Crocs " + self.blue,
            "Corote de Pêssego" + self.orange,
            "Caldo de Cana " + self.green,
            "Sola de Sapato " + self.brown,
            "Pilha Panasonic " + self.blue,
            "Vinho " + self.purple,
            "Óleo Diesel " + self.orange 
        ]

    def getFlavor(self):
        rdFlavorIndex = randint(0, len(self.sabores) - 1)
        return self.sabores[rdFlavorIndex]
