import csv
import requests
import datetime
import time

base_url = "https://api.wheretheiss.at/v1/satellites/25544"

#'a', щоб не перезаписувати файл
with open("location.csv", "a", newline='') as file:
    writer = csv.writer(file)
    
    try:
        while True:
            response = requests.get(url=base_url)#перевірка запиту
            response.raise_for_status()
            data = response.json()

            if 'timestamp' in data and 'latitude' in data and 'longitude' in data: #перевірка потрібних ключів у запиті
                timestamp = datetime.datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
                longitude = data['longitude']
                latitude = data['latitude']
                message = data.get('message', '')#пуста строка, якщо message відсутній

                if file.tell() == 0:
                    writer.writerow(["timestamp", "longitude", "latitude", "message"])
                writer.writerow([timestamp, longitude, latitude, message])
                time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
