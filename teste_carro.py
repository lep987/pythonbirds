from unittest import TestCase
from Carrozin import motor
from Carrozin import direção
class CarrroTeste(TestCase):
    def teste_vel(self):
        Motor = motor
        motor.fre()
        self.assertEqual(0, motor.vel)

    def teste_acel(self):
        Motor = motor
        Motor.acel()
        self.assertEqual(1, motor.vel)
