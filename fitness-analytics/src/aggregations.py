def total_calories_by_exercise(cleanedlist):
    newdict = {}
    for row in cleanedlist:
        exercise = row['exercise']
        calories = row['calories']
        if exercise not in newdict:
            newdict[exercise] = calories
        else:
            newdict[exercise] +=calories
    return newdict

def total_minutes_by_date(cleanedlist):
    newdict = {}
    for row in cleanedlist:
        date = row['date']
        minutes = row['minutes']
        if date not in newdict:
            newdict[date] = minutes
        else:
            newdict[date] += minutes

    
    return newdict
