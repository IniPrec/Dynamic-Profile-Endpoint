from flask import Flask, jsonify
import requests
import os
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/me", methods=["GET"])
def get_profile():
    try:
        # This will fetch a random cat fact from https://catfact.ninja/fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cat are mysterious creatures.")
    except Exception as e:
        # A fallback message in case the API fails
        cat_fact = "Unable to fetch cat fact at the moment."

    # The current UTC time in ISO 8601 format
    current_time = datetime.now(timezone.utc).isoformat()

    data = {
        "status": "success",
        "user": {
            "email": "omoprepre67@gmail.com",
            "name": "Precious Inioluwa Oyebanjo",
            "stack": "Python/Flask"
        },
        "timestamp": current_time,
        "fact": cat_fact
    }

    return jsonify(data), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)