import re
​
CALORIES_PER_GRAM_PROTEIN = 4
CALORIES_PER_GRAM_CARBS = 4
CALORIES_PER_GRAM_FAT = 9
​
​
def bulk(arr):
    total_protein = 0.0
    total_calories = 0.0
    for meal in arr:
        for weight, name in re.findall(r'(\d+)g\s+([A-Za-z]+)', meal):
            p, c, f = food[name]
            factor = int(weight) / 100.0
            total_protein += p * factor
            total_calories += (
                p * CALORIES_PER_GRAM_PROTEIN
                + c * CALORIES_PER_GRAM_CARBS
                + f * CALORIES_PER_GRAM_FAT
            ) * factor
​
    def fmt(x):
        s = f"{round(x, 2):.2f}".rstrip('0').rstrip('.')
        return s if s else "0"
​
    return f"Total proteins: {fmt(total_protein)} grams, Total calories: {fmt(total_calories)}"