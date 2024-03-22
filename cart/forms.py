from django import forms


class CheckoutForm(forms.Form):
    customer_firstName = forms.CharField(
        label="First Name",
        min_length=4,
        max_length=100, 
        error_messages={
            "min_length": "Tối thiểu 4 kí tự",
            "required": 'Vui lòng điền First Name'
            }
    )
    customer_lastname = forms.CharField(
        label="Last Name", 
        max_length=100, 
        error_messages={"required": 'Vui lòng điền Last Name'}
    )
    customer_email = forms.EmailField(
        label="Email", 
        max_length=255, 
        error_messages={"required": 'Vui lòng điền Email'},
        help_text="Để nhận email xác nhận đơn hàng"
    )   
    customer_phone = forms.CharField(
        label="Phone",
        min_length=10,
        max_length=20, 
        error_messages={"required": 'Vui lòng điền Phone'}
    )
    customer_street = forms.CharField(
        label="Street", 
        max_length=255, 
        error_messages={"required": 'Vui lòng điền Street'}
    )
    customer_city = forms.CharField(
        label="City", 
        max_length=100, 
        error_messages={"required": 'Vui lòng điền City'}
    )
    customer_state = forms.CharField(
        label="State", 
        max_length=100, 
        error_messages={"required": 'Vui lòng điền State'}
    )
    customer_zipCode = forms.CharField(
        label="ZipCode", 
        max_length=10, 
        required=False
    )
    PAYMENT_CHOICES = [
        ('1', 'COD'),
        ('2', 'Credit'),
        ('3', 'Banking'),
        ('4', 'Cast')
        # Thêm các lựa chọn khác tại đây...
    ]
    payment_type = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect,
        error_messages={
            "required": 'Vui lòng chọn Phương thức thanh toán'
            }
    )
    

    
