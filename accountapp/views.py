from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('next')
        request.Get.get('next')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # data_list = NewModel.objects.all()
        # return render(request, 'accountapp/hello_world.html',
        #               context={'data_list': data_list})
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name ='accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'   #이미 존재하는 유저에 대한 접근이 필요할떄 사용
    template_name = 'accountapp/detail.html'

has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
