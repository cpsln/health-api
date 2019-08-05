from flask import Flask,request,jsonify
from flask_mail import Mail, Message
# import smtplib
from app import app




	
# app =Flask(__name__)
# mail=Mail(app)
# def create_Messege():
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = '007cpsln@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Cp$ln0142'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'dkm.5853@gmail.com',
    MAIL_PASSWORD = 'saibaba@s$$1',
))
mail = Mail(app)
		# mail = Mail(app)
@app.after_request
def apply_caching(response):
		response.headers["Content-Type"] = "application/json"
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Headers'] = 'content-type'
		return response
# def CreateMessage1():	
@app.route("/sendMessage", methods=['POST'])
def createMessege():
		if request.method == 'POST':
			payload=request.get_json()
			print('*****\n',payload)
			#print(type(payload['subject']))
			msg = Message(payload['subject'], sender = 'dkm.5853@gmail.com', recipients = [payload['to']])
			msg.body =payload['message']
			mail.send(msg)

			response = jsonify({'sent':'messege sent'})
			response.headers.add('Access-Control-Allow-Origin', '*')
			response.headers['Access-Control-Allow-Origin'] = '*'
			
			return response
