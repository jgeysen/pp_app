from django.db import models
from django.utils import timezone

# Create your models here.



TIMELINE_CHOICES = [ ('< 1','Less than one month'),
		('1 - 6','1 to 6 months'),
		('6 - 12','6 months to 1 year'),
		('12 - 24','1 to 2 years'),
		('24 - 60','1 to 5 years'),
		('> 60','More than 5 years')]

COST_CHOICES = [('0 - 50,000','£0 - £50,000'),
		('50,000 - 100,000','£50,000 - £100,000'),
		('100,000 - 500,000','£100,000 - £500,000'),
		('500,000 - 1000,000','£500,000 - £1000,000'),
		('1000,000 - 2000,000','£1000,000 - £2000,000'),
		('2000,000 - 5000,000','£2000,000 - £5000,000'),
		('5000,000 - 10,000,000','£5000,0000 - £10,000,000'),
		('10,000,000 - 20,000,000','£10,000,000 - £20,000,000'),
		('> 20,0000,000','More than £20,000,000')]

#STAKE_CHOICES = 


class Project_gate_1(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    identifier = models.CharField(max_length=8)
    use_case_name = models.CharField(max_length = 50)
    description = models.TextField()
    owner = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=50)
    directorate = models.CharField(max_length=1500)
    timeline = models.CharField(max_length=10,choices=TIMELINE_CHOICES)
    cost = models.CharField(max_length=25,choices=COST_CHOICES)
    use_case_benefits = models.TextField()
    stake_benefits = models.TextField()
    strat_customer = models.TextField()
    strat_safety = models.TextField()
    strat_deliver = models.TextField()
    comments = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __st__(self):
        return self.title
