import pandas as pd
import auxiliary as aux

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = aux.nearest_tenth(df[df['sex'] == 'Male']['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = aux.get_percentage(df['education'], 'Bachelors')

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = aux.get_percentage(higher_education['salary'], '>50K')
    lower_education_rich = aux.get_percentage(lower_education['salary'], '>50K')

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # *** The original template function had an initialized None variable named "num_min_workers", presumably to help the learner break down the problem into steps.
    # *** I found it easier to filter the data by those who worked the minimum amount of hours and pass it to an auxiliary function I had written
    # *** for the previous exercise.
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = aux.get_percentage(min_hours_workers['salary'], '>50K')

    # What country has the highest percentage of people that earn >50K?
    # *** I don't want to use my "aux.get_percentage()" function here because it utilizes the "size" attribute of the series provided in the parameters, but...
    # *** I wanted to return a whole series of different percentages instead.
    # *** The series "richest_by_country" was not provided in the freecodecamp template, but part of my solution.
    richest_by_country = aux.to_percent(df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts())
    highest_earning_country_percentage = richest_by_country.max()
    highest_earning_country = richest_by_country.index[richest_by_country == highest_earning_country_percentage][0]

    # Identify the most popular occupation for those who earn >50K in India.
    # *** the value_counts() Series "highest_earning_occupation" is not in the original template, but part of my solution.
    highest_earning_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts()
    top_IN_occupation = highest_earning_occupation.index[highest_earning_occupation == highest_earning_occupation.max()][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }