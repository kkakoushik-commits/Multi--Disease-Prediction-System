


class DiabetesChecker:

  def __init__(self, glucose, bmi):
    self.glucose = glucose
    self.bmi = bmi

  def analyze(self):
    if self.glucose > 140 or self.bmi > 30:
      return "High Risk (Diabetes indicators are high)"
    elif 100 <= self.glucose <= 140 or 25 <= self.bmi <= 30:
      return "Moderate Risk (Pre-diabetes signs detected)"
    else:
      return "Low Risk (Normal glucose and BMI)"

