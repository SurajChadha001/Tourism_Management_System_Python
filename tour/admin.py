from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'password_display')  # Add hashed password column

    def password_display(self, obj):
        return obj.password  # Display hashed password

    password_display.short_description = "Password (Hashed)"  # Set column name

# Unregister default User admin
admin.site.unregister(User)

# Register new CustomUserAdmin
admin.site.register(User, CustomUserAdmin)
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id','place','country','image','price_by_bus','price_by_Train','price_by_Flight',]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Fname', 'Lname', 'Email', 'gender', 'destination', 'status']  # Use 'id' directly
    list_filter = ['status']
    actions = ['approve_booking', 'decline_booking']

    def approve_booking(self, request, queryset):
        queryset.update(status='Approved')
    approve_booking.short_description = "Mark selected bookings as Approved"

    def decline_booking(self, request, queryset):
        queryset.update(status='Declined')
    decline_booking.short_description = "Mark selected bookings as Declined"
    
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['id','first_Name','last_Name','email','subject','message']

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['id','user','topic','image','blog']

@admin.register(User_Profile)
class Profile(admin.ModelAdmin):
    list_display = ['id','address','mobile','image']
