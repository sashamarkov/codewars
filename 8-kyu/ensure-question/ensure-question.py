def ensure_question(s):
    return s + "?" if (not s or s[-1] != "?") else s