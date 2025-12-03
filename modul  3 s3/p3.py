class Hero:
    def __init__(self, name, health):
        # Konstruktor class Hero (parent)
        # Menyimpan nama dan health ke dalam atribut objek
        self.name = name
        self.health = health

    def showInfo(self):
        # Method untuk menampilkan informasi hero umum
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
        ))


class Hero_intelligent(Hero):
    # Subclass yang mewarisi dari Hero (tipe hero intelligent)

    def __init__(self, name):
        # Konstruktor subclass
        # Memanggil konstruktor parent dengan health default 100
        super().__init__(name, 100)

    def showInfo(self):
        # Method showInfo khusus untuk hero intelligent (override method parent)
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
        ))


class Hero_strength(Hero):
    # Subclass lain yang juga mewarisi dari Hero (tipe hero strength)

    def __init__(self, name):
        # Konstruktor subclass
        # Memanggil konstruktor parent dengan health default 200
        super().__init__(name, 200)


# Membuat objek dari masing-masing subclass
lina = Hero_intelligent('lina')   # Hero intelligent dengan health = 100
axe = Hero_strength('axe')        # Hero strength dengan health = 200

# Memanggil method showInfo milik subclass (override)
lina.showInfo()
