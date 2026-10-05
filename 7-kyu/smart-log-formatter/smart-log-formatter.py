from itertools import groupby
​
def smart_log_formatter(logs):
    return [f'{e} (x{n})' if (n:=len([*g])) > 1 else e for e, g in groupby(logs)]