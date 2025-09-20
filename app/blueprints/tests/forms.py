from app.forms import DataRequired, FlaskForm, StringField, SubmitField


class CreateUserForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()])
    submit = SubmitField("Registrar")
