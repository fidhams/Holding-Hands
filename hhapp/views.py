from django.shortcuts import render,redirect
from .forms import DonorForm, VolunteerForm, DonateForm, DoneeForm, NeedsForm, EventsForm
from .models import Donee, Donor, Donate, Volunteer, Needs, Events
from django.contrib import messages
# from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login



# Create your views here.
def contactus(request):
    approved_donees = Donee.objects.filter(approved='Yes')
    context={'approved_donees': approved_donees}
    return render(request, 'contactus.html',context)


def home(request):
    events= Events.objects.all
    context={'events':events}
    return render(request, 'home.html',context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user is a donor
        try:
            donor = Donor.objects.get(email=email)
            if donor.password == password:
                request.session['user_email'] = email
                return redirect('user')
            else:
                messages.error(request, 'Invalid password.')
                #return render(request, 'login.html')
        except Donor.DoesNotExist:
            pass

        # Check if the user is a donee
        try:
            donee = Donee.objects.get(email=email)
            if donee.password == password:
                if donee.approved == 'Yes':
                    request.session['user_email'] = email
                    return redirect('orghome')
                else:
                    messages.error(request, 'Your account has not been approved yet.')
            else:
                messages.error(request, 'Invalid password.')
        except Donee.DoesNotExist:
            messages.error(request, 'Email not found.')

    return render(request, 'login.html')



#user1 signup...
def signup(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = DonorForm()
    return render(request, 'signup.html', {'form': form})



#org signup...
def orgsignup(request):
    success = False
    if request.method == 'POST':
        form = DoneeForm(request.POST)
        if form.is_valid():
            donee = form.save(commit=False)
            donee.approved = 'No'  # Set approved to 'No' by default
            donee.save()
            messages.success(request, "Your request has been submitted successfully. You'll soon receive a mail for approval.")
            success = True
            return render(request, 'home.html', {'form': form, 'success': success})  # Redirect to a view that lists donees
    else:
        form = DoneeForm()
    return render(request, 'orgsignup.html', {'form': form})




#org home...
@login_required
def orghome(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')  # Redirect to login if user is not logged in
    donee = Donee.objects.get(email=email)
    needs = Needs.objects.filter(donee=email)
    events = Events.objects.filter(donee=email)
    
    context = {
        'donee': donee,
        'needs': needs,
        'events': events,
    }
    request.session['user_email'] = email
    return render(request, 'orghome.html', context)


#org need...
@login_required
def itemsreq(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')  # Redirect to login if user is not logged in
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        count = request.POST.get('count')
        status = request.POST.get('status')

        donee = Donee.objects.get(email=email)
        need = Needs(
            name=name,
            category=category,
            count=count,
            status=status,
            donee=donee
        )
        need.save()
        return redirect('orghome')  # Redirect to a view that lists needs
    else:
        return render(request, 'itemsreq.html')

#org events...
@login_required
def volunteerreq(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')  # Redirect to login if user is not logged in
    if request.method == 'POST':
        name=request.POST.get('name')
        venue=request.POST.get('venue')
        date=request.POST.get('date')
        category = request.POST.get('category')
        description = request.POST.get('description')

        donee = Donee.objects.get(email=email)
        event = Events(
            name=name,
            venue=venue,
            date=date,
            category=category,
            description=description,
            donee=donee
        )
        event.save()
        return redirect('orghome')  # Redirect to a view that lists events
    else:
        return render(request, 'volunteerreq.html')

#view...
def viewd(request):
    donations= Donate.objects.all
    context={'donations':donations}
    return render(request, 'viewd.html',context)


#user home...
@login_required
def user(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')  # Redirect to login if user is not logged in
    donor = Donor.objects.get(email=email)
    donations = Donate.objects.filter(donor=email)
    volunteers = Volunteer.objects.filter(donor=email)
    
    context = {
        'donor': donor,
        'donations': donations,
        'volunteers': volunteers,
    }
    request.session['user_email'] = email
    return render(request, 'user.html', context)

#user1 donate...
@login_required
def userdonate(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login') 
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        count = request.POST.get('count')
        image = request.FILES.get('image')
        #email = request.POST.get('email')

        donor = Donor.objects.get(email=email)
        donation = Donate(
            name=name,
            category=category,
            count=count,
            image=image,
            donor=donor
        )
        donation.save()
        return redirect('user')  # Redirect to the user's home page after saving

    return render(request, 'userdonate.html')

#user1 volunteer...
@login_required
def uservolunteer(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('login') 
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        #email = request.POST.get('email')

        donor = Donor.objects.get(email=email)
        volunteer = Volunteer(
            volunteer_category=category,
            volunteer_details=description,
            donor=donor
        )
        volunteer.save()
        return redirect('user')  # Redirect to the user's home page after saving

    return render(request, 'uservolunteer.html')
