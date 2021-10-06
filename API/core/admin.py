
# the module name is app_name.models
from django.contrib import admin
from .models import CustomUser
# Register your models here.




from django.contrib import admin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin




admin.site.register(CustomUser)

