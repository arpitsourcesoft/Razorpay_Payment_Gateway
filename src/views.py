from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import razorpay
from razorpay_bot.settings import API_KEY, SECURE_KEY, EMAIL_HOST_USER

from src.models import Car


# Create your views here.
def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        email = request.POST.get("email")
        client = razorpay.Client(auth=(API_KEY, SECURE_KEY))
        payment = client.order.create(
            {'amount': amount, 'currency': "INR", "payment_capture": '1'})
        print('payment: ', payment)

        car = Car(name=name, amount=amount,
                  email=email, payment_id=payment["id"])
        car.save()
        print('car: ', car)
        return render(request, 'index.html', {'payment': payment})

    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = (request.POST)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = Car.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html')

        send_mail("Your Payment has been Received", msg_plain, EMAIL_HOST_USER,
                  [user.email], html_message=msg_html
                  )

    return render(request, "success.html")
