from numpy.random import randint, randn
from pandas import DataFrame
import streamlit


class MapDashboard:
    def __init__(
        self,
        num_points: int = 1000,
        lat_min: int = 7,
        lat_max: int = 85,
        lon_min: int = -179,
        lon_max: int = -20,
    ):
        self.error_message = ""
        self.lat_choice = lat_min
        self.lon_choice = lon_min
        try:
            streamlit.sidebar.markdown("## ⚙ Settings")
            self.lat_sidebar: tuple = streamlit.sidebar.slider(
                "Latitude", lat_min, lat_max, (lat_min, lat_max)
            )
            self.lon_sidebar: tuple = streamlit.sidebar.slider(
                "Longitude", lon_min, lon_max, (lon_min, lon_max)
            )
            self.data = self.get_data(
                num_points, self.lat_sidebar, self.lon_sidebar
            )
        except ValueError:
            self.error_message = "Invalid range selected!"
        else:
            if self.error_message == "":
                streamlit.markdown("# Plotting points on the 🌎")
                streamlit.markdown(
                    f"> Coordinates of randomly generated points around: `({self.lat_choice}, {self.lon_choice})`"
                )

    def get_data(self, num_points: int, lat_range: tuple, lon_range: tuple) -> DataFrame:
        self.lat_choice = randint(*lat_range)
        self.lon_choice = randint(*lon_range)
        return DataFrame(
            randn(num_points, 2) / [50, 50] + [self.lat_choice, self.lon_choice],
            columns=["lat", "lon"]
        )

    def show_map(self) -> None:
        try:
            streamlit.map(self.data)
        except AttributeError:
            streamlit.error(f"### ⚠️ Couldn't generate data for given range.\n{self.error_message}")


MapDashboard().show_map()
