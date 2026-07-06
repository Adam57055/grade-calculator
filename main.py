from openai import OpenAI 
import json

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-5.3-mini',
    input = [
        {
            "role", "system",
            "content": 
                "You are a professional grade analyst tasked with assessing the future scores needed for the user to achieve their desired grade.",
                "Use mathematical equations and verify your solutions to ensure accuracy",
                "Return with VALID JSON ONLY",
        },
    ]
)



