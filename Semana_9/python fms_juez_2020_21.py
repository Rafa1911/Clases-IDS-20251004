#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Votación de un juez FMS (temporada 2020/2021)
- Puntaje por patrón: 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4
- Escena / Flow / Skills: 0 a 2 (enteros)
- Bono por respuesta en minuto de respuesta: +1 por respuesta
- Veredicto del juez:
    - "Réplica" si |PTB_A - PTB_B| <= 5
    - En otro caso, gana el MC con mayor PTB
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ========= Configuración =========
# Umbral de réplica por juez (temporada 20/21 se usaba 5 puntos por juez)
REPLICA_UMBRAL = 5.0

# Plantillas de rondas. Puedes ajustar "patrones" (cantidad a puntuar por ronda).
# NOTA: Los conteos varían entre sedes/jornadas; aquí lo dejamos editable.
ROUND_TEMPLATES = [
    {"clave": "easy", "nombre": "Easy Mode", "patrones": 12, "bono_respuesta": False},
    {"clave": "hard", "nombre": "Hard Mode", "patrones": 12, "bono_respuesta": False},
    {"clave": "tem1", "nombre": "Temática 1 (ida/vuelta)", "patrones": 8, "bono_respuesta": False},
    {"clave": "tem2", "nombre": "Temática 2 (ida/vuelta)", "patrones": 8, "bono_respuesta": False},
    {"clave": "random", "nombre": "Random Mode", "patrones": 12, "bono_respuesta": False},
    # Minutos de sangre (ida/vuelta). Aquí se puede dar bono +1 por respuesta.
    {"clave": "min_ida", "nombre": "Minuto de Sangre (IDA MC A)", "patrones": 12, "bono_respuesta": True},
    {"clave": "min_vta", "nombre": "Minuto de Sangre (VUELTA MC B)", "patrones": 12, "bono_respuesta": True},
    # Deluxe/Acapella (según sede). Déjalo si quieres evaluarlo por patrones.
    {"clave": "deluxe", "nombre": "Deluxe / Libre", "patrones": 6, "bono_respuesta": False},
]


# ========= Modelo de datos =========
@dataclass
class RoundScore:
    nombre: str
    patrones: int
    bono_respuesta: bool
    patrones_A: List[float] = field(default_factory=list)
    patrones_B: List[float] = field(default_factory=list)
    respuestas_A: int = 0
    respuestas_B: int = 0

    def total_A(self) -> float:
        return sum(self.patrones_A) + (self.respuestas_A if self.bono_respuesta else 0)

    def total_B(self) -> float:
        return sum(self.patrones_B) + (self.respuestas_B if self.bono_respuesta else 0)


@dataclass
class BattleScore:
    mc_A: str
    mc_B: str
    rondas: Dict[str, RoundScore] = field(default_factory=dict)
    escena_A: int = 0
    escena_B: int = 0
    flow_A: int = 0
    flow_B: int = 0
    skills_A: int = 0
    skills_B: int = 0

    def ptb_A(self) -> float:
        base = sum(r.total_A() for r in self.rondas.values())
        extra = self.escena_A + self.flow_A + self.skills_A
        return base + extra

    def ptb_B(self) -> float:
        base = sum(r.total_B() for r in self.rondas.values())
        extra = self.escena_B + self.flow_B + self.skills_B
        return base + extra

    def diff(self) -> float:
        return self.ptb_A() - self.ptb_B()

    def verdict(self) -> str:
        d = abs(self.diff())
        if d <= REPLICA_UMBRAL:
            return "Réplica"
        return f"Gana {self.mc_A}" if self.diff() > 0 else f"Gana {self.mc_B}"


# ========= Utilidades de entrada/validación =========
VALID_PATTERN_SCORES = {x * 0.5 for x in range(0, 9)}  # {0,0.5,1,...,4}

def ask_float_pattern(prompt: str) -> float:
    while True:
        v = input(prompt).strip().replace(",", ".")
        try:
            f = float(v)
            if f in VALID_PATTERN_SCORES:
                return f
            print(f"⚠️ Debe ser uno de {sorted(VALID_PATTERN_SCORES)}")
        except ValueError:
            print("⚠️ Ingresa un número válido (ej: 0, 1.5, 3, 4).")

def ask_int(prompt: str, min_v: int, max_v: int) -> int:
    while True:
        v = input(prompt).strip()
        if v.isdigit():
            i = int(v)
            if min_v <= i <= max_v:
                return i
        print(f"⚠️ Ingresa un entero entre {min_v} y {max_v}.")

def yes_no(prompt: str) -> bool:
    while True:
        v = input(prompt + " [s/n]: ").strip().lower()
        if v in ("s", "si", "sí", "y"):
            return True
        if v in ("n", "no"):
            return False
        print("Responde con s/n.")


