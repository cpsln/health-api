from app import app
from flask import render_template, request,session,jsonify
from db_config import patient

# def signupDoctor():                     
#     @app.route('/patientList')
#     def plist():
#         pass
    #     return render_template('signup.html')
def PatientList():
    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response
            
    @app.route('/patientList', methods=['POST'])
    def patientlist():
        if request.method =='POST':
            data=patient.find()
            l=[]
            payload=request.get_json()
            print(payload,'*************23')
            for i in data:
                if i['doc_ID']== payload['doc_ID']:
                    pId=str(i['_id'])
                    name=i['FirstName']+' '+i['LastName']   
                    gender=i['Gender']
                    email=i['email']
                    dob=i['Birthdate']
                    mob=i['phoneno']
                    mydict={'pId':pId,'name':name,'gen':gender,'email':email,'DOB':dob,'mobile':mob}
                    # print(mydict)
                    l.append(mydict)
                    # if i['Firstname']+' '+i['Lastname']=='vikash sharma':
                    
            # return jsonify(l)
            response = jsonify(l)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            # return "None"
                
PatientList()   

# if __name__ == '__main__':

#     app.run(debug=True,port=5002)