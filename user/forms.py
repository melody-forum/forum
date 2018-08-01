from django.forms import ModelForm, forms, fields

from user.models import User


class RegisterForm(ModelForm):
  class Meta:
    model = User
    fields = ['nickname', 'password','age','sex','icon']
      # 密码长度控制
  password = fields.CharField(min_length=6,max_length=12)
  password2 = fields.CharField(max_length=128)

  #二次密码验证
  def clean_password2(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      password2 = cleaned_data.get('password2')
      if password != password2:
          raise forms.ValidationError('两次密码不一致')


