import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    DGCR_KEY = # sign up for an API key at DGCourseReview.com
    DGCR_SIG = # sign up for an API key at DGCourseReview.com
    DGCR_URL = 'https://www.dgcoursereview.com/api/?key={key}&mode=near_rad&lat={lat}&lon={lng}&limit=25&rad=25&sig={sig}'

    GGL_KEY = # sign up for an API key at cloud.google.com/maps-platform/
    GGL_URL = "https://maps.googleapis.com/maps/api/geocode/json?address={place},+{state}&key={key}"

    GMAPS_URL = 'https://www.google.com/maps/search/?api=1&query={lat},+{lng}'

    STATES = [('AL', 'Alabama'),
              ('AK', 'Alaska'),
              ('AZ', 'Arizona'),
              ('AR', 'Arkansas'),
              ('CA', 'California'),
              ('CO', 'Colorado'),
              ('CT', 'Connecticut'),
              ('DE', 'Delaware'),
              ('FL', 'Florida'),
              ('GA', 'Georgia'),
              ('HI', 'Hawaii'),
              ('ID', 'Idaho'),
              ('IL', 'Illinois'),
              ('IN', 'Indiana'),
              ('IA', 'Iowa'),
              ('KS', 'Kansas'),
              ('KY', 'Kentucky'),
              ('LA', 'Louisiana'),
              ('ME', 'Maine'),
              ('MD', 'Maryland'),
              ('MA', 'Massachusetts'),
              ('MI', 'Michigan'),
              ('MN', 'Minnesota'),
              ('MS', 'Mississippi'),
              ('MO', 'Missouri'),
              ('MT', 'Montana'),
              ('NE', 'Nebraska'),
              ('NV', 'Nevada'),
              ('NH', 'New Hampshire'),
              ('NJ', 'New Jersey'),
              ('NM', 'New Mexico'),
              ('NY', 'New York'),
              ('NC', 'North Carolina'),
              ('ND', 'North Dakota'),
              ('OH', 'Ohio'),
              ('OK', 'Oklahoma'),
              ('OR', 'Oregon'),
              ('PA', 'Pennsylvania'),
              ('RI', 'Rhode Island'),
              ('SC', 'South Carolina'),
              ('SD', 'South Dakota'),
              ('TN', 'Tennessee'),
              ('TX', 'Texas'),
              ('UT', 'Utah'),
              ('VT', 'Vermont'),
              ('VA', 'Virginia'),
              ('WA', 'Washington'),
              ('WV', 'West Virginia'),
              ('WI', 'Wisconsin'),
              ('WY', 'Wyoming'),
              ('DC', 'District of Columbia')]