from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)

# Mock Database
assignments = []
COMMISSION_RATE = 0.20 # 20% platform fee

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/calculate-earning', methods=['POST'])
def calculate_earning():
    """
    Logic for 20% commission calculation
    """
    data = request.json
    amount = float(data.get('amount', 0))
    platform_fee = amount * COMMISSION_RATE
    writer_earning = amount - platform_fee
    
    return jsonify({
        "total": amount,
        "platform_fee": platform_fee,
        "writer_earning": writer_earning
    })

@app.route('/submit-request', methods=['POST'])
def submit_request():
    """
    Handles Student and Writer registration/requests
    """
    user_data = {
        "type": request.form.get('type'), # student or writer
        "name": request.form.get('name'),
        "phone": request.form.get('phone'),
        "subject": request.form.get('subject'),
        "details": request.form.get('message')
    }
    
    # Yahan hum database (jaise SQLite ya MongoDB) mein data save kar sakte hain
    assignments.append(user_data)
    
    # Simple success response
    return f"Dhanyawad {user_data['name']}! StudyPro India team aapse WhatsApp par sampark karegi."

if __name__ == '__main__':
    # Isko run karne ke liye 'python app.py' command use karein
    app.run(debug=True)
