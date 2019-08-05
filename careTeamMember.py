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

@app.route('/careTeamMember',methods = ['POST'])
def careTeamMember():
        if request.method == 'POST':
 
            payload=request.get_json()
            print(payload,"+++++")
            for pId in patient.find():

                if payload['pId'] == str(pId['_id']):
                        del payload['pId']
                        try:
                            
                            pId['careTeamMember'].append(payload)
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                        'careTeamMember':pId['careTeamMember']
                                        }
                                    }
                                )
                        except KeyError:
                        
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                            'careTeamMember':[payload]
                                        }
                                    }
                            )

                        response = jsonify({'status':'save contact'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                else:
                        pass
            
            response = jsonify({'status':'Not save contact'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            

