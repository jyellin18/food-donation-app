from flask import request, jsonify
from backend.app import app, db
from backend.app.models import Donation #imports Donation class from the models file

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/greet', methods=['GET'])  
def greet():
    name = request.args.get('name', 'Guest')  
    return f"Hello, {name}!"


donations = 0

@app.route('/donate', methods=['POST'])
def donate():
    # Parse the JSON data from the request
    data = request.get_json()
    donor_name = data.get('donor_name', 'Anonymous')  # Default to 'Anonymous' if no name
    amount = data.get('amount')

    # Validate input
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid donation amount"}), 400

    # Create a new donation record
    donation = Donation(donor_name=donor_name, amount=amount)
    db.session.add(donation)  # Add to the database session
    db.session.commit()       # Commit the transaction

    return jsonify({
        "message": "Donation added successfully!",
        "donation": donation.to_dict()
    }), 201

@app.route('/donationstotal')
def donationstotal():
    return jsonify({"total donations": donations}), 200


@app.route('/initdb', methods=['GET'])
def init_db():
    db.create_all()  # This creates all tables defined in models.py
    return {"message": "Database initialized successfully!"}, 200