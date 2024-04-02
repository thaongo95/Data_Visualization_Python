import csv
import matplotlib.pyplot as plt
from datetime import datetime

# ~ filename = 'sitka_weather_07-2014.csv'
# ~ filename = 'sitka_weather_2014.csv'
filename = 'csv_file/death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	highs, mediums, lows, dates = [], [], [], []
	
	for row in reader:
		try: 
			high = int(row[1])
			# ~ medium = row[2]
			low = int(row[3])
			date_now = datetime.strptime(row[0], "%Y-%m-%d")
			# ~ print(high + "-" + low)
		except ValueError:
			print(date_now, "missing data")
		else:
			highs.append(high)
			# ~ mediums.append(medium)
			lows.append(low)
			dates.append(date_now)
	indexs = [index for index, content in enumerate(highs)]
	
	img = plt.figure(figsize=(16, 9))
	plt.plot(dates, highs, c="red", alpha = 0.5, linewidth=2)
	# ~ plt.plot(dates, mediums, c="blue")
	plt.plot(dates, lows, c="blue", alpha = 0.5, linewidth=2)
	plt.fill_between(dates, highs, lows, facecolor='green', alpha= 0.3)
    
	plt.title("Daily high temputeres, July 2014", fontsize=24)
	
	# ~ img.autofmt_xdate()
	# ~ plt.gca().get_yaxis().set_visible(False)
	plt.xlabel("Date", fontsize=16)
	plt.ylabel("Temperture (F)", fontsize=16)
	plt.tick_params(axis='y', color = 'r', labelsize=6)
	plt.tick_params(axis='x', which='minor', labelsize=6)
	plt.show()
