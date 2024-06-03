import streamlit as st
import requests
def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize BMI into Underweight, Normal weight, Overweight, or Obese."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")

    weights = []
    heights = []
    bmis = []
    categories = []

    weight = st.number_input("Enter your weight in kilograms", step=0.1, format="%.1f")
    height = st.number_input("Enter your height in meters", step=0.01, format="%.2f")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        api_url = "http://localhost:8000/calculate_bmi"
    data = {"weight": weight, "height": height}

    response = requests.post(api_url, json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    bmi = response.json()["bmi"]
    category = response.json()["category"]

    weights.append(weight)
    heights.append(height)
    bmis.append(bmi)
    categories.append(category)

    st.write(f"Your BMI is: {bmi:.2f}")
    st.write(f"You are categorized as: {category}")

    if weights:
        st.subheader("Summary of all BMI calculations:")
        for i in range(len(weights)):
            st.write(f"Person {i + 1}: Weight = {weights[i]} kg, Height = {heights[i]} m, BMI = {bmis[i]:.2f}, Category = {categories[i]}")

if __name__ == "__main__":
    main()