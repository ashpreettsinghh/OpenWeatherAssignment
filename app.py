from flask import Flask, request, jsonify
import requests
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///weather_data.db')
Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    description = Column(String)
    wind_speed = Column(Float)
    date_time = Column(DateTime)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@app.route('/all_weather', methods=['GET'])
def get_all_weather():
    print("test")
    try:
        session = Session()
        all_weather = session.query(Weather).all()
        print(all_weather)
        session.close()
        # Format the queried data for response
        weather_data = []
        for weather in all_weather:
            weather_data.append({
                'id': weather.id,
                'city': weather.city,
                'country': weather.country,
                'temperature': weather.temperature,
                'humidity': weather.humidity,
                'description': weather.description,
                'wind_speed': weather.wind_speed,
                'date_time': str(weather.date_time)
            })

        return jsonify(weather_data)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')
    country = data.get('country')

    api_key = '9c067af5cf2d6e6ac2a40ccf2aaf18d0'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        
        # Check the status code and log the content for further investigation
        if response.status_code != 200:
            return jsonify({'error': f'Request failed with status code {response.status_code}'})
        
        weather_data = response.json()
        
        # Log the content of the weather data
        print(weather_data)
        
        # Extract required weather data
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']

        # Store data in the database
        session = Session()
        new_weather = Weather(city=city, country=country, temperature=temperature, humidity=humidity, description=description, wind_speed=wind_speed, date_time=datetime.now())
        
        session.add(new_weather)
        session.commit()
        session.close()

        return jsonify({'message': 'Weather data stored successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)