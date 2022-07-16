# bruggelrausschmeisser


### bot startn

0. key von @botfather (telegram) ist in .env enthalten.
1. bot starten:

   ```docker-compose up```

nach änderungen am code:

   ```docker-compose build && docker-compose up```

### todo 
- [ ] telegram-python verstehen
- [X] is_mod-funktion
- [ ] del - kommando inkl. begründung (optional)
- [ ] mute - kommando inkl. begründung (optional)
- [ ] unmute - kommando inkl. begründung (optional)
- [ ] ban - kommando inkl. begründung (optional)
- [ ] unban - kommando inkl. begründung (optional)
- [ ] bot soll nicht auf kommandos antworten
- [ ] ausgeführte befehle inkl. nachricht in mod_log chat umleiten
- [ ] bot soll auf @admin hören und falls die nachricht in den Mods 2.0-chat weiterleiten

- [ ] todo-liste fortsetzen

- [ ] "/faq"-Funktion: Der Bot antwortet dem Benutzer, auf den dieser Befehl angewandt wurde, mit einem Text, in welchem der Link zur FAQ etc. enthalten ist. Der Benutzer wird automatisch für 24 Stunden gemuted.
- [ ] "/such"-Funktion: Der Bot antwortet dem Benutzer, auf den dieser Befehl angewandt wurde, mit einem Text, in welchem die Beschreibung Suche enthalten ist. Der Benutzer wird automatisch für eine (1) Stunde gemuted.

- [ ] "/complain"-Funktion: Der Bot antwortet dem Benutzer, auf den dieser Befehl angewandt wurde, mit einem Text, in welchem der Link zur Beschwerdedestelle enthalten ist.

- [ ] "Captcha"-Funktion: Tritt ein Benutzer der Gruppe bei muss er innerhalb eines vor zu definierenden Zeitraums eine Schaltfläche betätigen. Es sind zwei Schaltflächen zu implementieren. Nur bei korrekter Auswahl wird der Benutzer für die Gruppe zugelassen. Bspw. "Ich bin d!" (Richtige Antwort), "Ich bin nicht d!" (Falsche Antwort)
- [ ] "Cleanup"-Funktion: Wird ein Konto gelöscht wird der Benutzer nicht automatisch aus dem Gruppenchat entfernt. Diese Funktion wird X mal in Zeitraum Y ausgeführt und bereinigt die Gruppe von gelöschten Nutzerkonten.
- [ ] "Killing Floor"-Automute: Wird der betreffende Satz (gerne auch mit ähnlichen Strings) X mal in Zeitraum Y gedroppt erfolgt ein automatischer Mute.
- [ ] "Wrote as channel"-Schutz: Schreibt ein Nutzer als Kanal wird die Nachricht sofort gelöscht. Ausnahmen können hinzugefügt oder entfernt werden. (Aktuelle Ausnahmen wären SB & OB)
´´´Command: "/funktion"
Victim: Username des Betroffenen (Telegram-ID des betroffenen Users)
Admin: Username des Admin (Telegram-ID des Admins)
Reason: "Begründungstext"
Duration:  Zeitraum (Bis Zeitraum Ende, Datum + Uhrzeit) -> Diese Zeile wird nur beigefügt, wenn das "/mute"-Kommando genutzt wurde.´´´