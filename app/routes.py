from app import app
from flask import render_template, redirect, url_for, session
import html
from app.functions import get_dgcr, gmaps_geolocator, zip_dgcr, zip_gmaps
import requests
import json
from app.forms import CityStateForm, ZipCodeForm
from config import Config


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CityStateForm()
    if form.validate_on_submit():
        session['courses'] = get_dgcr(form.city_field.data, form.state_field.data, form.prox_field.data)
        return redirect(url_for('results'))
    zform = ZipCodeForm()
    if zform.validate_on_submit():
        session['courses'] = zip_dgcr(zform.zip_field.data, zform.zprox_field.data)
        return redirect(url_for('results'))
    return render_template('index.html', title='Home', form=form, zform=zform)

@app.route('/results', methods=['GET'])
def results():
    return render_template('results.html', title='Course Results', results=session['courses'], gmaps_url=Config.GMAPS_URL)