========
Matchers
========

Matchers implementieren einen boolschen Vergleich zwischen aktuellen und erwarteten Werten und teilen anschließend Jasmine mit, ob die Erwartungen erfüllt wurden oder nicht.

``toBe``
 entspricht ``===``
``toEqual``
 für einfache Literale, Variablen und Objekte
``toMatch``
 für reguläre Ausrücke
``toBeDefined``
 vergleicht mit ``undefined``
``toBeUndefined``
 vergleicht mit ``undefined``
``toBeNull``
 vergleicht mit Null
``toBeTruthy``
 vergleicht mit boolscher Wahrscheinlichkeit
``toBeFalsy``
 vergleicht mit boolscher Wahrscheinlichkeit
``toContain``
 vergleicht, ob ein Item in einem Array enthalten ist
``toBeLessThan```
 mathematischer Vergleich
``toBeGreaterThan``
 mathematischer Vergleich
``toBeCloseTo``
 Präzision des mathematischen Vergleichs
``toThrow``
 überprüft, ob eine Funktion eine Fehlermeldung
 ausgibt.

Jeder *Matcher* kann auch eine negative Annahme
überprüfen indem bei ``èxpect`` ein ``not`` dem
*matcher* vorangestellt wird.

Zwar bringt Jasmine bereits eine ganze Reihe von
*Matchers* mit, es gibt jedoch auch die Möglichkeit,
eigene *Matchers* für spezifische Annahmen zu
schreiben.
