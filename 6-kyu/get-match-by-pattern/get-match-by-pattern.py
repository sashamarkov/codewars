from collections import defaultdict
​
def find_matched_by_pattern(pattern):
    def predicate(word):
        positions = defaultdict(list)
        for i, ch in enumerate(word):
            positions[ch].append(i)
        current_pos = -1
        used_counts = defaultdict(int)
        for ch in pattern:
            if len(positions[ch]) <= used_counts[ch]:
                return False
            next_pos = positions[ch][used_counts[ch]]
            used_counts[ch] += 1
            if next_pos <= current_pos:
                return False
            current_pos = next_pos
        return True
    return predicate