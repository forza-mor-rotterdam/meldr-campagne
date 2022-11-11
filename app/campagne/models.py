from django.db import models


class MeldRQRedirect(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    data = models.JSONField(null=True)

    class Meta:
        verbose_name = "MeldR Redirect"
        verbose_name_plural = "MeldR Redirects"
        ordering = ("created_at", )