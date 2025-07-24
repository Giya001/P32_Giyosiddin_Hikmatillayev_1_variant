from django.shortcuts import render, redirect

from account.forms import CustomUserCreationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request,'account/register.html',context=context)


