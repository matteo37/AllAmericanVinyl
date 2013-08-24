from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from vinylSite.models import Contact
from vinylSite.forms import ContactForm
from django.core.mail import send_mail
from smtplib import SMTPException

@processor_for(Contact)
def author_form(request, page):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form processing goes here.
            msg = form.cleaned_data.get('msg')
            subject = form.cleaned_data.get('subject')
            name = form.cleaned_data.get('name')
            from_email = form.cleaned_data.get('email')
            to_email = ['bryson.thor@gmail.com']
            import pdb; pdb.set_trace()  # XXX BREAKPOINT
            try:
                send_mail(subject, msg, from_email, to_email, fail_silently=False)
                redirect = request.path + "?sent=true"
            except SMTPException:
                redirect = request.path + "?sent=false"
            return HttpResponseRedirect(redirect)
    return {"contact_form": form, "page":page}
