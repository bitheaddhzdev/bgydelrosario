from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name )
                user.save()
                messages.success(request,'You are now registered')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
    return redirect('index')

def dashboard(request):
    # test if user is admin. 
    # if request.user.is_superuser:
    #     messages.success(request, 'Hello Admin')

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def edit_profile(request):
    user_id = request.user.id
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            #get form values
            middle_name = request.POST['middle_name']
            house_num = request.POST['house_num']
            street = request.POST['street']
            zone = request.POST['zone']
            gender = request.POST['gender']
            religion = request.POST['religion']
            photo_main = request.FILES['photo_main']
            file_upload = request.FILES['file_upload']
            birthplace = request.POST['birthplace']
            bio = request.POST['bio']
        
        save_profile = UserProfile.objects.all().update(
                                middle_name=middle_name,
                                house_num=house_num,
                                street=street,
                                zone=zone,
                                gender=gender,
                                religion=religion,
                                photo_main=photo_main,
                                file_upload=file_upload,
                                bio=bio,
                                birthplace=birthplace)
        # save_profile.save()
        messages.success(request, 'Profile Saved!')
        return redirect('dashboard')
    else:
        return render(request, 'accounts/edit_profile.html') 

def view_profile(request):
    user_id = request.user.id
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    return render(request, 'accounts/view_profile.html', {'user' : user_profile})

