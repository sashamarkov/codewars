from decimal import Decimal
​
def mant_exp(a_number, digits_number):
    d = a_number if isinstance(a_number, Decimal) else Decimal(str(a_number))
    exponent = d.adjusted() - (digits_number - 1)
    mantis = int(d.scaleb(-exponent))
    return f'{str(mantis).ljust(digits_number, "0")}P{exponent}'