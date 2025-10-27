from datetime import date, timedelta
​
def life_predictor(birth_date):
    return (date.fromisoformat(birth_date) - timedelta(days=280)).isoformat()