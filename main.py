from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_payload():
    data = request.get_json()
    payload = data.get('preferences', {}).get('custom', {}).get('payload', '')
    try:
        decoded = base64.b64decode(payload).decode('utf-8')
        steps = [step.strip() for step in decoded.split(';')]
        print("📥 تعليمات مستلمة:")
        for i, step in enumerate(steps, 1):
            print(f"Step {i}: {step}")
        return jsonify({"status": "success", "steps": steps})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run()