# ========= Captura de puntajes =========
def capture_round(round_cfg: dict, mc_A: str, mc_B: str) -> RoundScore:
    nombre = round_cfg["nombre"]
    patrones = round_cfg["patrones"]
    bono = round_cfg["bono_respuesta"]

    print(f"\n--- {nombre} ---")
    # Permitir ajustar cantidad de patrones si el juez lo desea
    print(f"Patrones sugeridos: {patrones}")
    if yes_no("¿Quieres cambiar la cantidad de patrones?"):
        patrones = ask_int("Nueva cantidad de patrones: ", 1, 40)

    rs = RoundScore(nombre=nombre, patrones=patrones, bono_respuesta=bono)

    # Notita para guiar: quién rapea primero
    if "IDA MC A" in nombre:
        print(f"Nota: Este minuto lo inicia {mc_A}.")
    elif "VUELTA MC B" in nombre:
        print(f"Nota: Este minuto lo inicia {mc_B}.")

    for i in range(1, patrones + 1):
        rs.patrones_A.append(ask_float_pattern(f"Patrón {i} {mc_A} (0–4, medios puntos): "))
        rs.patrones_B.append(ask_float_pattern(f"Patrón {i} {mc_B} (0–4, medios puntos): "))

    if bono:
        print("\nBono por respuesta (+1 por respuesta en el minuto de respuesta)")
        rs.respuestas_A = ask_int(f"Respuestas efectivas de {mc_A}: ", 0, 20)
        rs.respuestas_B = ask_int(f"Respuestas efectivas de {mc_B}: ", 0, 20)

    print(f"Subtotal {mc_A} en {nombre}: {rs.total_A():.1f}")
    print(f"Subtotal {mc_B} en {nombre}: {rs.total_B():.1f}")
    return rs


def capture_battle() -> BattleScore:
    print("=== Votación FMS (Juez) — Temporada 2020/21 ===")
    mc_A = input("Nombre MC A: ").strip() or "MC A"
    mc_B = input("Nombre MC B: ").strip() or "MC B"

    battle = BattleScore(mc_A=mc_A, mc_B=mc_B)

    print("\nConfigurar rondas:")
    # Permitir desactivar alguna ronda si no aplica en la jornada
    for rc in ROUND_TEMPLATES:
        usar = yes_no(f"¿Incluir la ronda '{rc['nombre']}'?")
        if usar:
            battle.rondas[rc["clave"]] = capture_round(rc, mc_A, mc_B)

    print("\n— Valoraciones extra: Escena / Flow / Skills (0–2 c/u) —")
    battle.escena_A = ask_int(f"Escena {mc_A}: ", 0, 2)
    battle.flow_A = ask_int(f"Flow {mc_A}: ", 0, 2)
    battle.skills_A = ask_int(f"Skills {mc_A}: ", 0, 2)
    battle.escena_B = ask_int(f"Escena {mc_B}: ", 0, 2)
    battle.flow_B = ask_int(f"Flow {mc_B}: ", 0, 2)
    battle.skills_B = ask_int(f"Skills {mc_B}: ", 0, 2)

    return battle


def print_summary(b: BattleScore):
    print("\n================= RESUMEN DEL JUEZ =================")
    print(f"MC A: {b.mc_A} | MC B: {b.mc_B}")
    print("\nSubtotales por ronda:")
    for rkey, r in b.rondas.items():
        print(f"  - {r.nombre}: {b.mc_A} {r.total_A():.1f}  |  {b.mc_B} {r.total_B():.1f}")
    print("\nValoraciones extra (Escena/Flow/Skills):")
    print(f"  {b.mc_A}: {b.escena_A}+{b.flow_A}+{b.skills_A} = {b.escena_A + b.flow_A + b.skills_A}")
    print(f"  {b.mc_B}: {b.escena_B}+{b.flow_B}+{b.skills_B} = {b.escena_B + b.flow_B + b.skills_B}")
    print("\nPTB Totales:")
    print(f"  {b.mc_A}: {b.ptb_A():.1f}")
    print(f"  {b.mc_B}: {b.ptb_B():.1f}")
    diff = b.diff()
    print(f"\nDiferencia (A - B): {diff:.1f}")
    print(f"Umbral de réplica configurado: {REPLICA_UMBRAL:.1f}")
    print(f"\n→ Veredicto del juez: {b.verdict()}")
    print("====================================================\n")


def main():
    while True:
        battle = capture_battle()
        print_summary(battle)
        if not yes_no("¿Registrar otra batalla?"):
            break


if __name__ == "__main__":
    main()
