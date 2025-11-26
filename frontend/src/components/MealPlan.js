import React from "react";

const MealPlan = ({ mealPlan, pdfUrl }) => {
  if (!mealPlan) return null;

  return (
    <div>
      <h2>Your Meal Plan</h2>
      {Object.keys(mealPlan).map((meal) => (
        <div className="meal-card" key={meal}>
          <h3>{meal.charAt(0).toUpperCase() + meal.slice(1)}</h3>
          <p>{mealPlan[meal].name} - {mealPlan[meal].grams} g</p>
        </div>
      ))}
      {pdfUrl && (
        <a href={pdfUrl} download="meal_plan.pdf">
          <button>Download PDF</button>
        </a>
      )}
    </div>
  );
};

export default MealPlan;
