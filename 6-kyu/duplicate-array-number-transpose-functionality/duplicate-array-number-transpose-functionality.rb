def my_transpose(a)
  return nil if a.nil?
  raise ArgumentError, "Uh Oh!" unless a.is_a?(Array)
  return [] if a.empty?
  raise TypeError, "Uh Oh!" unless a.all? { |sub| sub.is_a?(Array) && !sub.nil? }
  raise IndexError, "Uh Oh!" unless a.map(&:length).uniq.size == 1
  
  a.first.length.times.map { |i| a.map { |row| row[i] } }
end