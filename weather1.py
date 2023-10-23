import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Command line : python3 weather2.py ~/Desktop/weatherfiles -e 2005
# Command line : python3 weather2.py ~/Desktop/weatherfiles -c 2005/01
# Command line : python3 weather2.py ~/Desktop/weatherfiles -a 2005/01

def process_weather_data(file_path):
    date_format = '%Y-%m-%d'
    data_list = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)

    highest_temperature = 'Max TemperatureC'
    highest_temperature_index = data_list[0].index(highest_temperature)

    lowest_temperature = 'Min TemperatureC'
    lowest_temperature_index = data_list[0].index(lowest_temperature)

    highest_humidity = 'Max Humidity'
    highest_humidity_index = data_list[0].index(highest_humidity)

    columns_to_check = [
        highest_temperature_index,
        lowest_temperature_index,
        highest_humidity_index
    ]

    data_list = [row for row in data_list if all(row[col] for col in columns_to_check)]

    max_temperature_values = [float(row[highest_temperature_index]) for row in data_list[1:]]
    max_temperature_value = max(max_temperature_values)

    # Find the index of the maximum temperature value
    max_temperature_index = -1
    for idx, row in enumerate(data_list[1:]):
        if float(row[highest_temperature_index]) == max_temperature_value:
            max_temperature_index = idx

    max_temperature_date = datetime.strptime(data_list[max_temperature_index + 1][0], date_format)

    min_temperature_values = [float(row[lowest_temperature_index]) for row in data_list[1:]]
    min_temperature_value = min(min_temperature_values)

    # Find the index of the minimum temperature value
    min_temperature_index = -1
    for idx, row in enumerate(data_list[1:]):
        if float(row[lowest_temperature_index]) == min_temperature_value:
            min_temperature_index = idx

    min_temperature_date = datetime.strptime(data_list[min_temperature_index + 1][0], date_format)

    max_humidity_values = [int(row[highest_humidity_index]) for row in data_list[1:]]
    max_humidity_value = max(max_humidity_values)

    # Find the index of the maximum humidity value
    max_humidity_index = -1
    for idx, row in enumerate(data_list[1:]):
        if int(row[highest_humidity_index]) == max_humidity_value:
            max_humidity_index = idx

    max_humidity_date = datetime.strptime(data_list[max_humidity_index + 1][0], date_format)

    return (max_temperature_value, max_temperature_date,
            min_temperature_value, min_temperature_date,
            max_humidity_value, max_humidity_date)


def process_all_files_in_folder(folder_path, year):
    max_temp_all_files = float('-inf')
    max_temp_date = ''
    min_temp_all_files = float('inf')
    min_temp_date = ''
    max_humidity_all_files = 0
    max_humidity_date = ''

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name:
            file_path = os.path.join(folder_path, file_name)
            (max_temp, max_temp_date_curr,
             min_temp, min_temp_date_curr,
             max_humidity, max_humidity_date_curr) = process_weather_data(file_path)

            if max_temp > max_temp_all_files:
                max_temp_all_files = max_temp
                max_temp_date = max_temp_date_curr

            if min_temp < min_temp_all_files:
                min_temp_all_files = min_temp
                min_temp_date = min_temp_date_curr

            if max_humidity > max_humidity_all_files:
                max_humidity_all_files = max_humidity
                max_humidity_date = max_humidity_date_curr

            if max_temp_all_files is not float('-inf') and min_temp_all_files is not float('inf'):
             return max_temp_all_files, min_temp_all_files, max_humidity_all_files
            else:
             return None

    print('Highest Temperature:', max_temp_all_files, "°C on", max_temp_date)
    print('Lowest Temperature:', min_temp_all_files, "°C on", min_temp_date)
    print('Highest Humidity:', max_humidity_all_files, "% on", max_humidity_date)


def calculate_average_weather_data(folder_path, year, month):
    if month in months:
        month = months[month]
    else:
        print("Invalid month format. Please enter a valid month in the format MM.")
        return

    total_high_temp = 0
    total_low_temp = 0
    total_humidity = 0
    count = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and str(year) in file_name and month in file_name:
            file_path = os.path.join(folder_path, file_name)
            max_temp, _, min_temp, _, humidity, _ = process_weather_data(file_path)

            total_high_temp += max_temp
            total_low_temp += min_temp
            total_humidity += humidity
            count += 1

    if count == 0:
        print("No data found for the given year and month.")
    else:
        average_high_temp = total_high_temp / count
        average_low_temp = total_low_temp / count
        average_humidity = total_humidity / count

        print('Average Highest Temperature:', average_high_temp, "°C")
        print('Average Lowest Temperature:', average_low_temp, "°C")
        print('Average Humidity:', average_humidity, "%")
        


def draw_horizontal_bar_chart(max_temp, min_temp):
    
    max_temp_float = float(max_temp)
    min_temp_float = float(min_temp)
        


    plt.barh(['Max Temperature', 'Min Temperature'],
             [max_temp_float, min_temp_float],
             color=['red', 'blue'])
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Temperature Type')
    plt.title('Highest and Lowest Temperatures')
    plt.show()


months = {
    '01': "Jan", '02': "Feb", '03': "Mar",
    '04': "Apr", '05': "May", '06': "Jun",
    '07': "Jul", '08': "Aug", '09': "Sep",
    '10': "Oct", '11': "Nov", '12': "Dec"
}

