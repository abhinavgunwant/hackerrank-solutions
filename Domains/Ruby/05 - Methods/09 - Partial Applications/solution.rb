combination = -> (n) do
    -> (r) do
        n_ = (1..n).inject(1) {|product, i| product *= i}
        r_ = (1..r).inject(1) {|product, i| product *= i}
        n_r = (1..(n-r)).inject(1) {|product, i| product *= i}

        n_ /(r_ * n_r)
    end
end

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)

