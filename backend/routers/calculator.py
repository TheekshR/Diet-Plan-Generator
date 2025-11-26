from fastapi import APIRouter
from pydantic import BaseModel
from services.calculator_service import calculate_bmr, calculate_tdee, calculate_goal_calories

router = APIRouter(prefix="/calculate", tags=["Calculator"])

class CalcRequest(BaseModel):
    age: int
    gender: str
    weight: float   # in kg
    height: float   # in cm
    activity_level: str  # sedentary/light/moderate/active/very_active
    goal: str  # weight_loss / weight_gain / maintain

@router.post("/calories")
def calculate(data: CalcRequest):
    bmr = calculate_bmr(data.gender, data.weight, data.height, data.age)
    tdee = calculate_tdee(bmr, data.activity_level)
    goal_calories = calculate_goal_calories(tdee, data.goal)
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "target_calories": round(goal_calories)
    }
