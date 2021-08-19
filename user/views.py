from django.shortcuts import render,redirect
from .models import resume_details
from .forms import createResumeForm,updateResumeForm,messageForm
from django.contrib import messages
import uuid
from urllib.parse import urlencode


def message(request):
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully. It will be attended to as soon as possible")
            return redirect('message')
        else:
            print(form)
            return render(request, 'index.html', {'form':form})
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        form = createResumeForm(request.POST)
        if form.is_valid():
            resume_form = form.save(commit=False)
            resume_form.reference_id = uuid.uuid4().hex[:11]
            resume_form.save()
            messages.success(request, f"Resume created successfully, Your reference ID is {resume_form.reference_id}")
            return redirect("signup")
        else:
            return render(request, 'signup.html', {'form': form})

    return render(request, 'signup.html')


def edit_resume(request):
    #get the details attached with the reference ID
    try:
        # print(request.headers)
        user = resume_details.objects.get(reference_id = request.GET.get("reference_id"))
        if request.method == "POST":
            form = updateResumeForm(request.POST, instance=user)
            print(form)
            if form.is_valid():
                form_save = form.save(commit = False)
                form_save.reference_id = user.reference_id
                form_save.save()
                messages.success(request, 'Details updated successfully')
                return redirect("signup")
            else:
                return render(request, 'edit_resume.html', {'resume':user,'form': form})
        return render(request, 'edit_resume.html', {'resume':user})
    except resume_details.DoesNotExist:
        messages.error(request, "Your resume can't be found, Please create one")
        return redirect('signup')
