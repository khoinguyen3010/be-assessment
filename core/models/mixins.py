from django.db.models import SET_NULL, DateTimeField, ForeignKey, Model

from authentication.models.user import User

class TimeUserStampedMixin(Model):
    """
    Mixin to add time and user stamping to data
    """
    created_at = DateTimeField(auto_now_add=True, db_index=True)
    updated_at = DateTimeField(auto_now=True, db_index=True)
    # Do not allow related_names since this would break a load of stuff
    created_by = ForeignKey(User, null=True, blank=True, related_name='+', on_delete=SET_NULL)
    updated_by = ForeignKey(User, null=True, blank=True, related_name='+', on_delete=SET_NULL)

    class Meta:
        """Metaclass"""
        abstract = True
