from django.conf import settings
from campagne.models import MeldRQRedirect
from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import time
from ua_parser import user_agent_parser


IOS = "iOS"
ANDROID = "Android"


class HttpResponseNoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def add_qr_event(data):
    MeldRQRedirect.objects.create(**{
        "data": data,
    })


def check_user_agent(request):
    result_dict = user_agent_parser.Parse(request.META.get('HTTP_USER_AGENT'))
    return result_dict.get("os", {}).get("family", "not-found")


def ip_source_throttle(request):
    now = time.time()
    interval = settings.COOLDOWN_INTERVAL
    source = request.GET.get(settings.QRCODE_SOURCE_PARAM)

    if not source:
        return

    origin = request.META.get("HTTP_ORIGIN", "no-origin")

    ip = get_client_ip(request)
    last_run = cache.get(ip, 0)
    if now - last_run < interval:
        print("wait")
    else:
        add_qr_event({
            "ip-address": ip,
            "source": source,
            "origin": origin,
        })
        cache.set(ip, now)
