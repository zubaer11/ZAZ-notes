from django.shortcuts import render, redirect
from .models import Contact
from .models import Subscribe
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        email_id = request.POST['subscribed']
        subscribe = Subscribe(email=email_id)
        subscribe.save()
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name_id']
        email = request.POST['email_id']
        phone = request.POST['phone_id']
        s_of_i = request.POST['subject_issue']  # subject_of_issue
        describing_the_problem = request.POST['problem']
        if len(name) < 3 or len(email) < 12 or len(phone) < 11 or len(s_of_i) < 4 or len(describing_the_problem) < 10:
            messages.warning(request, 'Something went wrong. Please fill the form correctly and then resubmit it ')
        else:
            contact = Contact(user_name=name, contact_mail=email, contact_number=phone, subject_of_issue=s_of_i,
                              issue=describing_the_problem)
            contact.save()
            messages.success(request, "We will contact with you soon")

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    return render(request, 'home/under_construction.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username_id']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email_id']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        #to add in groups automatically
        group = Group.objects.get(name= 'test')

        # will check the pass match or not
        if len(username) > 20:
            messages.warning(request, 'username must be less then 15 charecters')
            return redirect('/signup/')

        #check if the user_name is already used or not
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already in use')
            return redirect('/signup/')


        if not username.isalnum():
            messages.warning(request, 'Special charecters are not allowed in username ')
            return redirect('/signup/')

        if password != confirm_password:
            messages.warning(request, "Password does not match.Please try again")
            return redirect('/signup/')

        # create user
        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstName
        my_user.last_name = lastName
        my_user.is_staff = True
        my_user.groups.add(group)
        my_user.save()
        return redirect("/con_signup")

    return render(request, 'home/signup.html')


def handle_login(request):
    if request.method == 'POST':
        log_user = request.POST['loginUserName']
        log_pass = request.POST['loginUserPassword']

        # authenticate
        user = authenticate(username=log_user, password=log_pass)

        if user is not None:
            # messages.success(request,"You have successfully logged in")
            # time.sleep(5)
            login(request, user)
            return redirect("/con_login/")
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("/login/")

    return render(request, 'home/login.html')


def handle_logout(request):
    logout(request)
    return redirect("/con_logout/")


def con_signup(request):
    return render(request, 'home/con_signup.html')

def con_login(request):
    return render(request, 'home/con_login.html')

def con_logout(request):
    return render(request, 'home/con_logout.html')

def login_shower(request):
    return render(request, 'home/index_backup.html')