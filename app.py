from flask import Flask, request,current_app,url_for,redirect,render_template
app = Flask(__name__)

@app.route('/index/', methods=['GET'])
def root():
	return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True)