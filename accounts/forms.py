from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


user = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = ('email', 'is_staff', 'is_active',)
