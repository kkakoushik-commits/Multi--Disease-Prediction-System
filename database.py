import sqlite3

def init_db():
    conn = sqlite3.connect('health_predictions.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM patients')
    if cursor.fetchone()[0] == 0:
        default_patients = [
            ("PT-2026-001", "Pradeep Sahu", 45, "Male"),
            ("PT-2026-002", "Varsha Rai", 38, "Female"),
            ("PT-2026-003", "Pradeep Kumar", 52, "Male"),
            ("PT-2026-004", "Bhargavi Ramesh", 29, "Female"),
            ("PT-2026-005", "Mahendra Rao", 61, "Male"),
            ("PT-2026-006", "Karthik Ram", 41, "Female")
        ]
        cursor.executemany('INSERT INTO patients (id, name, age, gender) VALUES (?, ?, ?, ?)', default_patients)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            disease TEXT,
            result TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_patient(patient_id, name, age, gender):
    conn = sqlite3.connect('health_predictions.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO patients (id, name, age, gender) VALUES (?, ?, ?, ?)', 
                   (patient_id, name, age, gender))
    conn.commit()
    conn.close()

def get_all_patients():
    conn = sqlite3.connect('health_predictions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, age, gender FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return patients

def save_prediction(patient_id, disease, result):
    conn = sqlite3.connect('health_predictions.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO predictions (patient_id, disease, result) VALUES (?, ?, ?)', 
                   (patient_id, disease, result))
    conn.commit()
    conn.close()