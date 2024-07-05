from numpy.random import randint, randn
from pandas import DataFrame
import streamlit


class MapDashboard:
    def __init__(
        self,
        num_points: int = 1000,
        lat_min: int = 7,
        lat_max: int = 85,
        lon_min: int = -20,
        lon_max: int = -179,
    ):
        self.error = False
        try:
            self.lat_sidebar: tuple = streamlit.sidebar.slider(
                "Latitude", lat_min, lat_max, (lat_min, lat_max)
            )
            self.lon_sidebar: tuple = streamlit.sidebar.slider(
                "Longitude", lon_min, lon_max, (lon_min, lon_max)
            )
            self.data = self.get_data(num_points, self.lat_sidebar, self.lon_sidebar)
        except ValueError:
            streamlit.write("Invalid range selected!")
            self.error = True

    @staticmethod
    def get_data(num_points: int, lat_range: tuple, lon_range: tuple) -> DataFrame:
        lat_choice = randint(*lat_range)
        lon_choice = randint(*lon_range)
        streamlit.write(f"Coordinates around: ({lat_choice}, {lon_choice})")
        return DataFrame(
            randn(num_points, 2) / [50, 50] + [lat_choice, lon_choice],
            columns=["lat", "lon"]
        )

    def show_map(self) -> None:
        try:
            streamlit.map(self.data)
        except AttributeError:
            streamlit.write("Couldn't generate data for given range.")
        else:
            if not self.error:
                streamlit.write("Plotting points on the 🌎")


if __name__ == "__main__":
    MapDashboard().show_map()
