from Cardio_module import CardioChecker
from database import init_db, add_patient, save_prediction, get_connection
from diabetes_module import DiabetesChecker
from fever_module import FeverChecker
from Kidney_module import KidneyChecker
from patient import Patient


def main():
  init_db()

  while True:
    print("\n=== MULTI-DISEASE PREDICTION SYSTEM ===")
    print("1. Register New Patient")
    print("2. Check Disease Risk")
    print("3. View Patient History")
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      print("\n--- New Patient Registration ---")
      pid = input("Enter a unique Patient ID (or code): ")

      # Check if patient already exists in SQLite database
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM patients WHERE id = ?", (pid,))
      existing_patient = cursor.fetchone()
      conn.close()

      if existing_patient:
        print("Error: This Patient ID already exists!")
      else:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO patients (id, name, age, gender) VALUES (?, ?, ?, ?)",
            (pid, name, age, gender),
        )
        conn.commit()
        conn.close()

        print(f"Success! Patient {name} registered and saved to database.")

    elif choice == "2":
      print("\n--- Disease Risk Assessment ---")
      pid = input("Enter Patient ID: ")

      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM patients WHERE id = ?", (pid,))
      db_patient = cursor.fetchone()
      conn.close()

      if not db_patient:
        print("Error: Patient ID not found. Please register first.")
      else:
        patient_name = db_patient[1]
        print(f"Running assessment for: {patient_name}")

        print("\nSelect Disease Module:")
        print("1. Diabetes")
        print("2. Cardiovascular")
        print("3. Kidney")
        print("4. Fever Assessment")

        disease_choice = input("Select option (1-4): ")

        if disease_choice == "1":
          g = float(input("Enter Blood Glucose (mg/dL): "))
          b = float(input("Enter BMI: "))
          checker = DiabetesChecker(g, b)
          result = checker.analyze()
          input_data = f"Glucose: {g}, BMI: {b}"
          save_prediction(pid, "Diabetes", input_data, result, risk_score=0.0)
          print(f"Result: {result}")

        elif disease_choice == "2":
          bp = float(input("Enter Blood Pressure (mmHg): "))
          chol = float(input("Enter Cholesterol (mg/dL): "))
          checker = CardioChecker(bp, chol)
          result = checker.analyze()
          input_data = f"BP: {bp}, Cholesterol: {chol}"
          save_prediction(
              pid, "Cardiovascular", input_data, result, risk_score=0.0
          )
          print(f"Result: {result}")

        elif disease_choice == "3":
          cr = float(input("Enter Creatinine (mg/dL): "))
          ur = float(input("Enter Blood Urea (mg/dL): "))
          checker = KidneyChecker(cr, ur)
          result = checker.analyze()
          input_data = f"Creatinine: {cr}, Urea: {ur}"
          save_prediction(pid, "Kidney Disease", input_data, result, risk_score=0.0)
          print(f"Result: {result}")

        elif disease_choice == "4":
          temp = float(input("Enter Body Temperature (°F): "))
          duration = int(input("Enter Duration (days): "))
          checker = FeverChecker(temp, duration)
          result = checker.analyze()
          input_data = f"Temp: {temp}°F, Duration: {duration} days"
          save_prediction(pid, "Fever Assessment", input_data, result, risk_score=0.0)
          print(f"Result: {result}")

        else:
          print("Invalid disease module choice.")

    elif choice == "3":
      print("\n--- View Patient History ---")
      pid = input("Enter Patient ID: ")

      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM patients WHERE id = ?", (pid,))
      db_patient = cursor.fetchone()

      if not db_patient:
        print("Error: Patient ID not found.")
      else:
        print(f"\nPatient Details:")
        print(f"ID: {db_patient[0]}")
        print(f"Name: {db_patient[1]}")
        print(f"Age: {db_patient[2]}")
        print(f"Gender: {db_patient[3]}")

        cursor.execute(
            "SELECT disease_type, input_data, result, prediction_date FROM"
            " predictions WHERE patient_id = ?",
            (pid,),
        )
        predictions = cursor.fetchall()

        print("\nPrediction History:")
        if not predictions:
          print("No history available.")
        else:
          for p in predictions:
            print(
                f"- [{p['prediction_date']}] {p['disease_type']}:"
                f" {p['result']} (Inputs: {p['input_data']})"
            )
      conn.close()

    elif choice == "4":
      print("\nExiting system. Stay healthy!")
      break

    else:
      print("Invalid menu choice. Please select between 1 and 4.")


if __name__ == "__main__":
  main()