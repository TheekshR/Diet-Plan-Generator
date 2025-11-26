import React, { useState } from "react";
import api from "../api";
import "../styles/Form.css";

const Form = ({ setMealPlan, setPdfUrl }) => {
  const [form, setForm] = useState({
    name: "",
    age: "",
    gender: "male",
    weight: "",
    height: "",
    activity_level: "sedentary",
    goal: "weight_loss",
    diet_preference: "any"
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const generateMealPlan = async () => {
    try {
      // Generate meal plan
      const res = await api.post("/meals/generate", form);
      setMealPlan(res.data.meal_plan);

      // Generate PDF
      const pdfRes = await api.post("/pdf/mealplan", form, { responseType: "blob" });
      const pdfBlob = new Blob([pdfRes.data], { type: "application/pdf" });
      const pdfUrl = window.URL.createObjectURL(pdfBlob);
      setPdfUrl(pdfUrl);
    } catch (err) {
      console.error(err);
      alert("Something went wrong!");
    }
  };

  return (
    <div className="form-container">
      <h2>Enter Your Details</h2>

      <label>Enter Name:</label>
      <input placeholder="Name" name="name" value={form.name} onChange={handleChange} />

      <label>Enter Age:</label>
      <input placeholder="Age" name="age" value={form.age} onChange={handleChange} type="number" />

      <label>Enter Weight (kg):</label>
      <input placeholder="Weight (kg)" name="weight" value={form.weight} onChange={handleChange} type="number" />

      <label>Enter Height (cm):</label>
      <input placeholder="Height (cm)" name="height" value={form.height} onChange={handleChange} type="number" />

      <label>Gender:</label>
      <select name="gender" value={form.gender} onChange={handleChange}>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>

      <label>Activity Level:</label>
      <select name="activity_level" value={form.activity_level} onChange={handleChange}>
        <option value="sedentary">Sedentary</option>
        <option value="light">Light</option>
        <option value="moderate">Moderate</option>
        <option value="active">Active</option>
      </select>

      <label>Goal:</label>
      <select name="goal" value={form.goal} onChange={handleChange}>
        <option value="weight_loss">Weight Loss</option>
        <option value="weight_gain">Weight Gain</option>
        <option value="maintenance">Maintenance</option>
      </select>

      <label>Diet Preference:</label>
      <select name="diet_preference" value={form.diet_preference} onChange={handleChange}>
        <option value="any">Any</option>
        <option value="veg">Vegetarian</option>
        <option value="non_veg">Non-Vegetarian</option>
      </select>

      <button onClick={generateMealPlan}>Generate Meal Plan</button>
    </div>
  );
};

export default Form;
