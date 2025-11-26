from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_meal_plan_pdf(user_info: dict, target_calories: int, meal_plan: dict, current_calories: int) -> bytes:
    """
    Generates a PDF for the meal plan with user details.
    user_info: dict containing name, age, weight, height, gender
    """
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 50, f"{user_info['name']}'s Daily Meal Plan")

    # User Details
    c.setFont("Helvetica", 12)
    y = height - 90
    c.drawString(50, y, f"Age: {user_info['age']} years")
    y -= 20
    c.drawString(50, y, f"Weight: {user_info['weight']} kg")
    y -= 20
    c.drawString(50, y, f"Height: {user_info['height']} cm")
    y -= 20
    c.drawString(50, y, f"Gender: {user_info['gender'].capitalize()}")
    y -= 30

    # Calories
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Calories Information")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Current Calories: {current_calories} kcal")
    y -= 20
    c.drawString(50, y, f"Target Calories: {target_calories} kcal")
    y -= 30

    # Meal Plan
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Meal Plan")
    y -= 20
    for meal_type, details in meal_plan.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, meal_type.capitalize())
        y -= 20
        c.setFont("Helvetica", 12)
        c.drawString(70, y, f"{details['name']} - {details['grams']} g")
        y -= 30

    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
