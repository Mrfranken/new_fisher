from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, DataRequired, NumberRange, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    nickname = StringField(validators=[DataRequired(message='name can not be empty'),
                                       Length(2, 10, message='at least 2, max 10')])
    email = StringField(validators=[DataRequired(message='email can not be empty'),
                                    Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='password can not be empty'),
                                         Length(2, 10, message='密码最少2，最多10')])

    # 1. 自定义验证器
    # 2. 使用模型进行数据库的查询
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('user is exist')


class LoginForm(Form):
    # nickname = StringField(validators=[DataRequired(message='name can not be empty'),
    #                                    Length(2, 10, message='at least 2, max 10')])
    email = StringField(validators=[DataRequired(message='email can not be empty'),
                                    Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='password can not be empty'),
                                         Length(2, 10, message='密码最少2，最多10')])

    # 1. 自定义验证器
    # 2. 使用模型进行数据库的查询
    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('user is exist')
