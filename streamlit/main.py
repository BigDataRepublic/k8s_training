from visualizations import Visualizations
from database import Database


def main():
    db = Database()
    data = db.run_query("SELECT * from predictions;")
    predictions = Visualizations(data)
    predictions.show_chart()
    db.close_connection()


if __name__ == "__main__":
    main()
