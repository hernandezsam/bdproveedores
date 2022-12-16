from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(64), index=True, nullable=False)
    razon_social = db.Column(db.String(64), index=True, nullable=False)
    cod_banco = db.Column(db.String(64), index=True, nullable=False)
    banco = db.Column(db.String(64), index=True, nullable=False)
    tipo_cta = db.Column(db.String(64), index=True, nullable=False)
    num_cta = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)