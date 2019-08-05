from app import app
from flask import render_template, request,session,jsonify

from db_config import doctor


# def signupDoctor():
#     @app.route('/PatientData')
#     def pdata():
#         # # return render_template('New_Patient.html')
#         # print("jnvjdksbjfbfjvbfjv")
#         # return "jkndcdj"
#         pass
@app.after_request
def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

def doctorData():
    @app.route('/doctorData', methods=['POST'])
    def doctordata():
        if request.method =='POST':
            data=doctor.find()
            payload=request.get_json()
            print(payload)

            for i in data:

                    if payload['doc_ID'] == str(i['_id']):
                        # i['_id']=str(i['_id'])
                        # return jsonify([i])
                        del i['_id']
                        # del i['doc_ID']
                        response = jsonify(i)
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                    else:
                        pass
                # else:
                #     return "No data for this doctor"
                
            
            response = jsonify({'status':'no data found'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
    
doctorData()
