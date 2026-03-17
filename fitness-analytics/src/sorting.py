def top_n_calorie_burns(cleanedlist, n):
    sortedlist = sorted(cleanedlist, key = lambda item: item['calories'], reverse = True)
    sortedlist1 = sortedlist[0:n]
    return sortedlist1
        

def top_n_intense_workouts(cleanedlist, n):
    sortedlist = sorted(cleanedlist, key = lambda item: item['calories_per_minute'], reverse = True)
    sortedlist1 = sortedlist[0:n]
    return sortedlist1