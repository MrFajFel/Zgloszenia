from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from app.form import LogForm,SkForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from rest_framework.response import Response


from app.models import User,MyAdmin


class RepUsers(ListView):
    queryset = User.objects.all().order_by('-zgloszono')
    context_object_name = 'Users'
    paginate_by = 3
    template_name = 'skargi.html'

    def get(self, request, *args, **kwargs):
        # Sprawdzenie, czy ciasteczko 'Zalogowany' ma wartość '1'
        if request.COOKIES.get('Zalogowany') != '1':
            # Jeśli ciasteczko nie istnieje lub ma inną wartość, przekierowanie na stronę logowania
            return redirect('app:logowanie')

        # Jeśli ciasteczko jest poprawne, kontynuuj z renderowaniem widoku
        return super().get(request, *args, **kwargs)


def logowanie(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            # Sprawdzenie danych logowania
            for aadmin in MyAdmin.objects.all():
                if (
                        form.cleaned_data['nickname'] == aadmin.nickname and
                        form.cleaned_data['password'] == aadmin.password
                ):
                    # Tworzenie odpowiedzi z przekierowaniem
                    response = HttpResponseRedirect('/base/')  # lub reverse('app:info')
                    response.set_cookie("Zalogowany", '1')  # Ustawienie ciasteczka
                    return response

            # Jeśli dane logowania są niepoprawne, przekaż błąd
            form.add_error(None, "Niepoprawne dane logowania")

    else:
        form = LogForm()

    return render(request, 'logowanie.html', {'form': form})



def skarga(request):
    if request.method == 'POST':
        form = SkForm(request.POST)
        if form.is_valid():  # sprawdzenie czy formularz jest wlasciwy
            user = form.save(commit=False)
            user.save()
            return redirect('app:skarga')
    else:
        form = SkForm()
    return render(request, 'napiszSkarge.html', {'form': form})


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
