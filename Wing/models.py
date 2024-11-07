from django.db import models
from django.contrib.auth.models import User

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
    ('Environment, Climate Change (CC) and Water Resources (WR)',
     'Environment, Climate Change (CC) and Water Resources (WR)'),
    ('Housing and Community Amenities', 'Housing and Community Amenities'),
    ('Health', 'Health'),
    ('Recreation, Culture and Religion', 'Recreation, Culture and Religion'),
    ('Education', 'Education'),
    ('Science and IT', 'Science and IT'),
    ('Social Protection', 'Social Protection'),
)

DEV_PARTNER = (
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

PROPABILITY = (
    ('Highly Probable', 'Highly Probable'),
    ('Probable', 'Probable'),
    ('Signed', 'Signed'),
)


class CO_FINANCER(models.Model):
    name = models.CharField(max_length=100, choices=DEV_PARTNER)

    def __str__(self):
        return self.name


class Wing(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    name = models.CharField(max_length=3000, null=True)

    def __str__(self):
        return self.name


class Wing_One(models.Model):
    wing = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # author                           = models.ForeignKey(Wing, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=3000, null=True)
    currency = models.CharField(max_length=100, choices=CURRENCY, default='USD')
    amount_as_per_agreement_currency = models.FloatField()
    amount_in_equivalent_million_us = models.FloatField()
    date_of_signature = models.DateTimeField()
    development_partner = models.CharField(max_length=100, choices=DEV_PARTNER)
    co_financer = models.ManyToManyField(CO_FINANCER)
    loan_or_grant = models.CharField(max_length=200, choices=LOAN_GRANT, default='Loan')
    # loan_amount                      = models.FloatField(null=True, blank=True)
    # grant_amount                     = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=PROPABILITY)
    sector = models.CharField(max_length=500, choices=SECTOR, default='General Public Services')
    if_loan_conditionally = models.TextField(null=True, blank=True)
    current_status = models.TextField(null=True, blank=True)
    previous_month_status = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    LOAN = 'Loan'
    GRANT = 'Grant'
    LOAN_AND_GRANT = 'LoanAndGrant'
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    LOAN_OR_GRANT_CHOICES = [
        (LOAN, 'Loan'),
        (GRANT, 'Grant'),
        (LOAN_AND_GRANT, 'Loan and Grant'),
    ]

    # Project Details
    name = models.CharField(max_length=255)
    project_support = models.BooleanField(default=False)
    budget_support = models.BooleanField(default=False)
    loan_or_grant = models.CharField(
        max_length=20,
        choices=LOAN_OR_GRANT_CHOICES,
        default=LOAN_OR_GRANT_CHOICES[0][0],  # Default to 'Loan'
    )
    amount_as_per_agreement_currency = models.DecimalField(max_digits=10, decimal_places=2)

    # Loan Specific Fields
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    loan_duration = models.PositiveIntegerField(null=True, blank=True)
    loan_terms = models.TextField(null=True, blank=True)

    # Grant Specific Fields
    grant_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    grant_terms = models.TextField(null=True, blank=True)

    # Status of the project
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Ongoing',
    )

    def __str__(self):
        return self.name