from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route("/")
def home_view () :
    return render_template( "base.html" )

@app.route( "/translate" )
def temp_view () :
    return render_template( "bootstrap.html" ) 

@app.route( "/bootstrap" )
def bootstrap () :
    return render_template( "bootstrap.html" ) 
