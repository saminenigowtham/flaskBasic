from flask import Flask, render_template,jsonify
from database import get_all_jobs

app = Flask(__name__)


@app.route('/')
def hello_gou():
  return render_template('home.html', jobs=get_all_jobs())
@app.route('/api/job')
def list_jobs():
  return jsonify(get_all_jobs())
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
