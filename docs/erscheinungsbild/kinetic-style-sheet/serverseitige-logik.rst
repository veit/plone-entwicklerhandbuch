===================
Serverseitige Logik
===================

In ``src/vs.registration/vs/registration/browser/registration.kss`` wird die Serveraktion referenziert mit::

 action-server:confirmRegistrant;
 confirm-registrant: kssAttr('confirm');

Beim Aufruf der Aktion wird ``confirmRegistran`` im aktuellen Kontext mit den entsprechenden Parametern aufgerufen. So wird z.B. eine HTTP POST-Anfrage zu der URL ``http://localhost:8080/mysite/registration/confirmRegistrant`` mit dem Parameter ``confirm`` gesendet.

Die serverseitige Aktion wird meist als *View* implementiert. Entsprechend geben wir in ``browser/configure.zcml`` folgendes an::

 <browser:page
     for="vs.registration.interfaces.IRegistration"
     name="confirmRegistrant"
     class=".confirmations.confirmedRegistrants"
     attribute="confirm_registrant"
     permission="zope2.RequestReview"
     />

Und die ``confirmedRegistrants``-Klasse in ``browser/confirmations`` sieht dann so aus::

 from zope.interface import alsoProvides
 from kss.core import kssaction
 from plone.app.kss.plonekssview import PloneKSSView
 from plone.app.layout.globals.interfaces import IViewView
 from Akquisition import aq_inner
 from Products.Five.browser import BrowserView
 from vs.Registration.interfaces import IConfirmations

 class confirmedRegistrants
     @kssaction
     def confirm_registrant
         confirm = confirm.lower()
         if confirm not in ("confirm", "reject"):
             return
