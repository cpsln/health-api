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

@app.route('/ContactDoc',methods = ['POST'])
def ContactDoc():
        if request.method == 'POST':
 
            
            payload=request.get_json()
            
            for pId in patient.find():
                if payload['doc_ID'] == str(pId['_id']):
                        del payload['doc_ID']
                    
                        print(payload['doc_ID'])
                        # patient.update_one({
                        #             '_id':pId['_id']
                        #     },{
                        #     # '$set':{'name':'chandra'},
                        #         '$set':{
                        #         'adresss':payload
                        #         }
                        #     }
                        # )
                        response = jsonify({'status':'Save Contact'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
            
            response = jsonify({'status':'Not save Contact'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response

# fillContact()
    