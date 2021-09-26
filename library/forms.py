from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput
from .models import Book


class DateType(DateInput):
    input_type = 'date'


class BookReturnForm(ModelForm):
    class Meta:
        model = Book
        fields = ['return_date']
        widgets = {'return_date': DateType}

    def clean(self):
        cleaned_data = super(BookReturnForm, self).clean()
        return_date = cleaned_data.get('return_date')
        print(cleaned_data)
        print(return_date)
        print(type(return_date))
        print(isinstance(return_date, date))
        if isinstance(return_date, date):
            if return_date < datetime.now().date():
                self.add_error(None, ValidationError(
                    'The date cannot be in the past!'))
        else:
            self.add_error(None, ValidationError(
                'invalid date'))
