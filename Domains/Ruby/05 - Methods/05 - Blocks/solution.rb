def factorial
    yield
end

n = gets.to_i
factorial do 
    puts (1..n).inject(1) { | product, i | product *= i}
end