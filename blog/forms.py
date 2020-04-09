from django import forms
from .models import Project_gate_1



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

STAKE_CHOICES = [('Network maintenance','Network maintenance (traffic, incidents, roadworks, maintenance management)'),
('Network enhancement (Network capacity and access)','Network enhancement (Network capacity and access)'),
('Social and environment (Network safety, environment)','Social and environment (Network safety, environment)'),
('Supplier payment and compensation','Supplier payment and compensation'),
('Supplier contracts and commercial (tendering and negotiations)','Supplier contracts and commercial (tendering and negotiations)'),
('Supplier engagement & relations (governance, collaboration and communication)','Supplier engagement & relations (governance, collaboration and communication)'),
('Supplier operations (staff safety and wellbeing, project management, tech and systems)','Supplier operations (staff safety and wellbeing, project management, tech and systems)'),
('Employee mental enablement (Authority & empowerment, Work structure & process, Collaboration)','Employee mental enablement (Authority & empowerment, Work structure & process, Collaboration)'),
('Employee physical enablement (training, resources, performance management)','Employee physical enablement (training, resources, performance management)'),
('Employee rewards (pay, benefits, respect and recognition, development opportunities)','Employee rewards (pay, benefits, respect and recognition, development opportunities)')]

DIRECTORATE_CHOICES = [('Data Science Team','Data Science Team'),
('Data Architecture Team','Data Architecture Team'),
('Data Governance Team','Data Governance Team'),
('Information Rights and Security Team','Information Rights and Security Team'),
('Major Projects & Capital Portfolio Management','Major Projects & Capital Portfolio Management'),('Operations','Operations'),
('Strategy and Planning','Strategy and Planning'),
('CFO','CFO'),
('Safety, Engineering and Standards','Safety, Engineering and Standards'),
('Commercial & Procurement','Commercial and Procurement'),
('HR & Organisational Development','HR & Organisational Development'),
('Corporate Affairs and Communications','Corporate Affairs and Communications'),
('ICT','ICT'),
('General Counsel','General Counsel')]

USE_CHOICES = [('Productivity increase','Productivity increase'),
('Cost reduction','Cost reduction'),
('Safety and wellbeing increase','Safety and wellbeing increase'),
('Decision making improvement','Decision making improvement'),
('Customer service improvement','Customer service improvement'),
('Resilience increase','Resilience increase'),
('Risk reduction','Risk reduction'),
('Efficiency increase','Efficiency increase'),
('Meeting a legal/regulatory requirement','Meeting a legal/regulatory requirement')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Project_gate_1
        fields = ('use_case_name','identifier','description','owner','sponsor','directorate','timeline','cost','use_case_benefits','stake_benefits','strat_customer','strat_safety','strat_deliver')
    
    identifier = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'style':'width:30ch'}))
    use_case_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'style':'width:30ch'}))
    description = forms.TextInput()
    owner = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'style':'width:30ch'}),label="Use case owner")
    sponsor = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'style':'width:30ch'}),label="Use case sponsor")
    directorate = forms.ChoiceField(choices=DIRECTORATE_CHOICES,widget=forms.Select,label="Please select the directorate or part of the business this use case originates from. (If the use case originates from the CDO Office, please select the relevant team)")
    timeline = forms.ChoiceField(choices=TIMELINE_CHOICES,widget=forms.Select,label='Please provide an estimate of the total time required to deliver the use case')
    cost = forms.ChoiceField(choices=COST_CHOICES,widget=forms.Select,label="Please give an estimate of the cost of completing the use case. Please be conservative with your estimates. For example, if the use case is likely to cost £100,000, please indicate £100,000 - £500,000")
    use_case_benefits = forms.MultipleChoiceField(choices=USE_CHOICES,widget=forms.CheckboxSelectMultiple,label='How does the new use case create value for Highways England?')
    stake_benefits = forms.MultipleChoiceField(choices=STAKE_CHOICES,widget=forms.CheckboxSelectMultiple,label='Please identify which stakeholder benefits are enabled by the use case.')
    strat_customer = forms.CharField(max_length = 250,label="Describe how the use case aligns to Highways England's strategic customer imperative:",widget=forms.TextInput(attrs={'style':'height:10ch'}))
    strat_safety = forms.CharField(max_length=250,label="Describe how the use case aligns to Highways England's strategic safety imperative:",widget=forms.TextInput(attrs={"style":"height:10ch"}))
    strat_deliver = forms.CharField(max_length=250,label="Describe how the use case aligns to Highways England's strategic delivery imperative:",widget=forms.TextInput(attrs={"style":"height:10ch"}))
