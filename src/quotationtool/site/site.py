import zope.interface
import zope.component
import zope.event
from zope.container.btree import BTreeContainer
from zope.site import SiteManagerContainer, LocalSiteManager
from zope.app.component.hooks import getSite, setSite
from zope.container.interfaces import IObjectAddedEvent

import interfaces


class NewQuotationtoolSiteEvent(object):
    """A new quotationtool site has been created."""

    zope.interface.implements(interfaces.INewQuotationtoolSiteEvent)

    def __init__(self, site):
        self.object = site


class QuotationtoolSite(SiteManagerContainer,
                        BTreeContainer):
    """Implementation of the container that holds the site for the
    quotationtool app."""

    zope.interface.implements(interfaces.IQuotationtoolSite)

    def setSiteManager(self, sm):
        super(QuotationtoolSite, self).setSiteManager(sm)

        # need to set the site since utilities might depend from
        # eachother
        old_site = getSite()
        setSite(self)
        
        # notify new site event
        zope.event.notify(NewQuotationtoolSiteEvent(self))
        
        setSite(old_site)


@zope.component.adapter(
    interfaces.IQuotationtoolSite, 
    IObjectAddedEvent)
def setSiteManagerWhenAdded(site, event):
    sm = LocalSiteManager(site)
    site.setSiteManager(sm)
