def skip_animals(animals, skip)
    arr = []
    animals[skip..-1].each_with_index do | animal, index|
        arr.push("#{index+skip}:#{animal}")
    end
    return arr
end