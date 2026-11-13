import secrets
import string

SIMBOLOS = "!@#$%&*?-_"


def generar_contrasena(
    longitud: int = 12,
    numeros: bool = True,
    simbolos: bool = False,
) -> str:
    if not 8 <= longitud <= 64:
        raise ValueError("La longitud debe estar entre 8 y 64.")

    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    digitos = string.digits

    grupos_obligatorios = [minusculas, mayusculas]
    if numeros:
        grupos_obligatorios.append(digitos)
    if simbolos:
        grupos_obligatorios.append(SIMBOLOS)

    caracteres = [secrets.choice(grupo) for grupo in grupos_obligatorios]
    alfabeto = "".join(grupos_obligatorios)
    caracteres.extend(
        secrets.choice(alfabeto) for _ in range(longitud - len(caracteres))
    )

    for indice in range(len(caracteres) - 1, 0, -1):
        otro_indice = secrets.randbelow(indice + 1)
        caracteres[indice], caracteres[otro_indice] = (
            caracteres[otro_indice],
            caracteres[indice],
        )

    return "".join(caracteres)
