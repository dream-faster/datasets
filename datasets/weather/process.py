import pandas as pd
city_name = "Los Angeles"
humidity = pd.read_csv(
    "humidity.csv", delimiter=",", index_col=0, parse_dates=True
)[city_name].rename("humidity")
pressure = pd.read_csv(
    "pressure.csv", delimiter=",", index_col=0, parse_dates=True
)[city_name].rename("pressure")
wind_speed = pd.read_csv(
    "wind_speed.csv", delimiter=",", index_col=0, parse_dates=True
)[city_name].rename("wind_speed")
wind_direction = pd.read_csv(
    "wind_direction.csv",
    delimiter=",",
    index_col=0,
    parse_dates=True,
)[city_name].rename("wind_direction")
temperature = pd.read_csv(
    "temperature.csv",
    delimiter=",",
    index_col=0,
    parse_dates=True,
)[city_name].rename("temperature")
df = (
    pd.concat([humidity, pressure, wind_speed, wind_direction, temperature], axis=1)
    .iloc[1:]
    .ffill()
    # .resample("1D")
    # .last()
)
df.to_csv("weather_la.csv")
