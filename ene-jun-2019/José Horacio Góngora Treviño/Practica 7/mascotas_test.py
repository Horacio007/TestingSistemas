import  unittest
import os
from unittest.mock import MagicMock
from mascotas import sqlite, Mascota, mostrarMascota

class TestMascotas(unittest.TestCase):
    #crear la base de datos y darle valores
    def setUp(self):
        self.db = sqlite("TestMascotas.db")
        cur = self.db.conn.cursor()
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

        self.db.guardar(Mascota("Chester", "Perro", "French Poodle", 11, "Macho", "Blanco", "Indescriptible", 15))
        self.db.guardar(Mascota("Max", "Perro", "Schnauzer", 1, "Macho", "Sal-Pimienta", "Alta", 16))
        self.db.guardar(Mascota("Pinguino", "Perro", "Chihuahua", 3, "Macho", "Pinto", "Tremendo", 20))
        self.db.guardar(Mascota("Roy", "Hamster", "Sirio", 11, "Macho", "Blanco", "Competitiva", 3))
        self.db.guardar(Mascota("El Loco Bily", "Pez de agua dulce", "Carpa Dorada", 5, "Macho", "Dorado", "Alterada", 10))

    #borrar la base de datos
    def tearDown(self):
        self.db.conn.close()
        os.remove("TestMascotas.db")

    #pruebas unitarias con mock
    def testShowAll(self):
        entrada = [Mascota("Chester", "Perro", "French Poodle", 11, "Macho", "Blanco", "Indescriptible", 15),
                Mascota("Max", "Perro", "Schnauzer", 1, "Macho", "Sal-Pimienta", "Alta", 16),
                Mascota("Pinguino", "Perro", "Chihuahua", 3, "Macho", "Pinto", "Tremendo", 20),
                Mascota("Roy", "Hamster", "Sirio", 11, "Macho", "Blanco", "Competitiva", 3),
                Mascota("El Loco Bily", "Pez de agua dulce", "Carpa Dorada", 5, "Macho", "Dorado", "Alterada", 10)]

        salida_esperada = [Mascota("Chester", "Perro", "French Poodle", 11, "Macho", "Blanco", "Indescriptible", 15),
                   Mascota("Max", "Perro", "Schnauzer", 1, "Macho", "Sal-Pimienta", "Alta", 16),
                   Mascota("Pinguino", "Perro", "Chihuahua", 3, "Macho", "Pinto", "Tremendo", 20),
                   Mascota("Roy", "Hamster", "Sirio", 11, "Macho", "Blanco", "Competitiva", 3),
                   Mascota("El Loco Bily", "Pez de agua dulce", "Carpa Dorada", 5, "Macho", "Dorado", "Alterada", 10)]

        dbMock = MagicMock()
        dbMock.mostrar.return_value = entrada

        real = mostrarMascota(dbMock)
        self.assertEqual(salida_esperada, real)

    #test integracion
    def test_integration(self):
        salida_esperada = [Mascota("Chester", "Perro", "French Poodle", 11, "Macho", "Blanco", "Indescriptible", 15),
                        Mascota("Max", "Perro", "Schnauzer", 1, "Macho", "Sal-Pimienta", "Alta", 16),
                        Mascota("Pinguino", "Perro", "Chihuahua", 3, "Macho", "Pinto", "Tremendo", 20),
                        Mascota("Roy", "Hamster", "Sirio", 11, "Macho", "Blanco", "Competitiva", 3),
                        Mascota("El Loco Bily", "Pez de agua dulce", "Carpa Dorada", 5, "Macho", "Dorado", "Alterada", 10)]

        real = mostrarMascota(self.db)
        self.assertEqual(salida_esperada, real)

if __name__ == '__main__':
    unittest.main()