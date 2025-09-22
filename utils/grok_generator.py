import requests
import os
from dotenv import load_dotenv

load_dotenv()
GROK_API_KEY = os.getenv("GROK_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_plan_with_grok(age, gender, weight, height, goal, activity, diet_pref):
    prompt = f"""
    Create a 7-day personalized workout and diet plan for:
    Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm, 
    Goal: {goal}, Activity Level: {activity}, Dietary Preference: {diet_pref}.
    
    Workout: Include exercise type, sets, reps, duration, rest time.
    Diet: Include breakfast, lunch, dinner, snacks, total daily calories, macros.
    Provide the output in a structured, readable format with clear headings.
    """

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "x-ai/grok-4-fast:free",  # <-- the model you're using
        "messages": [
            {"role": "system", "content": "You are a professional fitness and nutrition coach."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100000,
        "temperature": 0.7
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
