import requests
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

city = 'Hanoi'
url = 'https://api.waqi.info/feed/' + city + '/?token='
api_key = '4cc190163dcd4f2c221c0c635bfa4d4aeeb69fda'

main_url = url + api_key
r = requests.get(main_url)
data = r.json()['data']

aqi = data['aqi']
iaqi = data['iaqi']

for i in iaqi.items():
    print(i[0], ':', i[1]['v'])

dew = iaqi.get('dew','Nil')
no2 = iaqi.get('no2','Nil')
o3 = iaqi.get('o3','Nil')
so2 = iaqi.get('so2','Nil')
pm25 = iaqi.get('pm25', 'Nil')

print(f'{city} AQI :', aqi, '\n')
print('Individual Air quality')
print('Dew : ', dew)
print('NO2 : ', no2)
print('O3 : ', o3)
print('SO2 : ',so2)
print('PM25 : ', pm25)

pollutants = [i for i in iaqi]
values = [i['v'] for i in iaqi.values()]

print(pollutants)
print(values)

explode = [0 for i in pollutants]
mx = values.index(max(values))
explode[mx] = 0.1

# Vẽ biểu đồ thứ nhất
plt.figure(figsize=(12,9))
plt.pie(values, labels = pollutants, autopct='%1.2f%%', shadow = True, explode=explode)
plt.title('Air pollutants and their probable amount in atmosphere [Hanoi]')
plt.axis('equal')
plt.show()

# Vẽ biểu đồ thứ hai
geo = data['city']['geo']
plt.figure(figsize=(10,8))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.stock_img()
plt.scatter(geo[1],geo[0],color = 'blue')
plt.text(geo[1] + 3, geo[0] - 2, f'{city} AQI \n  {aqi}', color = 'red' )
plt.show()


