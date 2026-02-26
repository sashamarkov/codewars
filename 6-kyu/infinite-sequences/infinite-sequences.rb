def sequence(&block)
  Enumerator.new { |seq| (0..).each { |n| seq << block.call(n) } }
end