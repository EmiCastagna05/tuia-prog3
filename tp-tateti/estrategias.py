"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import math
import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")

    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """

    def MinMaxMax(tateti: Tateti, estado):
        if tateti.test_terminal(estado):
            return tateti.utilidad(estado, JUGADOR_MAX)

        valor = -math.inf

        for accion in  tateti.acciones(estado):
            sucesor = tateti.resultado(estado, accion)
            valor = max(valor, MinMaxMin(tateti, sucesor))
        return valor

    def MinMaxMin(tateti: Tateti, estado):
        if tateti.test_terminal(estado):
            return tateti.utilidad(estado, JUGADOR_MAX)
        
        valor = math.inf

        for accion in  tateti.acciones(estado):
            sucesor = tateti.resultado(estado, accion)
            valor = min(valor, MinMaxMax(tateti, sucesor))
        return valor

    def MinMax(tateti: Tateti, estado):
        if tateti.jugador(estado) == JUGADOR_MAX:
            sucesor = {accion: MinMaxMin(tateti, tateti.resultado(estado, accion))
                        for accion in tateti.acciones(estado)}
            return max(sucesor, key=sucesor.get)

        if tateti.jugador(estado) == JUGADOR_MIN:
            sucesor = {accion: MinMaxMax(tateti, tateti.resultado(estado, accion))
                        for accion in tateti.acciones(estado)}
            return min(sucesor, key=sucesor.get)

    return MinMax(tateti, estado)
