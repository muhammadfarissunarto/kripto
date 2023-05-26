from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from .models import Record
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegistrationView(CreateView):
    model = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm


# class RecordListView2(LoginRequiredMixin, ListView):
#     model = Record
#     template_name = 'website\listview.html'
#     context_object_name = 'Records'
    
class RecordListView(ListView):
    model = Record
    template_name = 'website\listview.html'
    context_object_name = 'records'

    def decrypt(self, text, shift):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

    def get_queryset(self):
        queryset = super().get_queryset()
        shift = 3  # Shift value used during encryption
        decrypted_records = []
        for record in queryset:
            decrypted_record = {
                'created_at': record.created_at,
                'name': self.decrypt(record.name, shift),
                'email': self.decrypt(record.email, shift),
                'phone': record.phone,
                'address': self.decrypt(record.address, shift),
                'city':record.city,
                'zipcode': record.zipcode,
                'id' : record.id,
            }
            decrypted_records.append(decrypted_record)
        return decrypted_records

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    template_name = 'website\createview.html'
    fields = "__all__"
    success_url = reverse_lazy('record')

