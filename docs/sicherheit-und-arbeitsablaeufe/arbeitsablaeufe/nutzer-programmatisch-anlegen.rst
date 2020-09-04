=============================
Nutzer programmatisch anlegen
=============================

Hierzu wird in der Datei ``vs/policy/setuphandlers.py`` folgendes angegeben::

 def installUsers(site):

     site.portal_membership.addMember('me', 'secret', ['Member'], ())
     site.portal_membership.addMember('myself', 'secret', ['Editor', 'Member'], ())
     site.portal_membership.addMember('i', 'secret', ['Manager', 'Member'], ())

 def setupVarious(context):

     if context.readDataFile('vs.policy_various.txt') is None:
        return

     ...
     installUsers(site)

Für das Anlegen mehrerer Nutzer stehen zwei Erweiterungen zur Verfüugung:

- `atreal.usersinout <https://pypi.python.org/pypi/atreal.usersinout/>`_
- `collective.mass_subscriptions <https://pypi.python.org/pypi/collective.mass_subscriptions>`_
