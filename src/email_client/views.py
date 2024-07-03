from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required


from django.views.generic import FormView

from django.core.mail import send_mail

from .forms import InboxForm

from .models import Email


# Create your views here.


class InboxView(FormView):
    form_class = InboxForm
    template_name = "email_client/inbox_page.html"
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        recipient = form.cleaned_data["email"]

        send_mail(
            subject="Received contact form submission",
            message=message,
            from_email=None,
            recipient_list=[recipient],
            fail_silently=False
        )

        obj = Email(
            subject=subject,
            message=message,
            email=recipient
        )
        obj.save()

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'email_client/login.html'
    fields = '__all__'

    # redirect_authenticated_user = True  # This is forcing authenticated users to a specified URL

    def get_success_url(self):
        return reverse_lazy('inbox')
