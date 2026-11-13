import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.servicios import calcular_fuerza

cliente = TestClient(app)


@pytest.mark.parametrize(
    ("contrasena", "fuerza"),
    [
        ("Abcdefghijk", "débil"),
        ("Abcdefghijkl", "débil"),
        ("Abcdefg1!", "débil"),
        ("Abcdefghij1k", "media"),
        ("Abcdefghijklmno1", "media"),
        ("Abcdefghijklmno!", "media"),
        ("Abcdefghijklmn1!", "fuerte"),
    ],
)
def test_calcular_fuerza_segun_longitud_y_caracteres(contrasena, fuerza):
    assert calcular_fuerza(contrasena) == fuerza


def test_api_conserva_campos_y_devuelve_fuerza():
    respuesta = cliente.get(
        "/api/contrasena",
        params={"longitud": 16, "numeros": "true", "simbolos": "true"},
    )

    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert set(datos) == {"contrasena", "longitud", "fuerza"}
    assert datos["longitud"] == 16
    assert datos["fuerza"] == "fuerte"
