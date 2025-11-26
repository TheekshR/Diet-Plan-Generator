def calculate_bmr(gender: str, weight: float, height: float, age: int) -> float:
    gender = gender.lower()
    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr: float, activity_level: str) -> float:
    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    return bmr * factors.get(activity_level, 1.2)

def calculate_goal_calories(tdee: float, goal: str) -> float:
    goal = goal.lower()
    if goal == "weight_loss":
        return tdee - 500
    if goal == "weight_gain":
        return tdee + 500
    return tdee
