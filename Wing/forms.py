from django import forms
from .models import Wing_One

LOAN_GRANT = (
    ('Loan', 'Loan'),
    ('Grant', 'Grant'),
)

CURRENCY = (
    ('USD', 'USD'),
    ('JPY', 'JPY'),
    ('A $', 'A $'),
    ('AS', 'AS'),
    ('BF', 'BF'),
    ('BSTC', 'BSTC'),
    ('C $', 'C $'),
    ('DFL', 'DFL'),
    ('Dirham', 'Dirham'),
    ('DKR', 'DKR'),
    ('DM', 'DM'),
    ('Euro', 'Euro'),
    ('FF', 'FF'),
    ('FM', 'FM'),
    ('ID', 'ID'),
    ('IDR', 'IDR'),
    ('IRS', 'IRS'),
    ('KD', 'KD'),
    ('Lira', 'Lira'),
    ('NKR', 'NKR'),
    ('NZD', 'NZD'),
    ('Rbl', 'Rbl'),
    ('SDR', 'SDR'),
    ('CHF/SF', 'CHF/SF'),
    ('SKR', 'SKR'),
    ('SR', 'SR'),
    ('STG/GBP', 'STG/GBP'),
    ('Taka', 'Taka'),
    ('Yen', 'Yen'),
    ('Yuan', 'Yuan'),
    ('Won', 'Won'),
)

SECTOR = (
    ('General Public Services', 'General Public Services'),
    ('Defence', 'Defence'),
    ('Public Order and Safety', 'Public Order and Safety'),
    ('Industrial and Economic Services', 'Industrial and Economic Services'),
    ('Agriculture', 'Agriculture'),
    ('Power and Energy', 'Power and Energy'),
    ('Transport and Communications', 'Transport and Communications'),
    ('Local Government and Rural Development', 'Local Government and Rural Development'),
    ('Environment, Climate Change (CC) and Water Resources (WR)', 'Environment, Climate Change (CC) and Water Resources (WR)'),
    ('Housing and Community Amenities', 'Housing and Community Amenities'),
    ('Health', 'Health'),
    ('Recreation, Culture and Religion', 'Recreation, Culture and Religion'),
    ('Education', 'Education'),
    ('Science and IT', 'Science and IT'),
    ('Social Protection', 'Social Protection'),
)

PROPABILITY = (
    ('Highly Probable', 'Highly Probable'),
    ('Probable', 'Probable'),
    ('Signed', 'Signed'),
)


DEV_PARTNER = (
    ('Select', 'Select'),
    ('ADB', 'ADB'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('AIIB', 'AIIB'),
    ('Belgium', 'Belgium'),
    ('Bulgaria', 'Bulgaria'),
    ('Belarus', 'Belarus'),
    ('Canada/CIDA', 'Canada/CIDA'),
    ('Canada/CIDA', 'Canada/CIDA'),
    ('China', 'China'),
    ('Czechoslovakia', 'Czechoslovakia'),
    ('Denmark', 'Denmark'),
    ('EU/EEC', 'EU/EEC'),
    ('EIB', 'EIB'),
    ('FAO', 'FAO'),
    ('French/AFD', 'French/AFD'),
    ('GAVI', 'GAVI'),
    ('GAIN', 'GAIN'),
    ('GEF', 'GEF'),
    ('Germany/(GIZ/KFW)', 'Germany/(GIZ/KFW)'),
    ('GFATM', 'GFATM'),
    ('Hungary', 'Hungary'),
    ('IBRD', 'IBRD'),
    ('IDA', 'IDA'),
    ('IFAD', 'IFAD'),
    ('IMO', 'IMO'),
    ('ILO', 'ILO'),
    ('India', 'India'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('IDB', 'IDB'),
    ('Italy', 'Italy'),
    ('Japan/JICA', 'Japan/JICA'),
    ('Kuwait', 'Kuwait'),
    ('NDF', 'NDF'),
    ('Netherland', 'Netherland'),
    ('Norway', 'Norway'),
    ('North Korea', 'North Korea'),
    ('OPEC', 'OPEC'),
    ('Pakistan', 'Pakistan'),
    ('Poland', 'Poland'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Rockefeller', 'Rockefeller'),
    ('Saudi Arabia/SFD', 'Saudi Arabia/SFD'),
    ('South Korea/KOICA', 'South Korea/KOICA'),
    ('Spain', 'Spain'),
    ('Sweden', 'Sweden'),
    ('Switzerland/SDC/SIDA', 'Switzerland/SDC/SIDA'),
    ('Singapore', 'Singapore'),
    ('SAARC Dev. Fund (SDF)', 'SAARC Dev. Fund (SDF)'),
    ('UNOPS', 'UNOPS'),
    ('UNEF', 'UNEF'),
    ('The Union ', 'The Union '),
    ('UAE', 'UAE'),
    ('UNDP', 'UNDP'),
    ('UNIDO', 'UNIDO'),
    ('UNFPA', 'UNFPA'),
    ('UNICEF', 'UNICEF'),
    ('UNESCO', 'UNESCO'),
    ('UK/DFID', 'UK/DFID'),
    ('USA/USAID', 'USA/USAID'),
    ('UNEP', 'UNEP'),
    ('WFP', 'WFP'),
    ('WHO', 'WHO'),
    ('UN Woman', 'UN Woman'),
    ('Yugoslavia', 'Yugoslavia'),
    ('UNCDF', 'UNCDF')
)

class Wing_One_Form(forms.ModelForm):
    name                             = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Name of project'}))
    amount_as_per_agreement_currency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'amount as per agreement urrency'}))
    amount_in_equivalent_million_us  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Amount in million'}))
    date_of_signature                = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    comments                         = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Comments','cols':'20', 'rows':'5'}))
    development_partner              = forms.ChoiceField(choices=DEV_PARTNER,widget=forms.Select(attrs={'class': 'form-control'}))
    date_of_signature                = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    sector                           = forms.ChoiceField(choices=SECTOR,widget=forms.Select(attrs={'class': 'form-control'}))
    loan_or_grant                    = forms.ChoiceField(choices=LOAN_GRANT,widget=forms.Select(attrs={'class': 'form-control'}))
    loan_amount                      = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'style':'display:none;', 'placeholder':'Enter loan amount'}))
    grant_amount                     = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'style':'display:none;', 'placeholder':'Enter grant amount'}))
    currency                         = forms.ChoiceField(choices=CURRENCY,widget=forms.Select(attrs={'class': 'form-control'}))
    status                           = forms.ChoiceField(choices=PROPABILITY,widget=forms.Select(attrs={'class': 'form-control'}))
    if_loan_conditionally            = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'If Loan Conditionally', 'cols':'20', 'rows':'5'}))
    current_status                   = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Current Status', 'cols':'20', 'rows':'5'}))
    previous_month_status            = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Previous Month Status', 'cols':'20', 'rows':'5'}))

    class Meta:
        model = Wing_One
        fields = '__all__'
        exclude = ['wing']