def strike(s)
    "<strike>#{s}</strike>"
end

def mask_article(s, arr)
    arr.each do | word |
        # create a RegEx pattern based on the word in array!
        pattern = Regexp.new word
        s = s.gsub(pattern, strike(word))
    end

    return s
end