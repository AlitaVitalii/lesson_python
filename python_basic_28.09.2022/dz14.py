d = {
    "apple": ["malum", "pomum", "popula"],
    "fruit": ["baca", "bacca", "popum"],
    "punishment": ["malum", "multa"]
}

set_values = ()
for v_01 in d.values():
    for v_02 in v_01:
        set_values += [v_02]

print(set_values)
