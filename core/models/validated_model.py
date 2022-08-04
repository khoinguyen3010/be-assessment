from django.db.models import Model

class ValidatedModel(Model):
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save()
