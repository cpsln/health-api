from app import app
from flask import render_template, request,session,jsonify
from db_config import patient

def patientData():
    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response
    @app.route('/PatientData', methods=['POST'])
    def patientdata():
        if request.method =='POST':
            data=patient.find()
            payload=request.get_json()
            print(payload)
            for i in data:

                    if payload['pId'] == str(i['_id']):
                        del i['_id']
                        del i['doc_ID']
                        response = jsonify([i])
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                    else:
                        pass

            response = jsonify({'status':'no data found'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
patientData()
