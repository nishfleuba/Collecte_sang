from django.contrib import admin
from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Donneur)
class DonneurAdmin(admin.ModelAdmin):
    list_display = "nom", "prenom", "date_naissance", "groupe_sanguin", "tel"
    

@admin.register(Stock_Sang)
class Stock_SangAdmin(admin.ModelAdmin):
    list_display = ("type_sang", "quantite", "date_reception", "date_expiration")

    def save_form(self, request, form, change):
        obj = form.save(commit=False)
        if change:
            messages.error(request, "Modification non autorisée.")
            return
        don = obj.don
        try:
            don.quantite += obj.quantite
        except Exception:
            don.quantite = obj.quantite
        don.save()
        obj.save()
        form.save_m2m()
        return obj

@admin.register(Centre_Collecte)
class Centre_CollecteAdmin(admin.ModelAdmin):
 list_display = "nom", "adresse","contact"

@admin.register( Personnel_Medical)
class  Personnel_MedicalAdmin(admin.ModelAdmin):
 list_display = "personnel", "specialite","collecte"

# @admin.register(Don)
# class  DonAdmin(admin.ModelAdmin):
#  list_display = "donneur","createde_by","collecte","date_don","quantite"
@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display ="donneur","created_by","collecte","date_don","quantite"

@admin.register(Receveur)
class  ReceveurAdmin(admin.ModelAdmin):
 list_display = "nom" ,"prenom","date_naissance","groupe_sanguin"

@admin.register(Transfusion)
class  TransfusionAdmin(admin.ModelAdmin):
 list_display = "receveur","date","quantite","stock" 
 

