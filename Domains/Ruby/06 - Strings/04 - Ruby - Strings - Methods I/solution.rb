def process_text(sArr)
    newArr = []

    sArr.each do | s |
        newArr.push(s.strip)
    end

    return newArr.join(' ')
end