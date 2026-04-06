import re
​
def calculate(price_dict, transaction):
    stacks = {item: [] for item in price_dict}
    for match in re.finditer(r'(-?\d+)([A-Z])|([A-Z])', transaction):
        if match.group(3):
            item = match.group(3)
            if stacks[item]:
                stacks[item].pop()
        else:
            item = match.group(2)
            stacks[item].append(int(match.group(1)))
    return sum(sum(stack) * price_dict[item] for item, stack in stacks.items())