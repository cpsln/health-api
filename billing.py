from flask import render_template, request,jsonify
import hashlib
from db_config import patient
from app import app

	
@app.after_request
def apply_caching(response):
			response.headers["Content-Type"] = "application/json"
			response.headers['Access-Control-Allow-Origin'] = '*'
			response.headers['Access-Control-Allow-Headers'] = 'content-type'
			return response

@app.route('/billing', methods=['POST'])

def Billing():
	if request.method == 'POST':
			
			payload=request.get_json()
			print(payload)
			
			for i in patient.find():
				
				if payload['pId'] == str(i['_id']):
					try: 
						
						i['Billing'].append(payload)
						patient.update_one({
								'_id':i['_id']
								},{	'$set':{
									'Billing':i['Billing']
									}
								}
						)
						response = jsonify({'DocId':'datagrazp'})
						response.headers.add('Access-Control-Allow-Origin', '*')
						response.headers['Access-Control-Allow-Origin'] = '*'
						print(response)
						print(response.headers)
						return response
					except KeyError:
						
					
						patient.update_one({
								'_id':i['_id']
							},{
								'$set':{
									'Billing':[payload]
								}
							}
						)
					
					response = jsonify({'DocId':'datagrazp1'})
					response.headers.add('Access-Control-Allow-Origin', '*')
					response.headers['Access-Control-Allow-Origin'] = '*'
					print(response)
					print(response.headers)
					return response
			
				else:
					pass
			
			response = jsonify({'DocId':'datagrazp2'})
			response.headers.add('Access-Control-Allow-Origin', '*')
			response.headers['Access-Control-Allow-Origin'] = '*'
			print(response,'++++******++++')
			print(response.headers)
			return response
			
		
		
		

