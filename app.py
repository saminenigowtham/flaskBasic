from flask import Flask, render_template,jsonify


app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York',
}, {
    'id': 3,
    'title': 'Machine Learning Engineer',
    'location': 'New York',
    'salary': '$150,000'
}, {
    'id': 4,
    'title': 'Software Engineer',
    'location': 'New York',
    'salary': '$200,000'
}]


@app.route('/')
def hello_gou():
  return render_template('home.html', jobs=JOBS)
@app.route('/api/job')
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
