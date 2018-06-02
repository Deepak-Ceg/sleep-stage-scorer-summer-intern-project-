from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route("/cron_job")
def cronjob_func():
	#Insert cron job code here
	return "Hello biks"
    #print(request.form['name'])
    #return 'Hello '+request.form['name']
if __name__ == '__main__':
   app.run()