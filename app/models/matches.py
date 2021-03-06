from .db import db


class Match(db.Model):

    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    user_matched = db.Column(db.Boolean, default=False)
    group_matched = db.Column(db.Boolean, default=False)

    user = db.relationship('User', lazy='select')
    group = db.relationship('Group', lazy='select')

    def to_dict(self):

        return {
            'id': self.id,
            'user_id': self.user_id,
            'group_id': self.group_id,
            'user_matched': self.user_matched,
            'group_matched': self.group_matched,
            'user': self.user.username,
            'group': {'group_name': self.group.name, 'group_owner': self.group.user.group_owner()}
        }
