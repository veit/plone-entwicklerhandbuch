=========
Debugging
=========

Um die Rollen eines Nutzers in einem bestimmten Kontext angezeigt zu bekommen, erstellen wir folgenden View.

Zunächst wird der View konfiguriert in ``browser/configure.zcml``::

 <browser:page
   name="debug-user"
   for="*"
   permission="zope2.View"
   class=".debug.DebugUser"
   />

Anschließend erstellen wir noch das Python-Skript ``browser/debug.py``::

 from Products.Five.browser import BrowserView
 from AccessControl import getSecurityManager

 class DebugUser(BrowserView):
     """ Current user debugging """

     def __call__(self):

         result = list()
         user = getSecurityManager().getUser()
         result.append('User: %s' % user.getUserName())
         result.append('Roles: %s' % user.getRoles())
         result.append('Roles in context: %s' % user.getRolesInContext(self.context))
         result.append('')
         result.append(self.request.text())
         return '\n'.join(result)

Nach einem Neustart der Instanz können Sie nun in jedem Kontext den View im Browser aufrufen mit ``@@debug-user`` und erhält neben der ID des Nutzers auch dessen globale und kontextabhängigen Rollen. Darüberhinaus erhalten Sie auch Informationen zur Session etc.
