# fever_module.py

def predict_fever(data):
    """
    Evaluates fever risk with a human, reassuring, and caring tone.
    """
    try:
        temp_input = (
            data.get('temperature') or 
            data.get('body_temperature') or 
            data.get('bodyTemperature') or 
            98.6
        )
        duration_input = (
            data.get('duration') or 
            data.get('duration_days') or 
            0
        )
        
        temperature = float(temp_input)
        duration = int(duration_input)
        
        if temperature >= 103.0 or (temperature >= 101.0 and duration >= 3):
            return {
                "risk_level": "High Priority",
                "message": "It looks like you've had a high fever or it's been lasting a few days. Please reach out to a doctor or visit a clinic soon so you can feel better."
            }
        elif temperature >= 100.4:
            return {
                "risk_level": "Moderate Attention",
                "message": "You have a mild fever. Try resting up, drinking plenty of water, and keeping an eye on how you feel over the next 24 hours."
            }
        else:
            return {
                "risk_level": "All Clear",
                "message": "Your body temperature is sitting right in the normal, healthy range. Keep taking care of yourself!"
            }
            
    except (ValueError, TypeError):
        return {
            "risk_level": "Oops!",
            "message": "We couldn't quite read those numbers. Could you please double-check your temperature and duration entries?"
        }

class FeverChecker:
    def __init__(self, temp, duration):
        self.temp = temp
        self.duration = duration

    def analyze(self):
        # Passes the instantiated values into a dictionary format for your existing prediction logic
        data = {
            "temperature": self.temp,
            "duration": self.duration
        }
        result_dict = predict_fever(data)
        return f"{result_dict['risk_level']}: {result_dict['message']}"

    @staticmethod
    def check_fever(data):
        return predict_fever(data)