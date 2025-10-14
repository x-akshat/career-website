from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS= [
   {
      "id": 1,
      "title": "INSTAGRAM",
      "Search": "Akshatchariya_",
      
   },
   {
      "id": 2,
      "title": "GitHub",
      "Search": "x-akshat",
      
   },
   {
      "id": 3,
      "title": "LinkedIn",
      "Search": "akshat-chariya-4910a9369"
   },
   {
      "id": 4,
      "title": "YouTube",
      "Search": "HACKERISLIVE_",
      
   }
]
  
@app.route('/')
def hello_world():
   return render_template("home.html",
                          jobs=JOBS,                 
                          company_name='AKSHAT')

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  