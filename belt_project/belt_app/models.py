from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
import bcrypt


from django.db.models.fields.related import ForeignKey

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(User.objects.filter(username=postData['username'])) > 0:
            errors['existe'] = "Username already registered"
        else:
            if len(postData['name']) == 0:
                errors['name'] = "Name required"
            if len(postData['username']) == 0:
                errors['username'] = "Username required"
            if len(postData['password']) < 8:
                errors['password'] = "Password must have 8 characters minimum"

            validate_pass = self.compare_password(postData['password'],postData['password_conf'])
            if len(validate_pass) > 0:
                errors['password'] = validate_pass

        return errors

    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def validate_login(self, password, user ):
        errors = {}
        if len(user) > 0:
            pw_hash = user[0].password

            if bcrypt.checkpw(password.encode(), pw_hash.encode()) is False:
                errors['wrong_pass'] = "Password is wrong"
        else:
            errors['invalid_user'] = "User does not exist"
        return errors
    
    def compare_password(self,password, password_conf):
        if password != password_conf:
            return "Passwords does not match"
        else:
            return ""


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date= models.DateField()
    end_date= models.DateField()
    users= ForeignKey(User, on_delete=CASCADE, related_name="trips")

