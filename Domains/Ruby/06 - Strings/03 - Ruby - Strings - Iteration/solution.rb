def count_multibyte_char(s)
    count = 0
    s.each_char do |c|
        if c.bytes.size > 1
            count += 1
        end
    end

    return count
end