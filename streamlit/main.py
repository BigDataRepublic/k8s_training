import streamlit as st
import psycopg2
import os
import pandas as pd
import altair as alt

st.title("ML predictions")

# Connect to the database
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

# Create a cursor
cursor = conn.cursor()

# Perform query.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


table = run_query("SELECT * from predictions;")
pandas_df = pd.DataFrame(table, columns=["id", "label"])

count_per_label = pandas_df.groupby("label").count().reset_index()

c = (
    alt.Chart(count_per_label)
    .mark_bar()
    .encode(
        x="label",
        y="id",
        color="label",
    )
)

st.altair_chart(c, use_container_width=True)

st.info(f"There is a total of {len(pandas_df)} predictions.")

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
