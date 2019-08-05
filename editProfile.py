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

@app.route('/editProfile',methods = ['POST'])
def editProfile():

        if request.method == 'POST':

            payload=request.get_json()
            print(payload)
            for pId in patient.find():

                if payload['pId'] == str(pId['_id']):
                        del payload['pId']
                        patient.update_one({
                                    '_id':pId['_id']
                            },{
                                '$set':{
                                'FirstName':payload['FirstName'],
                                'LastName':payload['LastName'],
                                'phoneno':payload['phoneno'],
                                'email':payload['email']
                                }
                            }
                        )
                        response = jsonify({'status':'save contact'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
            
            response = jsonify({'status':'Not save contact'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response

# fillContact()
    