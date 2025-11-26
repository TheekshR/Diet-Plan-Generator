import json
import random

DATA_PATH = "data/meals.json"

def load_meals():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def pick_meal(meals, meal_type, diet_preference="any"):
    options = meals.get(meal_type, [])
    if diet_preference != "any":
        options = [m for m in options if diet_preference in m.get("diet", "any")]
    if not options:
        return {"name": "No option available", "cal": 0, "default_grams": 100}
    return random.choice(options)

def generate_meal_plan(target_calories, diet_preference="any"):
    meals = load_meals()
    splits = {"breakfast": 0.3, "lunch": 0.35, "dinner": 0.3, "snacks": 0.05}
    plan = {}
    
    for meal_type, fraction in splits.items():
        choice = pick_meal(meals, meal_type, diet_preference)
        target_cal_for_meal = target_calories * fraction
        # Calculate grams needed to match target calories
        if choice["cal"] > 0:
            grams_needed = (target_cal_for_meal / choice["cal"]) * choice.get("default_grams", 100)
        else:
            grams_needed = choice.get("default_grams", 100)
        
        plan[meal_type] = {
            "name": choice["name"],
            "grams": round(grams_needed)
        }
    
    return plan
