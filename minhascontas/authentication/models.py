from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.aggregates import Max



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email musb be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Seuperuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)
        

class User(AbstractUser):
    GENDERS = (
        ("M", "MASCULINO"),
        ("F", "FEMININO"),
        ("O", "OUTRO")
    )
    username = None
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)

    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['birthday', 'gender']

    objects = UserManager()

    def __str__(self):
        return self.name

