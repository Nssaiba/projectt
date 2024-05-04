from django.contrib import admin
from .models import Offre
from .models import Evenements
from .models import Client
from .models import Destination
from .models import Commentaire
from .models import Admins

# Register your models here.
admin.site.register(Offre)
admin.site.register(Evenements)
admin.site.register(Client)
admin.site.register(Destination)
admin.site.register(Commentaire)
admin.site.register(Admins)
