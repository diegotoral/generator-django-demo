import django.db.models

class Task(django.db.models.Model):

    def __unicode__(self):
        return 'Task'
