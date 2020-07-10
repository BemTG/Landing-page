from flask import Flask, render_template

app=application=Flask(__name__)

@application.route('/')
@application.route('/index.html')
def index():
	return render_template('index.html')

if __name__ =='__main__':
    application.run(debug=True)