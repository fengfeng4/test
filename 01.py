import requests
import pandas as pd
import sqlite3

class OpenWeatherAPI:
    api_key =None
    row_data = None
    dataframe = None
    def __init__(self, api_key):
        self.api_key = api_key
    def fetch_weather_data(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            self.row_data = response.json()
            self.dataframe = {
                "Location": self.row_data["name"],
                "Temperature (K)": self.row_data["main"]["temp"],
                "Temperature (C)": self.row_data["main"]["temp"]-273.15,
                "Humidity (%)": self.row_data["main"]["humidity"],
                "Weather": self.row_data["weather"][0]["description"]
            }
            self.dataframe = pd.DataFrame([self.dataframe])
            return self.dataframe
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    def to_csv(self, path):
        self.dataframe.to_csv(path, index=False)

def TEXT(name):return (name, " TEXT")
def REAL(name):return (name, " REAL")
def INTEGER(name):return (name, " INTEGER")

class sqlAPI:
    cnct = None
    cursor = None
    column = []
    tableNames = []
    def __init__(self, path):
        self.cnct = sqlite3.connect("data/data.db")
        self.cursor = self.cnct.cursor()
    def CreateTable(self, name, column):
        self.column.append(column)
        self.tableNames.append(name)
        s = "CREATE TABLE IF NOT EXISTS " + name + "("
        for i in self.column:
            s += i[0] + i[1] + ","; 
        s = s[0:-1:1] + ")"
        self.cursor.execute(s)


def csvToDatabase():
    data = pd.read_csv("data/data.csv")
    cnct = sqlite3.connect("data/data.db")
    cursor = cnct.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather(
                location TEXT,
                temperature_k REAL,
                temperature_c REAL,
                humidity INTEGER,
                weather_description TEXT
        )
    ''')
    for idx, row in data.iterrows():
        cursor.execute('''INSERT INTO weather (location, temperature_k, temperature_c, humidity, weather_description)
            VALUES (?, ?, ?, ?, ?)''',
            [(row["Location"]), (row["Temperature (K)"]), (row["Temperature (C)"]), (row["Humidity (%)"]), (row["Weather"])]
        )
    cnct.commit()
    cnct.close()

        
# api = OpenWeatherAPI('2dd249caf078aec871ab451b46fee0a1')
# data = api.fetch_weather_data('Shenzhen')
# api.to_csv("data/data.csv")
# csvToDatabase()

# cnct = sqlite3.connect("data/data.db")
# cursor = cnct.cursor()
# cursor.execute("SELECT * FROM weather")
# data = cursor.fetchall()
# print(data)

# db = sqlAPI("data/data.db")
# db.CreateTable("test",[TEXT("item1"), INTEGER("item2")])d = 

d = {"a":1, "b":2}
print(tuple(d.values())[0])