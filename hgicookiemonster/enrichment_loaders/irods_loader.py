from cookiemonster.common.models import Cookie
from cookiemonster.processor.models import EnrichmentLoader
from hgicommon.data_source import register

from hgicookiemonster.context import HgiContext
from hgicookiemonster.enrichment_loaders._irods import load_enrichment_from_irods, IRODS_ENRICHMENT


def _can_enrich(cookie: Cookie, context: HgiContext) -> bool:
    if cookie.enrichments[-1].source == IRODS_ENRICHMENT:
        return False
    return cookie.identifier.endswith(".bam") or cookie.identifier.endswith(".cram")


_enrichment_loader = EnrichmentLoader(_can_enrich, load_enrichment_from_irods, priority=0, name=IRODS_ENRICHMENT)
register(_enrichment_loader)