import pytest
import funciones

#TEST

#Test Ejercicio 1 Funciones (Suma de digitos)
@pytest.mark.parametrize("num, res",[
    (15,6),
    (25,7),
    (31,4),
    (27,10)
])
def test_add_number(num, res):
    assert funciones.add_number(num) == res

#Test Ejercicio ahorcado (Nombre jugador en guiones)
@pytest.mark.parametrize("player, res",[
    ("messi","_____"),
    ("julian","______"),
    ("neymar","______"),
    ("vini","____")
])
def test_secret_word(player, res):
    assert funciones.secret_word(player) == res

#Test Ejercicio 1 Trabajo Practico Nro5 (Validacion DNI)
@pytest.mark.parametrize("id, res",[
    ("45360353", True),
    ("4640343", True),
    ("433243", False),
    ("194336547",False)
])
def test_validate_ID (id, res):
    assert funciones.validate_ID(id) == res

#Test Ejercicio 2 Trabajo Practico Nro5 (Longitud ultima palabra)
@pytest.mark.parametrize("str, res",[
    ("hola pepe", 4),
    ("soy yo", 2),
    ("pepe pedro  emiliano", 8),
    ("espacio espacio esp", 3)
])
def test_str_length(str, res):
    assert funciones.str_length(str) == res

#Test Ejercicio 4 Trabajo Practico Nro5 (Numero multiplo)
@pytest.mark.parametrize("a,b, res",[
    (15,3,True),
    (25,5,True),
    (18,7,False),
    (29,11,False)
])
def test_multiple_numbers(a,b, res):
    assert funciones.multiple_numbers(a,b) == res