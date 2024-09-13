from datetime import datetime
from Portal import db

class SoilDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.String(80), nullable=False)
    moisture = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<SoilDB {self.temperature}, {self.moisture}>"
