# import dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    # print goes to terminal
    print("Server received request for 'Home' page...")
    # return goes to API page
    return(
        f"Welcome to my SQL Alchemy API for Hawaii Climate<br/>"
        f"<br/>" 
        f"Available routes:<br/>"
        f"<br/>" 
        f"Precipitation data with dates:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"List of stations and names:<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"List of temperture observations a year from the last data point:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Min, Max. and Avg. temperatures for given start date: (please use 'yyyy-mm-dd' format):<br/>"
        f"/api/v1.0/min_avg_max/<start date><br/>"
        f"<br/>"
        f"Min, Max. and Avg. temperatures for given start date and end date: (please use 'yyyy-mm-dd'/'yyyy-mm-dd'format):<br/>"
        f"/api/v1.0/min_avg_max/<start date>/<end date><br/>"
        )
#################################################
# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipication' page...")
    # create session to link to database
    session= Session(engine)
    # return a list of all Precipitation dates through a query
    results = session.query(Measurement.date, Measurement.prcp).all()
    # close session
    session.close()
    # Convert list of tuples into normal list from day 3 activity 10
    precipitation = list(np.ravel(results))
    # convert list to dictionary
    # https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
    precipitation = {precipitation[i]:precipitation[i +1] for i in range(0, len (precipitation), 2)}
    # jsonify results
    return jsonify(precipitation)
#################################################
# stations route
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    # create session to link to database
    session= Session(engine)
    # query data to get stations list
    results = session.query(Station.station, Station.name).all()
    # close session
    session.close()
    # Convert list of tuples into normal list
    stations = list(np.ravel(results))
    # convert list to dictionary
    stations = {stations[i]:stations[i + 1] for i in range(0, len(stations),2)}
    # jsonify results
    return jsonify(stations)
#################################################
# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'TOBS' page...")
    # create session to link to database
    session= Session(engine)
    # query dates and temperatures for most active station for the last year of data
    # dates from climate notebook is "2016-08-23"
    last_year_date = '2016-08-23'
    most_active = 'USC00519281'
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active).filter(Measurement.date > last_year_date).all()
    # close session
    session.close()
    # return json list of temperature observations for previous year
    return jsonify(results)
#################################################
# min_max_avg_start_date route
@app.route("/api/v1.0/min_avg_max/<start_date>")
# activity 8 day 3
def only_start_date(start_date):
    print("Server received request for 'start_date_only' page...")
    # create session to link to database
    session = Session(engine)
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >=start_date).all()
    session.close()
    # activity 10 day 3
    start_date_list = []
    for min, avg, max in results:
        start_date_dict = {}
        start_date_dict['min_temp'] = min
        start_date_dict["avg_temp"] = avg
        start_date_dict['max_temp'] = max
        start_date_list.append(start_date_dict)
    return jsonify (start_date_list)










if __name__ == "__main__":
    app.run(debug=True)