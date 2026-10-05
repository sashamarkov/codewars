def find_quarter_notes(time_signature):
    n, d = map(int, time_signature.split('/'))
    if d <= 0 or (d & (d - 1)):
        return None
    return (4 * n) // d