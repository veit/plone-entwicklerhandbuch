=====
Views
=====

Folgende Änderungen können nun in ``browser/registrant.py`` hinzugefügt werden::

 from zope.component import getUtility
 ...
 @memoize
 def registrations(self):
     context = aq_inner(self.context)
     registrations = getUtility(IRegistrations)
     return registrations.registrations_for_registrant(context)

und in ``browser/registrant.pt``::

 <h2 i18n:translate="title_registrated_at">Registrated at</h2>
 <ul>
     <tal:block repeat="registration view/registrations">
         <li>
             <a tal:attributes="href registration/url"
                tal:content="registration/title" />
         </li>
     </tal:block>
 </ul>
