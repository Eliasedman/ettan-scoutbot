# Ettan Scoutbot

🎯 **Syftet**

Ettanklubbar saknar ofta resurser att göra omfattande datadriven scouting. Med den här boten kan man ranka alla spelare i serien utifrån hur väl de passar en specifik rollprofil – till exempel offensiv ytter, defensiv mittfältare eller bolltrygg mittback. Systemet ger varje spelare ett Fit Score mellan 0 och 100 som visar hur väl de matchar profilen.

## 🔍 Vad en rollprofil är

En rollprofil definierar vilken typ av egenskaper du letar efter på en viss position. För varje position (målvakt, mittback, ytterback, defensiv mittfältare, central mittfältare, offensiv mittfältare, winger, forward) kan klubben bestämma:

- Vilka statistikmått som är viktiga – t.ex. skott/90 minuter, nyckelpassningar/90, framåtpassningar/90, dueller vinst %, passningssäkerhet.
- Hur mycket varje mått ska väga – några mått kan vara viktigare än andra.
- Filter – som minsta antal minuter de senaste 12 månaderna och högsta tillåtna ålder. Det gör att du slipper spelare som spelat för lite eller är för gamla.

## 🧠 Hur Fit Score räknas ut

Efter att data har samlats in om spelare och matcher körs en scoring-engine som ger fyra delbetyg:

- **RollFit (0–100)** – jämför spelarnas statistik med andra på samma position och räknar procentiler. En spelare med hög percentil i ett viktigt mått får mycket poäng där.
- **AgePotential (0–100)** – unga spelare anses ha större utvecklingspotential. Poängen sjunker gradvis efter 26 års ålder.
- **Availability (0–100)** – baseras på hur många minuter spelaren spelat senaste året. En spelare som alltid är på plan får högre poäng.
- **GapScore (−0 till −20)** – straff för långa avbrott där spelaren inte ens var med i matchtruppen (mer än tre matcher i rad). Om spelaren bara satt på bänken räknas det inte som avbrott. Detta räknas bara för etablerade spelare som spelat minst fem av de senaste tio matcherna.

Dessa delbetyg kombineras till ett slutligt Fit Score med en viktning som går att justera (t.ex. 45 % RollFit, 25 % ålder, 20 % tillgänglighet, −10 % GapScore).

## 🖥️ Två huvudfunktioner i UI

- **Sök spelare + rollprofil** – du skriver in ett namn och väljer en rollprofil. Systemet visar spelarens Fit Score, hur delbetygen bidrar och vilka statistikmått som driver upp eller ner poängen.
- **Top 25 spelare** – du väljer en rollprofil och ser en lista med de 25 spelare som har högst Fit Score för den profilen. Tabellen visar namn, ålder, klubb, Fit Score, RollFit och GapScore för varje spelare.

## 🧱‍🚀 Tekniken bakom

- **Dataadapter:** en modul som kan hämta spelardata, säsongsstatistik och matchtrupper från olika källor (CSV, API).
- **Databas:** all data sparas i en SQLite-databas (kan bytas till Postgres senare).
- **Scoring engine:** ett Pythonpaket som kör beräkningarna ovan och sparar resultaten.
- **Streamlit‑UI:** ett enkelt webbgränssnitt där klubben kan skapa och välja rollprofiler, söka spelare och se topplistor.
