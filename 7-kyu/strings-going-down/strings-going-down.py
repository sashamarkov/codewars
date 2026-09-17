def vertical(words):
    return "\n".join(" ".join(w[i] if i < len(w) else " " for w in words).rstrip() for i in range(max(map(len, words), default=0)))