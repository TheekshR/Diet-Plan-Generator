from fastapi import APIRouter
from pydantic import BaseModel
from services.calculator_service import calculate_bmr, calculate_tdee, calculate_goal_calories
from services.meal_plan_service import generate_meal_plan

router = APIRouter(prefix="/meals", tags=["Meals"])

class MealRequest(BaseModel):
    age: int
    gender: str
    weight: float
    height: float
    activity_level: str
    goal: str
    diet_preference: str = "any"  # veg, non_veg, any

@router.post("/generate")
def generate_meals(request: MealRequest):
    bmr = calculate_bmr(request.gender, request.weight, request.height, request.age)
    tdee = calculate_tdee(bmr, request.activity_level)
    target_calories = calculate_goal_calories(tdee, request.goal)
    plan = generate_meal_plan(int(target_calories), request.diet_preference)
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "target_calories": round(target_calories),
        "meal_plan": plan
    }
