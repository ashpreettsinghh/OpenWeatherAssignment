# Build Docker Image
```
cd OpenWeatherAssignment
```

```
docker build -t ashpreetSingh-Flask-App .
```

# Run Docker Image

```
docker run -d -p 5000:5000 ashpreetSingh-Flask-App
```



# OpenWeather

API Key - 9c067af5cf2d6e6ac2a40ccf2aaf18d0


This Python server is designed to fetch weather data from OpenWeatherMap API, store it in a database, and provide advanced weather information for a given location. It's containerized using Docker and allows users to trigger the API to fetch weather records.

Requirements

OpenWeatherMap API Key: You'll need to sign up for a free API key from OpenWeatherMap to access their API.
Database System: This implementation uses SQLite to store weather data, but it can be adapted to use other systems like PostgreSQL or MySQL.
Python Backend Server: The server is built using Flask and includes error handling for scenarios such as incorrect city or country codes, API request failures, and database errors.
Docker: The server is containerized using Docker for easy deployment.
Setup

OpenWeatherMap API Key: Once you've obtained your API key from OpenWeatherMap, set it either in the code directly or as an environment variable.
Database Setup: If you're using SQLite, the database file is 'weather_data.db'. For other systems, modify the code to match your database configuration.
Install Dependencies: Use the provided 'requirements.txt' file to install the necessary Python packages.
Run the Server: Use the Dockerfile to build and run the containerized server.
Usage

Triggering API: To fetch weather records, send a POST request to http://127.0.0.1:5000/weather with the city and country code as JSON data. An example Python script Requestjupyter.ipynb is provided to demonstrate this.
Retrieve Stored Records: You can retrieve stored records from the database using the provided 'Requestjupyter.ipynb' file or by directly querying the database. The table 'weather' stores temperature, humidity, description, wind speed, and the date and time of data retrieval.
File Structure

AssignmentWork.py: Contains the Flask server code for fetching weather data and storing it in the database.
Requestjupyter.ipynb: A Jupyter notebook demonstrating how to trigger the API and retrieve stored records.
requirements.txt: Lists the Python package dependencies required for the server.
Dockerfile: Specifies the configuration for containerizing the application.
Submission

Please find the code for this project in the provided ZIP archive or access it through the GitHub repository. Ensure you follow the setup instructions in the README file for proper execution.

