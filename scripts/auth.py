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

# +
import requests, json

API = 'http://localhost:5000/'
# -

requests.post(API+'register',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({
                               'email':'jack' ,
                               'password': 'white',
              })).json()   

auth = requests.post(API+'auth',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({
                               'email':'jack' ,
                               'password': 'white',
              })).json()   

jwt = auth['JWT']

jwt

requests.post(API+'validate',
              headers={
                  'JWT': jwt,
                  'Content-Type': 'application/json'},
              ).json()   
