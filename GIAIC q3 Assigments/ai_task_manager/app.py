import json
from google import genai
from google.genai import types

# Initialize the Gemini AI client
client = genai.Client(api_key="AIzaSyBC6yAR-S2qW88rUE8fcc8zntaY2VpR0IA")

# Define the system instruction
system_instruction = types.Part.from_text(text="""
You are an AI assistant that follows a strict state protocol: START, PLAN, ACTION, OBSERVATION, OUTPUT.
Wait for the user prompt and then respond with a plan that uses the available tools.
After each action, wait for the corresponding observation.
When you are ready to provide the final answer, output a single JSON object in the exact format below (do not output multiple JSON objects or extra text):

Example final output:
{ "type": "output", "output": "The sum of weather of Patiala and Mohali is 24°C" }

AVAILABLE TOOLS:
1. function getWeatherDetails(city:string):string // Returns the weather detail of the city.

EXAMPLE:
{ "type": "user", "user": "What is the sum of weather of Patiala and Mohali?" },
{ "type": "plan", "plan": "I will call the getWeatherDetails for Patiala" },
{ "type": "action", "function": "getWeatherDetails", "input": "patiala" },
{ "type": "observation", "observation": "10°C" },
{ "type": "plan", "plan": "I will call getWeatherDetails for Mohali" },
{ "type": "action", "function": "getWeatherDetails", "input": "mohali" },
{ "type": "observation", "observation": "14°C" },
{ "type": "output", "output": "The sum of weather of Patiala and Mohali is 24°C" }
""")

# Generate AI response
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[types.Content(role="user", parts=[types.Part.from_text(text="give me karachi weather")]), 
              types.Content(role="")],
    config=types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[system_instruction],
    ),
)


print(response.text)