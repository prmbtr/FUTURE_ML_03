from flask import Flask, request, Response
import google.generativeai as genai
import json
from conf import gemini_key

app = Flask(__name__)
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    user_query = req.get("queryResult", {}).get("queryText", "")

    try:
        gemini_response = model.generate_content(
            user_query,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=100
            )
        )
        reply_text = gemini_response.text.strip()

    except Exception as e:
        print("Gemini error:", e)
        reply_text = "Sorry, I couldn’t process that. Please try again later."

    result = {
        "fulfillmentText": reply_text
    }

    return Response(json.dumps(result), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(port=5000)
