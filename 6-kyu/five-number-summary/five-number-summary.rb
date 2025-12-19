def five_num(array)
  sorted = array.sort.map(&:to_f)
  n = sorted.size
  median = n.odd? ? sorted[n/2] : (sorted[n/2-1] + sorted[n/2]) / 2
  lower = n.odd? ? sorted[0..n/2] : sorted[0...n/2]
  upper = sorted[n/2..-1]
  
  def med(arr)
    m = arr.size
    m.odd? ? arr[m/2] : (arr[m/2-1] + arr[m/2]) / 2
  end
  
  [sorted.first, med(lower), median, med(upper), sorted.last]
end