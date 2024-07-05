import numpy as np
import pandas as pd
import streamlit


def plot_map() -> None:
    streamlit.write("Plotting a Map")
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"]
    )
    streamlit.map(map_data)


def sidebar():


if __name__ == "__main__":
    plot_map()
