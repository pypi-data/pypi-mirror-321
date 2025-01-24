from django.core.signals import setting_changed
from saas_base.settings import Settings

DEFAULTS = {'PROVIDERS': {}}


class DomainSettings(Settings):
    IMPORT_PROVIDERS = [
        'PROVIDERS',
    ]

domain_settings = DomainSettings('SAAS_DOMAIN', defaults=DEFAULTS)
setting_changed.connect(domain_settings.listen_setting_changed)
