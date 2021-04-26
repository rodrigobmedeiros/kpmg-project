# Mean Car Value API
___

This project implements a API that consumes a dataset containing information on car sales. The main objective is obtain use endpoints to obtain mean car values per manufacturer and cities.

## Getting Started
___

### Pre-requisites and Local Development

For local use, it's necessary to have python3 and pip installed. All required packages are included in the requirements file. To run the application run following commands:

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
*commands considering windows environment for unix use export instead of set*

These commands put the application in development and directs our application to use the app.py into the working directory. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.
The application is run on `http://127.0.0.1:5000/` by default.

### Pre-requisites and docker

To run this project as a docker container, it's necessary to have docker installed, to install it correctly see this link with de orginal [documentarion](https://www.docker.com/).
Use the dockerfile to create an image and a container to run the application. To do this, follow the commands listed below:

```
docker build -t myImage .

docker run --name myContainer -p myPort:5000 myImage
```

To access the application, use the default host with the defined port.

```
http://127.0.0.1:myPort/
```

Considering the commands above, correctly fill in the following parameters:
- myImage - define a name for the image created based on the dockerfile.
- myPort - define a specific port to connect with the application port running inside the container.

Remember to run docker commands inside work directory containing the dockerfile. The url can be used directly in the browser or inside other local applications.

## API Rerefence
___

### Getting Started

- Base URL: Running locally the base url is `https://127.0.0.1:5000/`, running docker container the base url is `https://127.0.0.1:myPort` where myPort is the mapped port defined on the container creation.

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

The API will return two errors types when requests fail:
- 400: Bad Request
- 404: Resource Not Found

### Endpoints

#### GET /mean-values-per-manufacturer

- General:
    - Returns a list of manufacturers, success value and mean car value per manufacturer.
- Sample: `https://127.0.0.1:5000/mean-values-per-manufacturer`
```
{
  "manufacturer_mean_values": [
    {
      "car_make": "A", 
      "mean_car_value": 46144.93
    }, 
    {
      "car_make": "B", 
      "mean_car_value": 50383.38
    }, 
    {
      "car_make": "C", 
      "mean_car_value": 48890.29
    }, 
    {
      "car_make": "D", 
      "mean_car_value": 50650.46
    }, 
    {
      "car_make": "E", 
      "mean_car_value": 49621.39
    }, 
    {
      "car_make": "F", 
      "mean_car_value": 46137.7
    }, 
    {
      "car_make": "G", 
      "mean_car_value": 46113.37
    }, 
    {
      "car_make": "H", 
      "mean_car_value": 46126.33
    }, 
    {
      "car_make": "I", 
      "mean_car_value": 45487.54
    }, 
    {
      "car_make": "J", 
      "mean_car_value": 47992.98
    }
  ], 
  "success": true
}
```

#### GET /mean-values-per-manufacturer/< manufacturer >

- General:
    - Returns the passed manufacturer, success value and mean car value.
- Sample: `https://127.0.0.1:5000/mean-values-per-manufacturer/A`
    
```
{
  "manufacturer": "A", 
  "mean_value": 46144.93, 
  "success": true
}
```

#### GET /mean-values-per-city

- General:
    - Returns a list of cities, success value and mean car value per manufacturer.
- Sample: `https://127.0.0.1:5000/mean-values-per-city`
```
{
  "city_mean_values": [
    {
      "car_make": "C_04", 
      "mean_car_value": 47865.87
    }, 
    {
      "car_make": "C_07", 
      "mean_car_value": 48582.94
    }, 
    {
      "car_make": "C_05", 
      "mean_car_value": 48332.38
    }, 
    {
      "car_make": "C_01", 
      "mean_car_value": 47869.25
    }, 
    {
      "car_make": "C_03", 
      "mean_car_value": 47706.18
    }, 
    {
      "car_make": "C_06", 
      "mean_car_value": 47592.42
    }, 
    {
      "car_make": "C_02", 
      "mean_car_value": 46464.67
    }
  ], 
  "sucess": true
}
```

#### GET /mean-values-per-city/< city >

- General:
    - Returns the passed city, success value and mean car value.
- Sample: `https://127.0.0.1:5000/mean-values-per-manufacturer/C_02`
    
```
{
  "city": "C_02", 
  "mean_value": 47865.87, 
  "success": true
}
```

## Documentation

To access this documentation just access de `/` endpoint.
- `https://127.0.0.1:5000` (local)
- `https://127.0.0.1:myPort` (docker container)

## Authors

Rodrigo Bernardo Medeiros