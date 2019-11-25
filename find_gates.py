def get_minimum_gates(arrive, departure):
    sort_departure = sorted(departure)
    length = len(arrive)
    arrival_index = 0
    departure_index = 0
    max_gate = 0
    current_gate = 0

    while arrival_index < length:
        if arrive[arrival_index] < departure[departure_index]:
            current_gate += 1
            arrival_index += 1
        else:
            current_gate = max(current_gate - 1, 0)
            departure_index += 1
        max_gate = max(current_gate, max_gate)

    return max_gate


arr = [60, 100, 110, 120, 135, 240]
dep = [70, 180, 140, 150, 195, 360]
print(get_minimum_gates(arr, dep))
