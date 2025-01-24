import logging
from .base import BaseProvider
from ..models import Domain

logger = logging.getLogger(__name__)


class NullProvider(BaseProvider):
    def add_domain(self, domain: Domain) -> Domain:
        logger.info("Enable domain:", domain)
        domain.verified = True
        domain.ssl = self.options.get("ssl", False)
        domain.save()
        return domain

    def verify_domain(self, domain: Domain) -> Domain:
        logger.info("Verify domain:", domain)
        return domain

    def remove_domain(self, domain: Domain):
        logger.info("Remove domain:", domain)
