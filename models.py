from vnwardatabase import db

class Data(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    branch = db.Column(db.String(15))
    rank = db.Column(db.String(20))
    grade = db.Column(db.String(15))
    first = db.Column(db.String(20))
    middle = db.Column(db.String(20))
    last = db.Column(db.String(20))
    city = db.Column(db.String(20))
    state = db.Column(db.String(2))
    panel = db.Column(db.String(4))
    birth = db.Column(db.String(10))
    start = db.Column(db.String(10))
    incident = db.Column(db.String(10))
    casualty = db.Column(db.String(10))
    age = db.Column(db.Integer)
    location = db.Column(db.String(60))
    remains = db.Column(db.String(60))
    type = db.Column(db.String(60))
    reason = db.Column(db.String(60))
    details = db.Column(db.String(60))

    def __repr__(self):
        # return f"ID: '{self.id}', First: '{self.first}', Last: '{self.last}'"
        return f"Data({self.id}, '{self.first}', '{self.last}')"