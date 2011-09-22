from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class leadthewayPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import leadtheway.policy
        xmlconfig.file('configure.zcml', leadtheway.policy, context=configurationContext)
        
        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.PythonField')
        z2.installProduct(app, 'Products.TALESField')
        z2.installProduct(app, 'Products.TemplateFields')
        z2.installProduct(app, 'Products.PloneFormGen')
    
    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        z2.uninstallProduct(app, 'Products.TemplateFields')
        z2.uninstallProduct(app, 'Products.TALESField')
        z2.uninstallProduct(app, 'Products.PythonField')
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'leadtheway.policy:default')

LEADTHEWAY_POLICY_FIXTURE = leadthewayPolicy()
LEADTHEWAY_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(LEADTHEWAY_POLICY_FIXTURE,), name="leadtheway:Integration")
