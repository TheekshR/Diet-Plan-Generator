import React, { useState } from "react";
import Form from "./components/Form";
import MealPlan from "./components/MealPlan";
import './App.css';

function App() {
  const [mealPlan, setMealPlan] = useState(null);
  const [pdfUrl, setPdfUrl] = useState(null);

  return (
    <div className="App">
      <h1>Diet Plan Generator</h1>
      <div className="container">
        <div className="left">
          <Form setMealPlan={setMealPlan} setPdfUrl={setPdfUrl} />
        </div>
        <div className="right">
          <MealPlan mealPlan={mealPlan} pdfUrl={pdfUrl} />
        </div>
      </div>
    </div>
  );
}

export default App;
