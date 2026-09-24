from flask import Flask, render_template, request, jsonify
from database import init_db, save_prediction, get_all_patients, add_patient

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/patients", methods=["GET"])
def api_get_patients():
    patients = get_all_patients()
    return jsonify(patients)

@app.route("/api/register", methods=["POST"])
def register_patient():
    data = request.get_json()
    patient_id = data.get("id")
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    
    if not patient_id or not name:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
        
    add_patient(patient_id, name, age, gender)
    return jsonify({"status": "success", "message": "Patient registered successfully!"})

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    disease = data.get("disease")
    risk_status = "Normal"
    
    if disease == "Kidney Disease":
        creatinine = float(data.get("creatinine") or 0)
        urea = float(data.get("urea") or 0)
        if creatinine > 1.5 or urea > 40:
            risk_status = "High Risk"
        elif creatinine > 1.2 or urea > 30:
            risk_status = "Low Risk"
            
    elif disease == "Cardiovascular Disease":
        bp = float(data.get("bp") or 0)
        cholesterol = float(data.get("cholesterol") or 0)
        if bp > 140 or cholesterol > 240:
            risk_status = "High Risk"
        elif bp > 120 or cholesterol > 200:
            risk_status = "Low Risk"
            
    elif disease == "Fever Assessment":
        temp = float(data.get("temperature") or 0)
        if temp > 102.0:
            risk_status = "High Risk"
        elif temp > 99.5:
            risk_status = "Low Risk"
            
    elif disease == "Diabetes":
        glucose = float(data.get("glucose") or 0)
        if glucose > 140:
            risk_status = "High Risk"
        elif glucose > 100:
            risk_status = "Low Risk"

    return jsonify({"status": "success", "risk": risk_status})

if __name__ == "__main__":
    app.run(debug=True)