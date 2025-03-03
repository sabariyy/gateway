from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Simulated UPI ID
UPI_ID = "sabarinath.s@fam"

# Simulated payment status
payment_status = {
    "status": "pending",
    "amount": 0,
    "upi_id": UPI_ID,
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    amount = float(request.form['amount'])
    payment_status["amount"] = amount
    payment_status["status"] = "initiated"
    return jsonify({"message": "Payment initiated. Please confirm payment on your UPI app.", "upi_id": UPI_ID})

@app.route('/check_payment_status', methods=['GET'])
def check_payment_status():
    # Simulate payment confirmation after 5 seconds
    if payment_status["status"] == "initiated":
        payment_status["status"] = "completed"
        return jsonify({"status": "completed", "message": "Payment received!", "amount": payment_status["amount"]})
    else:
        return jsonify({"status": "pending", "message": "Payment not yet received."})

if __name__ == '__main__':
    app.run(debug=True)
