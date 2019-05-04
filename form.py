from wtforms import Form, BooleanField, StringField, PasswordField, validators

class Comparacao(Form):
    compare1 = StringField('Compare 1', [validators.Length(min=3, max=25)])
    compare2 = StringField('Compare 2', [validators.Length(min=3, max=25)])