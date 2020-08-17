from django.shortcuts import render, redirect
from django.views.generic import View
from home.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from home.models import File
from django.views import generic
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.

def dashboard(request):
    j = k = l = m = n = o = p = 0
    # counting unmoved files by ssg
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_ssg and not file.moved_from_ssg:
                j += 1
    except File.DoesNotExit:
        j = 0
    # counting unread files by perm sec cas
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_perm_sec_cas and not file.moved_from_perm_sec_cas:
                k += 1
    except File.DoesNotExit:
        k = 0
    # counting unmoved files by perm sec political
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_perm_sec_political and not file.moved_from_perm_sec_political:
                l += 1
    except File.DoesNotExit:
        l = 0
    # counting unmoved files by perm sec general admin
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_perm_sec_general_admin and not file.moved_from_perm_sec_general_admin:
                m += 1
    except File.DoesNotExit:
        m = 0
    # counting unmoved files by director internal affairs
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_director_internal_affairs and not file.moved_from_director_internal_affairs:
                n += 1
    except File.DoesNotExit:
        n = 0
    # counting unmoved files by director security
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_director_security and not file.moved_from_director_security:
                o += 1
    except File.DoesNotExit:
        o = 0
    # counting unmoved files by director cabinet affairs
    try:
        all_files = File.objects.all()
        for file in all_files:
            if file.moved_to_director_cabinet_affairs and not file.moved_from_director_cabinet_affairs:
                p += 1
    except File.DoesNotExit:
        p = 0
    context = {'ssg_unmoved': j, 'perm_sec_cas_unmoved': k, 'perm_sec_political_unmoved': l,
               'perm_sec_general_admin_unmoved': m, 'director_internal_affairs_unmoved': n,
               'director_security_unmoved': o, 'director_cabinet_affairs_unmoved': p}
    return render(request, 'secretary/s_dashboard.html', context)


class FileIndexView(generic.ListView):
    template_name = 'secretary/history.html'
    context_object_name = 'all_files'

    def get_queryset(self):
        return File.objects.all()


class FileDetailView(generic.DetailView):
    model = File
    template_name = 'home/detail.html'


def s_dashboard(request):
    return render(request, 'secretary/s_dashboard.html')


def upload(request):
    return render(request, "secretary/upload.html")


def comment(request, file_id, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        file = File.objects.get(pk=file_id)
        comment1 = request.POST['comment']
        date = datetime.today().strftime('%Y-%m-%d')
        comment1 = date + '\n' + comment1

        def add_comment(designation, new_comment, initial_comment_from_user):
            new_comment = 'To: ' + designation + '\n' + new_comment

            if initial_comment_from_user is None:
                initial_comment_from_user = new_comment

            else:
                new_comment = str(initial_comment_from_user) + '\n\n' + str(new_comment)
                initial_comment_from_user = new_comment
                return initial_comment_from_user
        # ssg comment
        if user.profile.ssg:
            position = request.POST['position']
            new_comment = add_comment(position, comment1, file.comment_from_ssg)
            file.comment_from_ssg = new_comment
            file.moved_from_ssg = True
            # when file is directed to perm sec cas
            if position == "perm sec cas":
                file.moved_to_perm_sec_cas = True
                file.moved_from_perm_sec_cas = False
            # when file is directed to perm sec political
            elif position == "perm sec political":
                file.moved_to_perm_sec_political = True
                file.moved_from_perm_sec_political = False
            # when file is directed to perm sec general admin
            elif position == "perm sec general admin":
                file.moved_to_perm_sec_general_admin = True
                file.moved_from_perm_sec_general_admin = False
            # wrong choice
            else:
                return HttpResponseRedirect(reverse('secretary:detail'), args=(file.id,))
            file.save()
        # perm sec cas comment
        elif user.profile.perm_sec_cas:
            file.moved_from_perm_sec_cas = True
            position = request.POST['position']
            new_comment = add_comment(position, comment1, file.comment_from_perm_sec_cas)
            file.comment_from_perm_sec_cas = new_comment
            # when file is directed to director internal affairs
            if position == "director internal affairs":
                file.moved_to_director_internal_affairs = True
                file.moved_from_director_internal_affairs = False
            # when file is directed to director security
            elif position == "director security":
                file.moved_to_director_security = True
                file.moved_from_director_security = False
            # when file is directed to director cabinet affairs
            elif position == "director cabinet affairs":
                file.moved_to_director_cabinet_affairs = True
                file.moved_from_director_cabinet_affairs = False
            elif position == "ssg":
                file.moved_from_ssg = False
            # wrong choice
            else:
                return HttpResponseRedirect(reverse('secretary:detail'), args=(file.id,))
            file.save()
        # perm sec political comment
        elif user.profile.perm_sec_political:
            file.comment_from_perm_sec_political = comment1
            file.moved_from_perm_sec_political = True
            file.save()
        # perm sec general admin comment
        elif user.profile.perm_sec_general_admin:
            file.comment_from_perm_sec_general_admin = comment1
            file.moved_from_perm_sec_general_admin = True
            file.save()
        # director of security comment
        elif user.profile.director_security:
            new_comment = add_comment('Perm. Sec. (CAS)', comment1, file.comment_from_director_security)
            file.comment_from_director_security = new_comment
            file.moved_from_director_security = True
            file.moved_from_perm_sec_cas = False
            file.save()
        # director of internal affairs comment
        elif user.profile.director_internal_affairs:
            new_comment = add_comment('Perm. Sec. (CAS)', comment1, file.comment_from_director_internal_affairs)
            file.comment_from_director_internal_affairs = new_comment
            file.moved_from_director_internal_affairs = True
            file.moved_from_perm_sec_cas = False
            file.save()
        # director of cabinet affairs comment
        elif user.profile.director_cabinet_affairs:
            new_comment = add_comment('Perm. Sec. (CAS)', comment1, file.comment_from_director_cabinet_affairs)
            file.comment_from_director_cabinet_affairs = new_comment
            file.moved_from_director_cabinet_affairs = True
            file.moved_from_perm_sec_cas = False
            file.save()
        else:
            return redirect('secretary:s_dashboard')
    return redirect('secretary:s_dashboard')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(None)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('secretary:s_dashboard'))
        messages.error(request, 'invalid username or password')
        return render(request, self.template_name, {'form': form})


class FileCreate(CreateView):
    model = File
    fields = ['file_name', 'file', 'date_of_file', 'comment_from_secretary']

    def get_form(self, form_class=None):
        form = super(FileCreate, self).get_form()
        form.fields['date_of_file'].widget = SelectDateWidget()
        return form


def append_file_no(request, file_id):
    file = File.objects.get(pk=int(file_id))
    year = file.date_of_file.strftime('%Y')
    file.file_number = 'ssg/' + str(year) + '/' + str(file_id)
    file.moved_to_ssg = True
    file.save()
    return redirect('secretary:s_dashboard')
