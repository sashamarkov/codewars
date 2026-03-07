def major_scale(melody):
    notes_order = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    notes = parse_melody(melody)
    if not notes:
        return "No major scale"
    unique_notes = set(notes)
    for root in notes_order:
        if get_major_scale(root, notes_order) == unique_notes:
            return f"{root} major scale"
    return "No major scale"
​
def parse_melody(melody):
    notes, i = [], 0
    invalid = {'E#', 'B#'}
    while i < len(melody):
        if melody[i] not in 'CDEFGAB':
            return None
        note = melody[i] + '#' if i+1 < len(melody) and melody[i+1] == '#' else melody[i]
        if note in invalid:
            return None
        notes.append(note)
        i += 2 if '#' in note else 1
    return notes
​
def get_major_scale(root, notes_order):
    pos = notes_order.index(root)
    scale = []
    for step in [2,2,1,2,2,2,1]:
        scale.append(notes_order[pos % 12])
        pos += step
    return set(scale)
​