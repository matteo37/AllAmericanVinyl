from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from vinylSite.models import Contact
from vinylSite.forms import ContactForm


@processor_for(Contact)
def author_form(request, page):
    form = ContactForm()
    if request.method == "POST":
        import pdb; pdb.set_trace()  # XXX BREAKPOINT
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form processing goes here.
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    return {"contact_form": form, "page":page}
