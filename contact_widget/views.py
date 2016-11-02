from django.conf import settings
from django.http import HttpResponse
from django.core.mail import (send_mail, BadHeaderError)
from django.views.decorators.csrf import csrf_exempt
from contact_widget.models import Contact


@csrf_exempt
def contact_view(request):
    if request.method == 'POST' and request.is_ajax():
        from_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject + " from {}".format(from_email),
                message,
                from_email,
                [settings.EMAIL_HOST_USER]
            )
            contact_model = Contact.objects.create(
                email=from_email,
                subject=subject,
                message=message
            )
            contact_model.save()

        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        success_message = ("Thankyou, We appreciate that you've "
                           "taken the time to write us. "
                           "We'll get back to you very soon. "
                           "Please come back and see us often.")
        return HttpResponse(success_message)
    else:
        return HttpResponse("Something went wrong!")
