class Num
  DIGITS = %w[zero one two three four five six seven eight nine]
  
  def initialize(value = 0)
    @value = value
  end
  
  def to_i
    @value
  end
  
  DIGITS.each_with_index do |name, digit|
    define_singleton_method(name) { new(digit) }
    define_method(name) { self.class.new(@value * 10 + digit) }
  end
end