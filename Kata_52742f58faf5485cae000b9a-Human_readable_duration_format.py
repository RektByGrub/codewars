def format_duration(seconds):

    ## If the value is 0
    if seconds == 0:
        return "now"

    ## Create counters
    return_list = [
        ["year", seconds // 31536000],
        ["day", seconds % 31536000 // 86400],
        ["hour", seconds % 31536000 % 86400 // 3600],
        ["minute", seconds % 31536000 % 86400 % 3600 // 60],
        ["second", seconds % 31536000 % 86400 % 3600 % 60 // 1]
    ]

    ## Remove empties
    clean_list = []
    for item in return_list:
        if item[1] != 0:
            clean_list.append(item)

    ## Assemble return
    try:
        ## Last item
        if clean_list[-1][1] == 1:
            return_string = f"{str(clean_list[-1][1])} {str(clean_list[-1][0])}"
        else:
            return_string = f"{str(clean_list[-1][1])} {str(clean_list[-1][0])}s"

        ## Second to last item
        if clean_list[-2][1] == 1:
            return_string = f"{str(clean_list[-2][1])} {str(clean_list[-2][0])} and {return_string}"
        else:
            return_string = f"{str(clean_list[-2][1])} {str(clean_list[-2][0])}s and {return_string}"

        ## Every other
        for item in reversed(clean_list[:-2]):
            if item[1] == 1:
                return_string = f"{str(item[1])} {str(item[0])}, {return_string}"
            else:
                return_string = f"{str(item[1])} {str(item[0])}s, {return_string}"
    except:
        pass

    return return_string
