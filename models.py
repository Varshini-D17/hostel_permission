from django.db import models
class permission(models.Model):
	ParentsApproval=models.CharField(max_length=50)
	ClasscoordinatorApproval=models.CharField(max_length=50)
	WardenApproval=models.CharField(max_length=40)
	HODApproval=models.CharField(max_length=40)
