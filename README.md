# SQLAlchemy_Challenge

Climate analysis on Honolulu, Hawaii

## Climate Analysis and Exploration
- Utilized Python and SQLAlchemy to perform a basic climate analysis and data exploration of a climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- Chosen start date and end date for analysis February 10 - 20, 2018
- Utilized SQLAlchemy create_engine to connect to your sqlite database. SQLAlchemy automap_base() to reflect tables into classes and saved a reference to those classes called Station and Measurement.

### Precipitation Analysis

- Designed a query to retrieve the last 12 months of precipitation data and selected only the date and prcp values.
- Loaded the query results into a Pandas DataFrame and set the index to the date column.
- Sorted the DataFrame values by date.
- Utilized MatPlotLib and placed results into a bar graph using the DataFrame plot method.
- Applied Pandas to print the summary statistics for the precipitation data.


### Station Analysis

- Designed a query to calculate the total number of stations as well as find the most active stations listing said stations and observation counts in descending order.
- Designed a query to retrieve the last 12 months of temperature observation data (TOBS) and filtered by the station with the highest number of observations.
- Applied MatPlotLib to place the results into histogram with bins=12.



## Climate App
After initial analysys designed a Flask API based on the queries above.

 - Employed Flask to create the following routes which return a JSON list of requested data:
    * Home page which lists all available routes
    * Precipitation
    * Stations
    * Temperatures
    * Min, Max and Average temps for given start date
    * Min, Max and Average temps for given start date and end date

### Temperature Analysis I
(Additional query challenges)

- Utilized Jupyter Notebook annd Pandas to measure if there is a meaningful difference between the temperature in, for example, June and December
- Identified the average temperature in June & December at all stations across all available years in the dataset. 
- Utilized a unpaired t-test to determine whether the difference in the means, if any, is statistically significant. Unpaired t-test was chosen over a paired t-test as the means are from seperate groups and are not dependent on each other.
- Null Hypothesis: The difference between the mean temperatures of June and December is equal to zero
- Hypothesis: The difference between the mean temperatures of June and December is NOT equal to zero
- The pvalue was lower than .05 which implies the means of the two datasets are not statistically significant.

### Temperature Analysis II

- Used a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. and will return the minimum, average, and maximum temperatures for a range of dates.  In this case, I utlized February 10 - 20, 2018.
- Ploted the min, avg, and max temperature from your previous query as a bar chart using MatPlotLib. Used the average temperature as the bar height and the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

### Daily Rainfall Average

- Calculated the rainfall per weather station using the previous year's matching dates.
- Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures using a function called daily_normals. This function calculates the daily normals for a specific date. This date string will be in the format %m-%d. 
- Created a list of dates for your trip in the format %m-%d and used the daily_normals function to calculate the normals for each date string and appended the results to a list.
- Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
- Utilized Pandas (MatPlotLib) to plot an area plot (stacked=False) for the daily normals.


Copyright
Trilogy Education Services © 2020. All Rights Reserved.
