from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from services.pdf_service import generate_meal_plan_pdf
from services.calculator_service import calculate_bmr, calculate_tdee, calculate_goal_calories
from services.meal_plan_service import generate_meal_plan
import io

router = APIRouter(prefix="/pdf", tags=["PDF"])

class PDFRequest(BaseModel):
    name: str
    age: int
    gender: str
    weight: float
    height: float
    activity_level: str
    goal: str
    diet_preference: str = "any"

@router.post("/mealplan")
def create_pdf(request: PDFRequest):
    # Calculate current and target calories
    bmr = calculate_bmr(request.gender, request.weight, request.height, request.age)
    tdee = calculate_tdee(bmr, request.activity_level)
    target_calories = calculate_goal_calories(tdee, request.goal)
    
    # Generate meal plan
    meal_plan = generate_meal_plan(int(target_calories), request.diet_preference)

    # Prepare user info dict
    user_info = {
        "name": request.name,
        "age": request.age,
        "weight": request.weight,
        "height": request.height,
        "gender": request.gender
    }

    # Generate PDF
    pdf_bytes = generate_meal_plan_pdf(user_info, int(target_calories), meal_plan, int(tdee))
    return StreamingResponse(io.BytesIO(pdf_bytes), media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename={request.name}_meal_plan.pdf"
    })

