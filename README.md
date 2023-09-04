# Migration from HK Estimator

This Python script retrieves and analyzes daily passenger traffic data from the Hong Kong Immigration Department's open data portal. It calculates the estimated migration from Hong Kong based on the number of arrivals and departures of Hong Kong residents through the airport.

## Requirements

- Python 3.x
- pandas
- requests
- matplotlib

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:
pip install pandas requests matplotlib

scheme
Copy

## Usage

Run the script using the following command:

```
python migration_estimator.py [-d show_detail] [-f freq]
```

Optional arguments:
- `-d, --detail`: Input 'y' to show the arrival and departure numbers. Default is 'n'.
- `-f, --frequency`: Set the frequency for plotting. Default is 'M' (monthly). Other options include 'D' (daily), 'W' (weekly), and 'Q' (quarterly).

Example usage:
```
python migration_estimator.py -d y -f W
```

The script will fetch the data, clean it, calculate the estimated migration, and plot the results based on the specified frequency.

## Data Source

The script retrieves the daily passenger traffic data from the Hong Kong Immigration Department's open data portal. The data is obtained from the following URL:

[https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/statistics_on_daily_passenger_traffic.csv ↗](https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/statistics_on_daily_passenger_traffic.csv)

## License

This project is licensed under the [MIT License](LICENSE).
