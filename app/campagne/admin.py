from campagne.models import MeldRQRedirect
from django.contrib import admin
from django.http import JsonResponse


import csv
from django.http import HttpResponse
from django.template.defaultfilters import slugify

def export(qs, fields=None):
    model = qs.model
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={slugify(model.__name__)}.csv"},
    )
    writer = csv.writer(response)
    writer.writerow([
        "created_at",
        "source",
        "ip-address",
        "origin",
    ])
    for obj in qs:
        row = []
        row.append(getattr(obj, "created_at"))
        row.append(getattr(obj, "data").get("source"))
        row.append(getattr(obj, "data").get("ip-address"))
        row.append(getattr(obj, "data").get("origin"))
        writer.writerow(row)
    return response


class MeldRQRedirectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "data",
    )

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        return export(queryset)


admin.site.register(MeldRQRedirect, MeldRQRedirectAdmin)
