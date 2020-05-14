# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,rmd//Rmd,scripts//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Test API

# First make sure that you have the backend server running: in the `backend` folder, `python run.py`

import requests, json

api = 'http://localhost:5000/'

requests.get(api+'churches').json()

requests.post('http://localhost:5000/churches',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({
                  
                               'postcode': 'L13 7EQ',
                               'name': 'Covenant Family',
                               'website':'covenantfamily.org.uk',
                               'latitude':2.3,
                               'longitude':56.0,
              })).json()   

requests.put('http://localhost:5000/churches/1',
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                               'postcode': 'L13 7EQ',
                               'website':'church.com',
                               'latitude': '2.3',
                               'longitude': '56.0',
                'name': 'walk'
            })).json()

requests.delete('http://localhost:5000/churches/1')
