def group_by_marks(marks, pass_marks)
    marks.group_by {
        | key, value |
        if value >= pass_marks
            "Passed"
        else
            "Failed"
        end
    }
end