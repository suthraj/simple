##### .../myapp/forms.py #####

from django import forms
from myapp.models import Shirt


"""
    Simple 'Name' form.
    NOTE:
    - required: By default, each Field class assumes the value is required, so to make it not required you need to set 'required=False'.
    - label: The 'label' argument lets you specify the “human-friendly” label for this field.
        - This is used when the Field is displayed in a Form.
    - label_suffix: The 'label_suffix' argument lets you override the form’s 'label_suffix' on a per-field basis.
    - validators: The 'validators' argument lets you provide a list of validation functions for this field.
    - disabled: The 'disabled' boolean argument, when set to True, disables a form field using the disabled HTML attribute so that it won’t be editable by users.
    - localize: The 'localize' argument enables the localization of form data input, as well as the rendered output.
    - error_messages: The 'error_messages' argument lets you override the default messages that the field will raise.
        - Pass in a dictionary with keys matching the error messages you want to override.
    - help_text: The 'help_text' argument lets you specify descriptive text for this Field.
        - If you provide 'help_text', it will be displayed next to the Field when the Field is rendered by one of the convenience Form methods.
"""
class NameForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)


"""
    The Django forms API have two field types to work with multiple options: 'ChoiceField' and 'ModelChoiceField'.
    - Following is a basic implementation using a 'ChoiceField'.
"""
class ShirtForm(forms.Form):
    CHOICES = Shirt.SHIRT_SIZES
    name = forms.CharField(max_length=60)
    shirt_size = forms.ChoiceField(choices=CHOICES)


"""
    Expense Form (without groups).
"""
class ExpenseFormSimple(forms.Form):
    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )
    amount = forms.DecimalField()
    date = forms.DateField()
    category = forms.ChoiceField(choices=CHOICES)


"""
    Expense Form (with groups).
    - Organize the choices in groups to generate the <optgroup> tags.
"""
class ExpenseFormFancy(forms.Form):
    CHOICES = (
        ('Debt', (
            (11, 'Credit Card'),
            (12, 'Student Loans'),
            (13, 'Taxes'),
        )),
        ('Entertainment', (
            (21, 'Books'),
            (22, 'Games'),
        )),
        ('Everyday', (
            (31, 'Groceries'),
            (32, 'Restaurants'),
        )),
    )
    amount = forms.DecimalField()
    date = forms.DateField()
    category = forms.ChoiceField(choices=CHOICES)
