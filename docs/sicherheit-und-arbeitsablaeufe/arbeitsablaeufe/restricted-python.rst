=================
Restricted Python
=================

Zope erlaubt privilegierten Nutzern *Page Templates, DTML-Methoden und Python-Skripte *through-the-web* zu erstellen. *Restricted Python* gewährleistet nun, dass diese Nutzer nicht Skripte oder Templates erstellen können, die Zugang zu Ressourcen oder Methoden erlauben würden, die ihnen nicht zugestanden wurden. Die Berechtigungen werden automatisch überprüft und führen ggf. zu einer *Unauthorized*-Exception.

Es lassen sich sog. *Proxy Roles* für Templates oder Python-Skripte entweder im ZMI oder in einer ``*.metadata``-Datei angeben. So gibt es z.B. für das *Controller Python Script* ``send_feedback.cpy`` eine korrespondierende Datei ``send_feedback.cpy.metadata`` mit folgendem Inhalt::

 [default]
 proxy=Manager,Anonymous
 [security]
 View=0:Authenticated

Dies ist notwendig, da das Skript normalerweise von Nutzern aufgerufen wird, die nicht auf die E-Mail-Konfiguration der Site zugreifen dürften, das Skript jedoch bestimmte angaben aus dieser Konfiguration benötigt.

*Restricted Python* gewährleistet ebenfalls, dass *through-the-web* erstellte Skripte nicht auf das Dateisystem zugreifen oder unautorisierte Module importieren können, die die Sicherheit des Servers kompromittieren könnten. Lediglich die von``AccessControl`` in ``allow_module()`` und ``allow_class()`` angegebenen Module und Klassen können importiert werden. Zusätzlich werden alle Methoden und Variablen, deren Namen mit einem Unterstrich ``_`` beginnen, als *privat* betrachtet und können nicht aufgerufen werden.

Durch diese Sicherheitsmechanismen sollten Administratoren bei sachgemäßer Handhabung daran gehindert werden, versehentlich Sicherheitslücken in eine Anwendung zu reißen. Bei unsachgemäßer Handhabung kann jedoch weiterhin erheblicher Schaden angerichtet werden.
