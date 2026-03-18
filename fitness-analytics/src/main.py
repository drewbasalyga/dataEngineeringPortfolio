from cleaner import cleaner
from aggregations import total_calories_by_exercise, total_minutes_by_date
from filters import long_workouts, high_calorie_workouts
from sorting import top_n_calorie_burns, top_n_intense_workouts

def main():
    cleanedlist = cleaner("C:\Users\dbasalyga\Downloads\workouts.csv")

    calsbyexercise = total_calories_by_exercise(cleanedlist)
    total_minutes = total_minutes_by_date(cleanedlist)
    longworkouts = long_workouts(cleanedlist, 40)
    highcalorie = high_calorie_workouts(cleanedlist, 500)
    topburns = top_n_calorie_burns(cleanedlist, 2)
    intenseworkouts = top_n_intense_workouts(cleanedlist, 2)

    print("Calories by exercise:", calsbyexercise)
    print("Minutes by date:", total_minutes)
    print("Long workouts:", longworkouts)
    print("High calorie workouts:", highcalorie)
    print("Top calorie burns:", topburns)
    print("Most intense workouts:", intenseworkouts)

if __name__ == "__main__":
    main()
