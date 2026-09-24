


class KidneyChecker:

  def __init__(self, creatinine, urea):
    self.creatinine = creatinine
    self.urea = urea
  def analyze(self):
    if self.creatinine > 1.3 or self.urea > 45:
      return "High Risk (Abnormal kidney function values)"
    elif 1.0 <= self.creatinine <= 1.3 or 20 <= self.urea <= 45:
      return "Moderate Risk (Slightly elevated numbers)"
    else:
      return "Low Risk (Kidneys functioning normally)"