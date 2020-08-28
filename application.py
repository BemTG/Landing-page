from flask import Flask, render_template, request
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *



app=application=Flask(__name__)

@application.route('/', methods=['POST', 'GET'])
@application.route('/index.html', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		email_address = request.form['email']
		full_name = request.form['name']
		message = request.form['message']
		
		if email_address != '':
			full_name = full_name.encode('ascii', errors='ignore').decode()
			
			SENDGRID_API_KEY = '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'
			sg = sendgrid.SendgridAPIClient(api_key=SENDGRID_API_KEY )
			
			message = Mail(
				from_email='fesum_g@hotmail.co.uk',
				to_email='fesum_g@hotmail.co.uk',
				subject='Bemenet website',
				html_content='Email: ' + email_address + ' Name: ' + full_name + ' ' + message)
			
			try:
				sg = sendgrid.SendgridAPIClient(api_key=SENDGRID_API_KEY )
				response = sg.send(message)
			except Exception as e:
				print(str(e))
	return render_template('index.html')

if __name__ =='__main__':
    application.run(host='0.0.0.0', port=80,debug=True)
