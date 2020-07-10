from flask import Flask, render_template

app=application=Flask(__name__)

@application.route('/')
@application.route('/index.html')
def index():
	return render_template('index.html')

if __name__ =='__main__':
    application.run(host='0.0.0.0', port=80,debug=True)
