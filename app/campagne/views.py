from django.conf import settings
from django.http import HttpResponseRedirect
from campagne.utils import HttpResponseNoContent, check_user_agent, ip_source_throttle, IOS, ANDROID


class AppStoreSchemaRedirect(HttpResponseRedirect):
    allowed_schemes = ["itms-apps"]


def meldr_qr_event(request):
    ip_source_throttle(request)
    return HttpResponseNoContent()


def meldr_redirect(request):

    ip_source_throttle(request)

    url = f"{settings.MELDR_URL}/{settings.MELDR_DOWNLOADS_PATH}"

    mobile_device_os = check_user_agent(request)
    if mobile_device_os == IOS:
        url = settings.MELDR_APPSTORE 
        return AppStoreSchemaRedirect(url)
    elif mobile_device_os == ANDROID:
        url = settings.MELDR_PLAYSTORE 

    return HttpResponseRedirect(url)