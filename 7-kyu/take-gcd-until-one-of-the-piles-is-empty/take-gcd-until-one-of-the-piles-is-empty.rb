def calc(xs)
  total = 0
  while xs.min > 0
    gcd_val = xs.reduce(:gcd)
    qty = gcd_val * xs.min / gcd_val
    total +=  xs.length * qty
    xs = xs.map { |x| x - qty }
  end
  total
end