from app import app
from flask import render_template, redirect, url_for, session
from app.functions import get_dgcr, gmaps_geolocator
import requests
import json
from app.forms import CityStateForm
from config import Config


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CityStateForm()
    if form.validate_on_submit():
        session['courses'] = get_dgcr(form.city_field.data, form.state_field.data)
        return redirect(url_for('results'))
    return render_template('index.html', title='Home Page', form=form)

@app.route('/results', methods=['GET'])
def results():
    return render_template('results.html', title='Course Results', results=session['courses'], gmaps_url=Config.GMAPS_URL)