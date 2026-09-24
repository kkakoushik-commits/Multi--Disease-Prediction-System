

class CardioChecker:

  def __init__(self, bp, cholesterol):
    self.bp = bp
    self.cholesterol = cholesterol

  def analyze(self):
    if self.bp > 140 or self.cholesterol > 240:
      return "High Risk (High blood pressure/cholesterol levels)"
    elif 120 <= self.bp <= 140 or 200 <= self.cholesterol <= 240:
      return "Moderate Risk (Borderline heart markers)"
    else:
      return "Low Risk (Healthy heart range)"
