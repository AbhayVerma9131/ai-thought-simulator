from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def simulate_thought(scenario, mode):
    try:
        prompt = f"""
You are an intelligent decision-making assistant.

Analyze the following situation:
"{scenario}"

Use {mode} thinking style.

Break your response into:
1. Key Factors
2. Pros and Cons
3. Risks
4. Final Recommendation

Keep it structured and clear.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ ERROR: {str(e)}"
