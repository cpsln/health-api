from flask import render_template, request,session,jsonify
# from flask_api import status
import hashlib
from db_config import doctor
from app import app
def signupDoctor():
    @app.after_request
    def apply_caching(response):
        response.headers["Content-Type"] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
        return response
    @app.route('/signup',methods = ['POST'])
    def signup():
        if request.method == 'POST':
            payload=request.get_json()
            # payload["Password"] = hashlib.sha256(str.encode(request.form["Password"])).hexdigest()
            # print(payload)
            for i in doctor.find():
                if payload['email'] == i['email']:
                    response = jsonify({'status':'Allready present email'})
                    response.headers.add('Access-Control-Allow-Origin', '*')
                    response.headers['Access-Control-Allow-Origin'] = '*'
                    print(response)
                    print(response.headers)
                    return response,204
                else:
                    pass
            doctor.insert_one(payload)
            response = jsonify({'status':'Signup Success'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            

signupDoctor()  