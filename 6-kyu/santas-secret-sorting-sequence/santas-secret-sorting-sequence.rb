def sort(gifts)
  return gifts if gifts.nil? || gifts.length <= 1
  pivot = gifts.first
  left, right = gifts[1..-1].partition { |gift| gift < pivot }
  sort(left) + [pivot] + sort(right)
end