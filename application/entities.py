from application import db

class User(db.Model):
    # New instance instantiation procedure
    def __init__(self, name, userName, email, password):
        self.name = name
        self.userName = userName
        self.email = email
        self.password = password
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    # User Full Name
    name = db.Column(db.String(128),  nullable=False)
    # username
    userName = db.Column(db.String(128),  nullable=False)
    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False,
                      unique=True)
    password = db.Column(db.String(192),  nullable=False)


    def __repr__(self):
        return '<User %r>' % (self.name)

class Contact(db.Model):
    # New instance instantiation procedure
    def __init__(self, name, email, description):
        self.name = name
        self.email = email
        self.description = description
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    # User Full Name
    name = db.Column(db.String(128),  nullable=False)
    # username
    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False,
                      unique=True)
    description = db.Column(db.String(250),  nullable=False)


    def __repr__(self):
        return '<Contact %r>' % (self.name)