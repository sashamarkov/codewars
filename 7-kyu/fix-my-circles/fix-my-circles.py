import re
​
def circle_mender(content: str) -> str:
    return re.sub(
        r'(?<=#)[^#\n]*(?=#)',
        lambda m: '#' * len(m.group()),
        content
    )