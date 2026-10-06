def build_palindrome(s: str) -> str:
    return min((c for k in range(len(s)+1)
                  for c in (s + s[:k][::-1], s[len(s)-k:][::-1] + s)
                  if c == c[::-1]), key=len)