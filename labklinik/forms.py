from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_text', 'description', 'due_date', 'priority']
        widgets = {
            'task_text': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
        }
