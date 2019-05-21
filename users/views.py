from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

# Create your views here.
@login_required
def profile(request):
    context = dict()
    if request.method == 'POST':
        context['user_update_form'] = UserUpdateForm(request.POST, instance=request.user)
        context['profile_update_form'] = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if context['user_update_form'].is_valid() and context['profile_update_form'].is_valid():
            context['profile_update_form'].save()
            context['user_update_form'].save()
            messages.success(request, _('Account updated.'))

            return redirect('users:profile')
    else:
        context['user_update_form'] = UserUpdateForm(instance=request.user)
        context['profile_update_form'] = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'account/profile.html', context)
