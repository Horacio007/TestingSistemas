import sqlite3

#clase para crear el objeto mascota y sus metodos
class Mascota():
    #creamos el objeto
    def __init__(self, nombre, especie, raza, edad, genero, color, ternura, eVida):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.genero = genero
        self.color = color
        self.ternura = ternura
        self.eVida = eVida

    #metodo toString
    def __str__(self):
        return str(f"Tu Mascota se llama {self.nombre} es un {self.especie} de raza {self.raza} con edad de {self.edad} su genero es {self.genero} de color {self.color} con ternura de {self.ternura} y esperanza de vida de {self.eVida} años")

    #comparacion de los atributos
    def __eq__(self, mascota):
        if mascota.nombre != self.nombre:
            return False

        if mascota.especie != self.especie:
            return False

        if mascota.raza != self.raza:
            return False

        if mascota.edad != self.edad:
            return False

        if mascota.genero != self.genero:
            return False

        if mascota.color != self.color:
            return False

        if mascota.ternura != self.ternura:
            return False

        if mascota.eVida != self.eVida:
            return False
        return True

#clase de la base de datos
class sqlite():
    def __init__(self, archivoM):
        self.conn = sqlite3.connect(archivoM)

    def guardar(self, mascota):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO mascotas VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(mascota.nombre, mascota.especie, mascota.raza, mascota.edad, mascota.genero, mascota.color, mascota.ternura, mascota.eVida))
        self.conn.commit()

    def mostrar(self):
        cur = self.conn.cursor()
        mascotas = cur.execute("SELECT * FROM mascotas").fetchall()
        listaM = []

        for m in mascotas:
            listaM.append(Mascota(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7]))
        return listaM

def guardarMascota(mascota, db):
    db.guardar(mascota)

def mostrarMascota(db):
    mascotas = db.mostrar()
    return  mascotas

if __name__ == '__main__':
    mascota1 = Mascota("Chester", "Perro", "French Poodle", 11, "Macho", "Blanco", "Indescriptible", 15)
    mascota2 = Mascota("Max", "Perro", "Schnauzer", 1, "Macho", "Sal-Pimienta", "Alta", 16)
    mascota3 = Mascota("Pinguino", "Perro", "Chihuahua", 3, "Macho", "Pinto", "Tremendo", 20)
    mascota4 = Mascota("Roy", "Hamster", "Sirio", 11, "Macho", "Blanco", "Competitiva", 3)
    mascota5 = Mascota("El Loco Bily", "Pez de agua dulce", "Carpa Dorada", 5, "Macho", "Dorado", "Alterada", 10)

    db = sqlite("MascotasDB.db")
    cur = db.conn.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS mascotas
    (nombre Text,
    especie Text,
    raza Text,
    edad Integer,
    genero Text,
    color Text,
    ternura Text,
    eVida Integer)
    ''')

    guardarMascota(mascota1, db)
    guardarMascota(mascota2, db)
    guardarMascota(mascota3, db)
    guardarMascota(mascota4, db)
    guardarMascota(mascota5, db)
    print(*mostrarMascota(db), sep="\n")