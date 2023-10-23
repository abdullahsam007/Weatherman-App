import argparse
import os
from weather1 import (
    draw_horizontal_bar_chart,
    process_all_files_in_folder,
    calculate_average_weather_data
)


def main():
    parser = argparse.ArgumentParser(description="Weatherman")
    parser.add_argument("folder_path", help="Path to the folder containing weather data files.")
    parser.add_argument("-e", "--year", type=int, help="Display the highest temperature, lowest temperature, and humidity for a given year.")
    parser.add_argument("-a", "--average", help="Display the average highest temperature, average lowest temperature, and average mean humidity for a given year and month in the format YYYY/MM.")
    parser.add_argument("-c", "--chart", help="Draw horizontal bar charts for the highest and lowest temperature for a given year and month in the format YYYY/MM.")

    args = parser.parse_args()

    if not os.path.exists(args.folder_path):
        print(f"Error: The folder path '{args.folder_path}' does not exist.")
        return

    if args.year:
        process_all_files_in_folder(args.folder_path, args.year)

    if args.average:
        year, month = args.average.split('/')
        if not month.isdigit() or len(month) != 2:
            print("Invalid month format. Please enter a valid month in the format MM.")
            return
        calculate_average_weather_data(args.folder_path, year, month)

    if args.chart:
        year, month = args.chart.split('/')
        if not month.isdigit():
            print("Invalid month format. Please enter a valid month in the format MM.")
            return

        result = process_all_files_in_folder(args.folder_path, year)
        
        if result is not None:
            max_temp_all_files, min_temp_all_files, _ = result
            draw_horizontal_bar_chart(max_temp_all_files, min_temp_all_files)
        else:
            print("No data found for the given year and month.")



if __name__ == "__main__":
    main()
