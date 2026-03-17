def long_workouts(cleanedlist, minutes):
    final= []
    for row in cleanedlist:
        time = row['minutes']
        if time >= minutes:
            final.append(row)
    return final

def high_calorie_workouts(cleanedlist, min_calories):
    final = []
    for row in cleanedlist:
        calories = row['calories']
        if calories >= min_calories:
            final.append(row)

    return final