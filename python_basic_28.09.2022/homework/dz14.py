d = {
    "apple": ["malum", "pomum", "popula"],
    "fruit": ["baca", "bacca", "popum"],
    "punishment": ["malum", "multa"]
}

set_values = set()
for v_01 in d.values():
    for v_02 in v_01:
        set_values.add(v_02)

for i_set in set_values:
    print(f'{i_set.upper()}:')
    for key, values in d.items():
        if i_set in values:
            print(f'- {key}')
