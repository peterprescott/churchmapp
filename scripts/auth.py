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

# # Test Authentication and JWT validation

# ## Use `requests` to engage with the API

import requests, json

# First make sure backend server is running: from `backend` folder, run `python run.py`

API = 'http://localhost:5000/'

requests.get(API).text

# ## Authentication should give you back a JSON Web Token

jimmy = requests.post(API+'auth',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({
                               'email':'jimmy' ,
                               'password': 'strawberry',
              })).json()   

jimmy

jam = requests.post(API+'auth',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({
                               'email':'jam' ,
                               'password': 'strawberry',
              })).json()   

jam

requests.post(API+'auth',
              headers={
                  'JWT': jwt,
                  'Content-Type': 'application/json'},
                data=json.dumps({
                                       'email':'jam' ,
                                       'password': 'strawberry',
                }
                )
              ).json()   

# ## Valid JWT necessary to post new place

requests.post(API+'places',
              headers={
                  'JWT': jam['JWT'],
                  'Content-Type': 'application/json'},
                data=json.dumps({
                                       'postcode': 'L1 4BS',
                                        'latitude': '3.1',
                                        'longitude': '5.6',
                                        'name': 'strawberry place'
                }
                )
              ).json()   

requests.post(API+'places',
              headers={
                  'JWT': jimmy['JWT'],
                  'Content-Type': 'application/json'},
                data=json.dumps({
                                       'postcode': 'L1 4BS',
                                        'latitude': '3.1',
                                        'longitude': '5.6',
                                        'name': 'jimmys house'
                }
                )
              ).json()   

# ## User can only `get` their own places, and only with valid JWT

requests.get(API+'places',
            headers={'JWT':jwt}).json()

requests.get(API+'places',
            headers={'JWT':jimmy['JWT']}).json()

requests.get(API+'places',
            headers={'JWT':jam['JWT']}).json()

# ## User can only `delete` their own places, and only with valid JWT

# +
deletion = requests.delete(API+f'places/13', headers={'JWT':jam['JWT']})

deletion.status_code
# -

deletion = requests.delete(API+f'places/13', headers={'JWT':jimmy['JWT']})
deletion.status_code

requests.get(API+'places',
            headers={'JWT':jimmy['JWT']}).json()

requests.get(API+'places',
            headers={'JWT':jam['JWT']}).json()
