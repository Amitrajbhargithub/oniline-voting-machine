from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')
admin.site.register(contact,contactAdmin)


class profileAdmin(admin.ModelAdmin):
    list_display=('name',"mobile","email","passwd",'ppic','address')
admin.site.register(profile,profileAdmin)

class partiesAdmin(admin.ModelAdmin):
    list_display=('id',"name","ppic","pdate")
admin.site.register(parties,partiesAdmin)


class uregisterAdmin(admin.ModelAdmin):
    list_display=('uname',"ugender","udob","umobile",'uadhar','upasswd','ustate','ucity','rdate','upic')
admin.site.register(uregister,uregisterAdmin)


class upcomingelectionAdmin(admin.ModelAdmin):
    list_display=('id',"etitle","edes","edate","city","state")
admin.site.register(upcomingelection,upcomingelectionAdmin)


class voteAdmin(admin.ModelAdmin):
    list_display=('aadhar',"vparty","vdate")
admin.site.register(vote,voteAdmin)

class pollAdmin(admin.ModelAdmin):
    list_display=('pname',"aadhar","comment","pdate")
admin.site.register(poll,pollAdmin)


