import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
import argparse

URL = 'https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/statistics_on_daily_passenger_traffic.csv'


def loadData(url):
    response = requests.get(url)

    data = StringIO(response.text)
    df = pd.read_csv(data)

    df.rename(columns = {'ï»¿Date':'Date'}, inplace = True)
    df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")
    return df


def cleanData(df, detail):
    # Remove irrelevant data
    # Exclude people other than Hong Kong Residents
    df = df[["Date","Control Point", "Arrival / Departure", "Hong Kong Residents"]]

    # Only rows of travelling through Airport, sorted by date, group by Arrival / Departure
    df = df[df["Control Point"]=="Airport"]

    # Sort by date
    df.sort_values(by='Date', inplace = True)

    # Group by Arrival / Departure
    df.groupby(["Arrival / Departure"])

    # Reshaping: everyday's Arrival and Departure as separate columns next to each other
    df = df.pivot(index="Date",columns="Arrival / Departure", values="Hong Kong Residents")
    df['Estimated migration from HK'] = df['Departure'] - df['Arrival']

    if detail == 'n':
        df = df[["Estimated migration from HK"]]

    return df


def main():
    df_loaded = loadData(URL)

     # create parser object
    parser = argparse.ArgumentParser(description = "Migration from HK Estimator")

    # defining arguments for parser object
    parser.add_argument("-d", "--detail", type = str, nargs = 1,
                        metavar = "show_detail", default = 'n', choices=['y','n'],
                        help = "Input 'y' to show the arrival and departure numbers. Default as 'n'")

    parser.add_argument("-f", "--frequency", type = str, nargs = 1,
                        metavar = "freq", default = 'M', choices=['M', 'Q', 'W', 'D'],
                        help = "Set the frequency. Default as M (monthly). Other options include D (daily), W (Weekly) and Q (quarterly).")
    
    # Parse the arguments from standard input
    args = parser.parse_args()

    # Clean data
    df_cleaned = cleanData(df_loaded, args.detail[0])

    # Set frequency and plot
    df_cleaned.resample(args.frequency[0]).mean().plot()
    
    plt.show()


if __name__ == "__main__":
    # calling the main function
    main()