from models import User, Note
from flask_marshmallow import Marshmallow

ma= Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= User
        load_instance = True
        fields =('id', 'email', 'password', 'first_name', 'last_name')

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "user_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("user_list"),
        }
    )
