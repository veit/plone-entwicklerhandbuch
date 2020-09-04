=======================================
DocTest Unit Tests in separaten Dateien
=======================================

Falls Ihnen die Tests zu umfangreich erscheinen oder Sie sie gern in einer separaten Datei hätten, können Dummy-Methoden in einem normalen Unit Test erstellt werden, die docstrings mit DocTests enthalten. Diese DocTests sollten beschreibenden Text **und** die entsprechenden Testmethoden enthalten.

Das folgende Beispiel ist aus der i18n-Architektur von Plone 3 entnommen: `test_countries.py`_. Es bezieht sich stark auf die Zope 3-Komponentenarchitektur, lädt ZCML-Dateien und bezieht das Test-Setup von ``zope.component.testing``::

    import unittest

    [...]

    from zope.component.testing import setUp, tearDown
    from zope.configuration.xmlconfig import XMLConfig
    from zope.testing import doctest
    from zope.testing.doctestunit import DocTestSuite

    def configurationSetUp(self):
        setUp()
        XMLConfig('meta.zcml', zope.component)()
        XMLConfig('meta.zcml', zope.app.publisher.browser)()
        XMLConfig('configure.zcml', plone.i18n.locales)()

    def testAvailableCountries():
        """
          >>> util = queryUtility(ICountryAvailability)
          >>> util
          <plone.i18n.locales.countries.CountryAvailability object at ...>

          >>> countrycodes = util.getAvailableCountries()
          >>> len(countrycodes)
          243

          >>> 'de' in countrycodes
          True

          >>> countries = util.getCountries()
          >>> len(countries)
          243

          >>> de = countries['de']
          >>> de['name']
          'Germany'

          >>> de['flag']
          '/@@/country-flags/de.gif'
        """

    def test_suite():
        return unittest.TestSuite((
            DocTestSuite('plone.i18n.locales.countries'),
            DocTestSuite(setUp=configurationSetUp,
                         tearDown=tearDown,
                         optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
            ))

    if __name__ == '__main__':
        unittest.main(defaultTest="test_suite")

.. _`test_countries.py`: http://dev.plone.org/plone/browser/plone.i18n/trunk/plone/i18n/locales/tests/test_countries.py
