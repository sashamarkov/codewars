def calculate_improved(students):
    result = []
    for s in students:
        marks = [m if m is not None else 0 for m in s['marks']]
        first = marks[0]
        last = marks[-1]
        if first == 0:
            improvement = 0
        else:
            improvement = round(((last - first) / first) * 100)
        result.append({'name': s['name'], 'improvement': improvement})
    return sorted(result, key=lambda x: (-x['improvement'], x['name']))