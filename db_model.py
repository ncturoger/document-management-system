from database import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256, collation="utf8_general_ci"), nullable=False)
    content = db.Column(db.Text(collation="utf8_general_ci"), nullable=False)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title %r>' % self.title