from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .forms import BookReturnForm
from .models import Book
from accounts.models import CustomUser


class StaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class StudentMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_staff


class BookOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().student == self.request.user


class AccountOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user


class NotBorrowedMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().student is None


class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    # paginate_by = 12


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    # add comments


class BookUpdateView(LoginRequiredMixin, StaffMixin, UpdateView):
    model = Book
    fields = ('title', 'category', 'img', 'description')
    template_name = 'library/book_edit.html'


class BookDeleteView(LoginRequiredMixin, StaffMixin, DeleteView):
    model = Book
    template_name = 'library/book_delete.html'
    success_url = reverse_lazy('book_list')


class BookCreateView(LoginRequiredMixin, StaffMixin, CreateView):
    model = Book
    template_name = 'library/book_new.html'
    fields = ('title', 'category', 'img', 'description')


class BookSearchView(ListView):
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(title__contains=self.request.GET.get('title'))


class BookBorrowView(LoginRequiredMixin, NotBorrowedMixin, StudentMixin, UpdateView):
    model = Book
    form_class = BookReturnForm
    template_name = 'library/book_borrow.html'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class BookReturnView(LoginRequiredMixin, StudentMixin, BookOwnerMixin, DetailView):
    model = Book

    def get_object(self):
        obj = super().get_object()
        if obj.student == self.request.user:
            obj.student = None
            obj.return_date = None
            obj.save()
            return obj


class BorrowListView(ListView):
    context_object_name = 'books'
    queryset = Book.objects.exclude(student=None)


class avaliableListView(ListView):
    context_object_name = 'books'
    queryset = Book.objects.filter(student=None)


class StudentListView(LoginRequiredMixin, StaffMixin, ListView):

    context_object_name = 'students'
    queryset = CustomUser.objects.filter(is_staff=False)
    template_name = 'library/student_list.html'


class StudentDetailView(LoginRequiredMixin, StaffMixin, DetailView):

    model = CustomUser
    template_name = 'library/student_detail.html'
    context_object_name = 'student'


class StudentUpdateView(LoginRequiredMixin, AccountOwnerMixin, UpdateView):
    model = CustomUser
    fields = ('username', 'email')
    template_name = 'library/student_edit.html'


class StudentBooksListView(LoginRequiredMixin, StudentMixin, ListView):
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(student=self.request.user)


class StudentSearchView(LoginRequiredMixin, StaffMixin, ListView):
    model = CustomUser
    context_object_name = 'students'
    template_name = 'library/student_list.html'

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.GET.get('name'))
