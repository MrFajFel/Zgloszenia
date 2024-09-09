from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from app.models import User


class RepUsers(ListView):
    queryset = User.objects.all()
    context_object_name = 'Users'
    paginate_by = 9
    template_name = 'skargi.html'

def reported(request, year, month, day,hour,minute,second):
    rep = get_object_or_404(User,
                                zgloszono__year=year,
                                zgloszono__month=month,
                                zgloszono__day=day,
                                zgloszono__hour=hour,
                                zgloszono__minute=minute,
                                zgloszono__second=second,
                                )
    return render(request, "dokladnyOpis.html",
                  {'rep': rep, })
# Create your views here.
