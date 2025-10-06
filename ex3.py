valores = [
    10,
    3 + 2j,
    1.1,
    "to com fome",
    True,
    False,
    [8, 16, 24],
    {"x": "Valor"},
    (7, 8, 9),
    {6, 5, 4}
]

for valor in valores:
    print(f"Valor: {valor} - Tipo: {type(valor)}")
