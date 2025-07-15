from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    # Placeholder response
    return jsonify({"response": f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)
