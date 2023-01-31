import altair as alt
import pandas as pd
import streamlit as st


class Visualizations:
    def __init__(self, data: list):
        self.data = data

    def show_chart(self):
        pandas_df = pd.DataFrame(self.data, columns=["id", "label"])
        count_per_label = pandas_df.groupby("label").count().reset_index()
        chart = (
            alt.Chart(count_per_label)
            .mark_bar()
            .encode(
                x="label",
                y="id",
                color="label",
            )
        )
        st.title("Predictions 🚀🚀🚀")
        st.altair_chart(chart, use_container_width=True)
        st.info(f"There is a total of {len(pandas_df)} predictions.")
