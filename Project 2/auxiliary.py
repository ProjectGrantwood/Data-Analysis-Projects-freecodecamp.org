import pandas as pd

# Because the project's requirements ask for all decimals rounded to the nearest tenth.
def nearest_tenth(input):
    return round(input, 1)

def to_percent(input):
    return nearest_tenth(input * 100)

def count_values(series, label):
    return series.value_counts()[label]

def get_percentage(series, label):
    return to_percent(count_values(series, label) / series.size)