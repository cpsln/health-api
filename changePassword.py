from flask import render_template, request,session,jsonify
import hashlib
from db_config import doctor,patient
from app import app
               


@app.after_request
def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

@app.route('/changePassword',methods = ['POST'])
def changePassword():

        if request.method == 'POST':

            payload=request.get_json()
            print(payload)

            for dId in doctor.find():

                if payload['dId'] == str(dId['_id']):
                    if payload['Passwordnew'] == payload['Passwordconf']:
                        doctor.update_one({
                                    '_id':dId['_id']
                            },{
                                '$set':{
                                'password':payload['Passwordnew']
                                }
                            }
                        )
                        response = jsonify({'status':'save password'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                    else:
                        response = jsonify({'status':'password not match'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response,201

            response = jsonify({'status':'Not save password'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response,205


    