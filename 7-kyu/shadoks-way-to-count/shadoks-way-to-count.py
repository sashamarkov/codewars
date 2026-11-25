def shadok(n:int) -> str:
    s = ["GA", "BU", "ZO", "MEU"]
    return s[n] if n < 4 else shadok(n // 4) + s[n % 4]