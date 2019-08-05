from flask import render_template, request,session,jsonify
import hashlib
from db_config import doctor,patient
from app import app                   

def FillAlternateContact():
#     @app.route('/AlternateContact')
#     def rootAC():
#         return render_template('AlternateContact.html')

    @app.after_request
    def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

    @app.route('/AlternateContact',methods = ['POST'])
    def AlternateContact():
        if request.method == 'POST':
 
            # fname = request.form["Full Name"]
            # mno = request.form["MobileNo"]
            # Rship=  request.form["RelationShip"]
            # mydict={'Full Name':fname,'MobileNo':mno,'RelationShip':Rship}

            payload=request.get_json()
            print(payload,"+++++")
            for pId in patient.find():
                # if session['docId'] == pId['DoctorId']:
                # name=pId["Firstname"]+' '+pId["Lastname"]
                # if request.form["Patient name"] == name:

                if payload['pId'] == str(pId['_id']):
                        del payload['pId']
                        try:
                            
                            pId['AlternateContact'].append(payload)
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                        'AlternateContact':pId['AlternateContact']
                                        }
                                    }
                                )
                        except KeyError:
                        
                            patient.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                            # 'AlternateContact':[mydict]
                                            'AlternateContact':[payload]
                                        }
                                    }
                            )
                        # return render_template("AlternateContact.html",a='AlternateContact Add')
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
            
FillAlternateContact()
