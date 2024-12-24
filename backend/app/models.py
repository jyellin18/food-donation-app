from backend.app import db

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(80), nullable = False)
    amount = db.Column(db.Float, nullable = False)
    time_stamp = db.Column(db.DateTime, default = db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "donor_name": self.donor_name,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()
        }