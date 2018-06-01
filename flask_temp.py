from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route("/cron_job",methods=['POST'])
def cronjob_func():
	#Insert cron job code here
    print(request.form['name'])
    return 'Hello '+request.form['name']
if __name__ == '__main__':
   app.run()
