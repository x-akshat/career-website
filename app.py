from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS= [
   {
      "id": 1,
      "title": "DOCTOR 1",
      "location": "Bengaluru, India",
      "FEES": "Rs. 1,000"
   },
   {
      "id": 2,
      "title": "DOCTOR 2",
      "location": "Delhi, India",
      "salary": "Rs. 1,500"
   },
   {
      "id": 3,
      "title": "DOCTOR 3",
      "location": "New delhi"
   },
   {
      "id": 4,
      "title": "Doctor 4",
      "location": "AGRA",
      "salary": "Rs. 800"
   }
]
  
@app.route('/')
def hello_world():
   return render_template("home.html",
                          jobs=JOBS,                 
                          company_name='SA')

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  