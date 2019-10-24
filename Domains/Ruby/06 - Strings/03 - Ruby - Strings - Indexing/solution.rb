def serial_average(s)
    a = s[4, 5]
    b = s[10, 5]

    avg = (a+b)/2
    return "#{s[0,3]}-#{avg.round(2).to_s.rjust(5, '0')}"
end