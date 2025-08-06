# FUTURE_ML_03
Task 3

🔗 **Download ZIP**:  
👉 [Download dialogflow agent (.zip)](https://drive.google.com/file/d/1dXbrlvYVjyhkDuRXckuUG9_GCZzDHgS1/view?usp=sharing)

To import:
1. Go to Dialogflow console
2. Create a new agent
3. Click ⚙️ → "Export and Import" → "Restore from ZIP"
4. Select the downloaded ZIP file

# AI Chatbot with Dialogflow, Gemini API, Flask & Ngrok

This is a chatbot project using:
Dialogflow (for user intents)
 Flask (for the webhook)
 Google's Gemini API (for generating intelligent responses)
 ngrok (to expose your local server to Dialogflow)


## 📦 What You Need:
- Python 3.10 or higher
- API key
- Dialogflow account: https://dialogflow.cloud.google.com
- ngrok: https://ngrok.com/download

---

## How to Run This Project:

### Step 1: Install Python libraries
Open a terminal and run:
    pip install flask google-generativeai

---

### Step 2: Paste your API key
Replace `"your-api-key"` in the code with your actual key from Google.

---

### Step 3: Run the Flask webhook
In the terminal:
    python chatbot_webhook.py

Flask will start on:
    http://127.0.0.1:5000

---

### Step 4: Run ngrok in a second terminal
    ngrok http 5000

This will give you a public HTTPS URL like:
    https://abcd1234.ngrok-free.app

---

### Step 5: Connect Dialogflow

1. Go to Dialogflow → Fulfillment
2. Enable Webhook
3. Paste your ngrok URL + `/webhook`
   Example:
   https://abcd1234.ngrok-free.app/webhook
4. Click Save

---

### Step 6: Setup a Fallback Intent

1. Create a new intent: `Fallback to Gemini`
2. Set it as fallback
3. Enable webhook call
4. Remove all static responses
5. Save

---

### Step 7: Test It

Go to the test console in Dialogflow and type:
    Recommend a gaming phone

You should get a Gemini-generated answer.
Check your Flask terminal to see logs.

---

## Notes

- Dialogflow webhook timeout = 5 seconds
- Use `max_output_tokens=100` to speed up Gemini replies
- Always keep **both Flask and ngrok terminals** running while testing
- Use `ngrok config add-authtoken <your-token>` once to avoid auth errors
