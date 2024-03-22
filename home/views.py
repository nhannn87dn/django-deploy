from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import EmailMessage

# Create your views here.
"""
Tạo một hàm = với tên của app đã tạo
"""
def index(request):
    template = loader.get_template('home_index.html')
    # Tạo một context chứa các biến muốn sử dụng trong template
    context = {
        'categories': {
            'id': 1, 
            'name': 'Mobile'
        },
    }
    # có thể dùng HttpResponse
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the Home Page.")

def sendmail(request):
    print('send mail')
    email = EmailMessage(
        subject='Hello Ngoc nhan form Python Django',
        body='<h2>Body <strong>goes</strong> here<h2>',
        from_email='ecshopvietnamese@gmail.com',
        to=['nhannn87@gmail.com'],
        cc=['nhannn@softech.vn'],
      # bcc=['bcc@example.com'],
        reply_to=['ecshopvietnamese@gmail.com'],
    )
    #mặc định body là text/plain
    #Nếu muốn gửi html thì thêm dòng sau
    email.content_subtype = "html"  # Main content is now text/html
    #Đính kèm file
    #email.attach_file("/images/weather_map.png")
    result = email.send() # 1 success, 0 fail
    print('Status Send', result)
    return HttpResponse("Send mail Example.")