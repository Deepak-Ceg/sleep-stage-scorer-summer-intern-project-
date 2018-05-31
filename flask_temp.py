from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/cron_job")
def cronjob_func():
	#Insert cron job code here
	return;
	
