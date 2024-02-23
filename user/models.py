from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.name


class profile(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class parties(models.Model):
    name=models.CharField(max_length=300)
    ppic=models.ImageField(upload_to='static/profile/', default="")
    pdate=models.DateField()


class uregister(models.Model):
    uname = models.CharField(max_length=120)
    ugender = models.CharField(max_length=10)
    udob = models.DateField()
    umobile = models.CharField(max_length=20)
    uadhar = models.CharField(max_length=12, primary_key=True)
    upasswd = models.CharField(max_length=50)
    ustate = models.TextField(max_length=100)
    ucity = models.TextField(max_length=100)
    rdate = models.DateField()
    upic=models.ImageField(upload_to='static/profile/', default="")


class upcomingelection(models.Model):
    etitle=models.CharField(max_length=100)
    edes=models.TextField(max_length=5000)
    edate=models.DateField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.etitle


class vote(models.Model):
    aadhar=models.CharField(max_length=20)
    vparty=models.CharField(max_length=20)
    vdate=models.DateField()

class poll(models.Model):
    pname=models.CharField(max_length=50)
    aadhar=models.CharField(max_length=50)
    comment=models.TextField(max_length=5000)
    pdate=models.DateField()









