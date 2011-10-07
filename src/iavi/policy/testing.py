from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class IaviPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import iavi.policy as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

    def tearDownZope(self, app):
        pass

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'iavi.policy:default')


IAVI_POLICY_FIXTURE = IaviPolicy()

IAVI_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IAVI_POLICY_FIXTURE,),
    name='Iavi:Integration'
    )
