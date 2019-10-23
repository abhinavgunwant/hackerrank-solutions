# Solution URL: https://www.hackerrank.com/challenges/ruby-methods-keyword-arguments/forum/comments/233869

def convert_temp(temp, input_scale:, output_scale: 'celsius')
    case input_scale.downcase
    when 'celsius'
        if output_scale.downcase == 'fahrenheit'
            temp * 9/5 + 32
        else
            temp + 273.15
        end

    when 'fahrenheit'
        if output_scale.downcase == 'celsius'
            (temp - 32) * 5/9
        else
            (temp - 32) * 5/9 + 273.15
        end
        
    when 'kelvin'
        if output_scale.downcase == 'celsius'
            (temp - 273.15)
        else
            (temp - 273.15) * 9/5 + 32
        end
    end
end