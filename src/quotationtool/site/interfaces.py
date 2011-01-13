import zope.interface
import zope.component
from zope.location.interfaces import IPossibleSite
from zope.container.interfaces import IContainer
from zope.component.interfaces import IObjectEvent


class IQuotationtoolSite(IContainer, IPossibleSite):
    """Site containing the quotationtool application."""


class INewQuotationtoolSiteEvent(IObjectEvent):
    """Indictes that a new QuotationtoolSite has been created."""


