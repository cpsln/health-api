from flask import render_template, request,session,jsonify
import hashlib
from db_config import doctor
from app import app

def loginDoctor():
        @app.after_request
        def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

        @app.route('/login',methods = ['POST', 'GET'])
        def login():
            if request.method == 'POST':
                eml=doctor.find()
                payload=request.get_json()
                # print(payload,"*********")

                for i in eml:
                        if payload["Username"] == i["email"] and payload['Password'] == i['password']:
                            
                                response = jsonify({'DocId':str(i["_id"]),'name':i["Firstname"]+' '+i["Lastname"]})
                                response.headers.add('Access-Control-Allow-Origin', '*')
                                response.headers['Access-Control-Allow-Origin'] = '*'
                                print(response)
                                print(response.headers)
                                return response
                        else:
                                pass
                        
                response = jsonify({'wrong':'worng email/password'})
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers['Access-Control-Allow-Origin'] = '*'
                print(response)
                print(response.headers)
                return response,202    
loginDoctor()
