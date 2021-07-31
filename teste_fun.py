import pytest
from multi import NumMulti

class TestMultiplo:
    def setup(self):
        pass

    def test_mul(self):
        resultado = NumMulti(70)

        assert resultado == 'fizzbuzz'

    def test_mul1(self):
        resultado = NumMulti(15)

        assert resultado == 'fizz'

    def test_mul2(self):
        resultado = NumMulti(21)

        assert resultado == 'buzz'

    def test_mul3(self):
        resultado = NumMulti(12)

        assert resultado == 'miss'
