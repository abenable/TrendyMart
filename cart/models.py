import os
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='img', null=True)
    job_title = models.CharField(max_length=150, null=True)
    company_organization = models.CharField(max_length=150, null=True)
    bio = models.CharField(max_length=250, null=True)
    phone_number = models.CharField(max_length=150, null=True)
    Address = models.CharField(max_length=150, null=True)
    Gender = models.CharField(max_length=150, null=True, default='Prefer not to say', choices=(
        ('M', 'Male'), ('F', 'Female')))
    DoB = models.DateField(verbose_name='Date of Birth',
                           max_length=150, null=True, editable=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    def update_image(self, new_image):
        # Delete the old image file if it exists
        if self.image:
            old_image_path = self.image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        # Set the new image and save the model
        self.image = new_image
        self.save()
