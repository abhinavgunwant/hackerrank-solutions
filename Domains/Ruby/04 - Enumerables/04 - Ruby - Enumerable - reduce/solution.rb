def sum_terms(n)
    return (1..n).map{ |x| x**2 + 1}.reduce(0, :+)
end