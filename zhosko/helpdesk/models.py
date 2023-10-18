from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    assigned_user = models.ForeignKey(User, related_name='assigned_issues', on_delete=models.SET_NULL, null=True)
    resolved_user = models.ForeignKey(User, related_name='resolved_issues', on_delete=models.SET_NULL, null=True)

    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )
    
    NEW = "NEW"
    INPROGRESS = "IN PROGRESS"
    RESOLVED = "RESOLVED"
    CONFIRMED = "CONFIRMED"
    STATUS_CHOICES = [
        (NEW, 'new'),
        (INPROGRESS, 'in progress'),
        (RESOLVED, 'resolved'),
        (CONFIRMED, 'confirmed')
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=NEW
    )
    actions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.status}"
    

   