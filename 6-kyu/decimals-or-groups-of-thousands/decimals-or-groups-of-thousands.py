import re
from decimal import Decimal
​
NUM_RE = re.compile(r'^(\d{1,3}(?:[.,]\d{3})*|\d+)(?:[.,](\d{1,2}))?$')
​
def parse_number(s: str) -> Decimal:
    m = NUM_RE.match(s.strip())
    if not m:
        raise ValueError(f"Bad number: {s!r}")
    int_part, frac_part = m.groups()
    int_str = re.sub(r'[.,]', '', int_part)
    return Decimal(f"{int_str}.{frac_part or '0'}")
​
def sum_up_numbers(numbers):
    total = sum(parse_number(n) for n in numbers)
    return f"{total.quantize(Decimal('0.01')):,}"