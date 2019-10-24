square      = ->(x) { x * x }
plus_one    = ->(x) { x + 1 }
into_2      = ->(x) { x * 2 }
adder       = ->(x, y) { x + y }
values_only = ->(arr) { arr.values }


input_number_1 = gets.to_i
input_number_2 = gets.to_i
input_hash = eval(gets)

a = square.(input_number_1); b = plus_one.(input_number_2);c = into_2.(input_number_1); 
d = adder.(input_number_1, input_number_2);e = values_only.(input_hash)

p a; p b; p c; p d; p e

