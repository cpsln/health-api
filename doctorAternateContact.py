from flask import render_template, request,session,jsonify
import hashlib
from db_config import doctor
from app import app                   

# def FillAlternateContact():
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
def docAlternateContact():
        if request.method == 'POST':
 
            # fname = request.form["Full Name"]
            # mno = request.form["MobileNo"]
            # Rship=  request.form["RelationShip"]
            # mydict={'Full Name':fname,'MobileNo':mno,'RelationShip':Rship}

            payload=request.get_json()
            
            for dId in doctor.find():
                # if session['docId'] == dId['DoctorId']:
                # name=dId["Firstname"]+' '+dId["Lastname"]
                # if request.form["Patient name"] == name:

                if payload['dId'] == str(dId['_id']):
                    
                        try:
                            
                            dId['AlternateContact'].append(payload)
                            doctor.update_one({
                                    '_id':dId['_id']
                                },{
                                    '$set':{
                                
                                        'AlternateContact':dId['AlternateContact']
                                        }
                                    }
                                )
                        except KeyError:
                            doctor.update_one({
                                    '_id':dId['_id']
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
            
# FillAlternateContact()
