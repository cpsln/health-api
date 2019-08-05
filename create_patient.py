from flask import render_template, request,session,jsonify
# import hashlib

from db_config import doctor,patient
from app import app 


def CreatPatient():
    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

    @app.route('/New_Patient',methods = ['POST'])
    def New_Patient():
        if request.method == 'POST':
 
            payload=request.get_json()
            print(payload,"*******")
            patient.insert_one(payload)   
            
            response = jsonify({'status':'save data'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response

CreatPatient()