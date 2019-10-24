def rot13(secret_messages)
    strArr = []
    
    secret_messages.each do | s |
        s_ = s.each_byte.to_a.map {
            | char |
            if char.chr == '!' || char.chr == ' '
                char.chr
            elsif /[A-Z]/.match(char.chr)
                char = (65 + ((char - 65) + 13) % 26).chr
            else
                char = (97 + ((char - 97) + 13) % 26).chr
            end
        }.join
        strArr.push(s_)
    end
    
    return strArr
end