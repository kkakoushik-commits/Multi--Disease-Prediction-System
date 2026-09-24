class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.reports = []  

    def add_report(self, disease_name, risk_status):
        report = {"disease": disease_name, "status": risk_status}
        self.reports.append(report)

    def show_details(self):
        print("\n--- Patient Profile ---")
        print(f"ID     : {self.patient_id}")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")

        if self.reports:
            print("Prediction History:")
            for report in self.reports:
                print(f" -> {report['disease']}: {report['status']}")
        else:
            print("No risk reports logged yet.")

        print("-" * 25)