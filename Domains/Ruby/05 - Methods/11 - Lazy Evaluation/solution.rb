require 'prime'

palindromicPrimes = ->(n) do
    arr = []
    return Prime.each(Float::INFINITY).lazy.filter {|x| x.to_s == x.to_s.reverse}.first(n)
end

n = gets.to_i
print palindromicPrimes.(n)