# Rückblick Commandline

# Navigation

Wir haben die Commandline oder den Terminal bereits gestern kennengelernt. Damit installieren wir neue Programme, wir halten alten aktuell, und wir können damit unsere Eigen-Kreationen, unsere eigene Programme auslösen. Sehr oft, können wir auf das Terminal dazu nutzen, sehr komplexe Aufgaben zu lösen.

Deshalb wollen wir uns dieses Werkzeug näher anschauen, bevor wir uns in die Python-Pogrammiersprache stürzen.

Zuerst wollen wir damit üben:

- Übung 1

Aber die Commandline ist natürlich nicht nur dazu da, Dokumente herumzuschieben, oder neue zu erschaffen. Die Commanline kann viel mehr. Lassen wir den Computer damit reden.

- ```say hello```
- ```say hallo, ich bins```
- ```man say```damit rufen wir das ganze Manual auf. Schauen wir uns an, was wir alles damit machen könnne. Mit ```q```verlassen wir den Modus wieder.
- ```say -v ?```oder```say voice ?```damit können wir alle gespeicherte Sprachen abrufen.
- Mit dem Befehl ```say -f "namedesfiles"```können wir uns ganze Dokumente vorlesen lassen.

Wirkt der Computer nicht bereits endlich menschlicher, weil er sprechen kann? Aber natürlich spricht er nur dann, wenn wir es ihm sagen. Noch beeindruckender ist, wenn der Computer scheinbar unaufgefordert zu uns spricht.

Wir können den Computer sagen, dass er gewisse Tätigkeiten zu genau bestimmten Zeiten ausführt. Mit derselben Funktionialität funktionieren Dutzende Dienste, und Apps. E-Mail-Dienste zum Beispiele. Sie sind je nach Einstellung einfach alle 15 Minuten oder jede Minute so eingestel.

Damit wir dem Computer entsprechend einstellen können, müssen wir zuerst den entsprechenden Editor einstellen. Das ist das Eingabesystem für unser Gerät. Der gängiste Editor für Unix-Geräte (Apple und Linux) ist der VIM Editor. Dieser ist allerdings ziemlich kompliziert. Wir arbeiten mit dem Nano Editor.

- Dafür gebt ihr ein: ```export EDITOR=nano```
- Nun öffnen wir den Crontab: ``crontab -e```
- Und wir geben die fünf * Zeichen ein, und dann ```say "hello you"```
- Der Computer wird nun jede Minute "hello you" sagen.
- Das lässt sich natürlich verfeinern. Wie, erschliesst sich auf der Site [Crontab.guru](https://crontab.guru/).

Übung 2  



#talk, cron, grep, piping, wget, file abspeichern mit Datum
