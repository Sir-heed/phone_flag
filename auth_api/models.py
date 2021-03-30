import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, active=False, admin=False, staff=False):
        if not email:
            raise ValueError("Users must have an email address")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = staff
        user_obj.admin = admin
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff_user(self, email, password):
        user = self.create_user(email, password=password, staff=True)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password, staff=True, admin=True)
        return user

class User(AbstractBaseUser):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=250, unique=True)
    sex = models.CharField(max_length=7, choices=SEX, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    # REQUIRED_FIELDS = ['phoneNumber','dateTimeCreated']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.staff

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Vendor(models.Model):
    vendor_id = models.UUIDField(default = uuid.uuid4, editable = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.company

class DeviceOwner(models.Model):
    owner_id = models.UUIDField(default = uuid.uuid4, editable = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'