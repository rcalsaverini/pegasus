from flask_wtf import FlaskForm
from pegasus.equity.entities import RSUGrant, OptionGrant
from wtforms import StringField, IntegerField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired


class RSUForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    date = DateField("date", validators=[DataRequired()])
    shares = IntegerField("shares", validators=[DataRequired()])
    vesting = IntegerField("vesting", validators=[DataRequired()])
    cliff = IntegerField("cliff")
    submit_rsu = SubmitField("submit_rsu")

    def to_grant(self):
        return RSUGrant(
            self.name.data,
            self.shares.data,  # type: ignore
            self.date.data,  # type: ignore
            self.cliff.data or 0,
            self.vesting.data,  # type: ignore
        )


class OptionForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    date = DateField("date", validators=[DataRequired()])
    shares = IntegerField("shares", validators=[DataRequired()])
    vesting = IntegerField("vesting", validators=[DataRequired()])
    cliff = IntegerField("cliff")
    strike = FloatField("strike")
    submit_option = SubmitField("submit_option")

    def to_grant(self):
        return OptionGrant(
            self.name.data,
            self.shares.data,  # type: ignore
            self.date.data,  # type: ignore
            self.cliff.data or 0,
            self.vesting.data,  # type: ignore
            self.strike.data,  # type: ignore
        )
