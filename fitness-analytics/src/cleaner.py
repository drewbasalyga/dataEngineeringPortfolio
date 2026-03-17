def cleaner(inputfile):

    import csv
    import logging
    with open(inputfile, mode = "r", newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        fix_columns = []
        cleaned_list = []
        for row in csv_reader:
            thelist = {}
            
            for key, value in row.items():
                cleanedkey = key.lower().replace(" ", "")
                thelist[cleanedkey] = value
                if cleanedkey == "date":
                    thelist[cleanedkey] = value
                if cleanedkey == "exercise":
                    thelist[cleanedkey] = value if value != "" else "Unknown"
                if cleanedkey == "minutes":
                    try:
                        val = int(value)
                        thelist[cleanedkey] = int(value)
                    except ValueError:
                        thelist[cleanedkey] = 0
                if cleanedkey == "calories":
                    try:
                        val = int(value)
                        thelist[cleanedkey] = int(value)
                    except ValueError:
                        thelist[cleanedkey] = 0
            try:
                thelist['calories_per_minute'] = thelist['calories'] / thelist['minutes']
            except ZeroDivisionError:
                thelist['calories_per_minute'] = 0
            if thelist['exercise'] != "Rest":
                cleaned_list.append(thelist)
        return cleaned_list
