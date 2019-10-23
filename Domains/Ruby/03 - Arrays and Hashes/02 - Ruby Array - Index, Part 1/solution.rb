def element_at(arr, index)
    arr.at(index) # or
    # arr[index]
end

def inclusive_range(arr, start_pos, end_pos)
    arr[start_pos..end_pos]
end

def non_inclusive_range(arr, start_pos, end_pos)
    arr[start_pos...end_pos]
end

def start_and_length(arr, start_pos, length)
    arr[start_pos, length]
end