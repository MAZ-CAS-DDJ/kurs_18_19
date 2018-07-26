# Zusatzpackages Wget und CSVkit

Es gibt sehr viele Zusatprogramme für das Terminal, alle mit sehr unterschiedlichen Funktionialtäten. Es lohnt sich in den Dokumentationen herumzustöbern, um die unterschiedlichen Programme kennenzulernen.

Wir wollen hier zwei kennenlernen: ```wget``` und ```csvkit```und am Ende wollen wir alle Befehle mit einem Crontab kombinieren, um Files dann automatisch abzuspeichern.

## wget

Was ist wget? Um die Funktionen kennenzulernen googelt ihr am besten immer nach "wget documentation". Ihr stösst dann [zum Beispiel auf darauf](https://www.gnu.org/software/wget/manual/wget.html#Overview). Die kurze Definition von Wget ist "GNU Wget is a free utility for non-interactive download of files from the Web".

- Zuerst müsst ihr es installieren. Das geschieht mit ```pip install wget```.
- Mit ```wget --version```erfährt ihr, welche Version ihr nun installiert habt, und, wer eigentlich hinter Wget steckt.
- Mit ```wget --help```könnte ihr alle Funktionen aufrufen. Das wird euch zunächst nicht viel sagen. Aber lasst euch nicht abschrecken. Ihr müsst nicht alles auf einmal wissen. Und vieles braucht ihr gar nicht zu wissen. Wenn ihr euch entschliesst, dass Wget für euch nichts taugt, müsst ihr euch gar nie damit befassen.
- Ich verwende wget beispielsweise, um regelmässig Snapshots von Websites oder von Facebook-Gruppen zu nehmen. z.B. ```wget https://www.balthasar-glaettli.ch/```
- Viele Dienste erkennen Wget als Roboter, deshalb muss man manchmal mitgeben, dass es sich hier um einen Browser handelt, z.B.: ```wget --user-agent=Firefox https://www.facebook.com/glaettli.ch```
- 
