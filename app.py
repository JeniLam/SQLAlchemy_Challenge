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
        f"/api/v1.0/min_max_avg_start_date_only<br/>"
        f"<br/>"
        f"Min, Max. and Avg. temperatures for given start date and end date: (please use 'yyyy-mm-dd' format):<br/>"
        f"/api/v1.0/min_max_avg_start_date_and_end_date<br/>"
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
    session.close
    # Convert list of tuples into normal list from day 3 activity 10
    precipitation = list(np.ravel(results))
    # convert list to dictionary
    # https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
    precipitation = {precipitation[i]:precipitation[i +1] for i in range(0, len (precipitation), 2)}
    # jsonify results
    return jsonify(precipitation)
    

if __name__ == "__main__":
    app.run(debug=True)