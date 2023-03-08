from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Cluj-Napoca, Romania',
  'salary': '$5,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary': '$3,500'
}, {
  'id': 3,
  'title': 'Frontend Enginner',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Enginner 2',
  'location': 'San-Francisco, USA',
  'salary': '$39,000'
}]


@app.route("/")
def hello_ctarnu():
  return render_template('home.html', jobs=JOBS, company_name='All I need')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
