#!/usr/bin/env python3
"""Build data/familie.json: every person and couple found so far, with sources.

Data comes from the research notes in onderzoek/ (FamilySearch records and Family Tree, MyHeritage).
Living people are not named: the daughter of András Kagol and Mária Fridlik is shown only as "dochter".
Run: python scripts/build_data.py
"""
import json
import os

FS_TREE = "https://www.familysearch.org/tree/person/details/"
FS_REC = "https://www.familysearch.org/ark:/61903/1:1:"

P = {}


def person(pid, name, sex, born=None, died=None, place=None, note="", fs=None, recs=(), line=""):
    P[pid] = {
        "id": pid, "name": name, "sex": sex, "born": born, "died": died, "place": place,
        "note": note, "line": line,
        "sources": ([{"label": "FamilySearch stamboom " + fs, "url": FS_TREE + fs}] if fs else [])
        + [{"label": lab, "url": rid if rid.startswith("http") else FS_REC + rid} for lab, rid in recs],
    }


# --- Kargol (Szczepanów, Galicië -> Boedapest) ---
L = "kargol"
# Poland: all in the parish of Szczepanów (Tarnów diocese); house no. 57 lies in the village of Wokowice.
person("casimir_kargol_sr", "Casimir Kargol", "m", "ca. 1751", "22-2-1815", "Wokowice", line=L,
       note="Oudste bekende Kargol van deze lijn. Woonde op huis nr. 57 in Wokowice en overleed daar in 1815, 64 jaar "
            "oud. Kinderen met Agnes Grochola: Josephus (gedoopt 19-3-1776), Simon (ca. 1777), Bartholomaeus "
            "(21-8-1787) en Marianna (2-7-1789). Zijn huwelijk (rond 1775) en zijn doop staan niet in de online index.",
       recs=[("Begrafenis 1815", "6V34-W5QS"), ("Genoemd bij begrafenis zoon Simon 1834", "6V34-8W94"),
             ("Doop zoon Josephus 1776", "6V39-9495")])
person("agnes_grochola", "Agnes Grochola", "f", None, None, "Wokowice", line=L)
person("simon_kargol", "Simon Kargol", "m", "ca. 1777", "9-10-1834", "Wokowice", fs="PZ9V-ZK5", line=L,
       note="Boer op huis nr. 57 in Wokowice. Trouwde op 16 februari 1806 in Szczepanów met Catharina Lis (18), "
            "dochter van Stanislaus Lis. Overleed op 57-jarige leeftijd.",
       recs=[("Huwelijk 1806", "6VSB-KR2T"), ("Begrafenis 1834", "6V34-8W94")])
person("catharina_lis", "Catharina Lis", "f", "ca. 1788", None, "Szczepanów", fs="PZ9V-CNY", line=L,
       note="Waarschijnlijk dezelfde als de Catharina die op 17 maart 1788 in Szczepanów werd gedoopt als dochter van "
            "Stanislaus Lis en Theresia.", recs=[("Doop 1788 (waarschijnlijk)", "6VS1-7NDS")])
person("stanislaus_lis", "Stanislaus Lis", "m", None, None, "Szczepanów", line=L)
person("theresia_lis", "Theresia", "f", None, None, "Szczepanów", line=L)
person("casimir_kargol", "Casimir Kargol", "m", None, None, "Wokowice", line=L,
       note="Vader van Salomea. Een andere Kargol dan de Casimir hierboven, uit dezelfde grote familie in Wokowice.")
person("agnes_ksiazek", "Agnes Książek", "f", None, None, None, line=L)
person("adalbert_kargol", "Wojciech (Adalbertus) Kargol", "m", "ca. 1817", "5-11-1845", "Wokowice", line=L,
       note="Zoon van Simon Kargol en Catharina Lis. Trouwde al op zijn 19e, op 26 januari 1836, met Salomea Kargol "
            "(21), ook een Kargol uit Wokowice. Overleed op 30-jarige leeftijd op huis nr. 57. Kinderen: Franciscus "
            "(1836), Martha (1838–1849), Matheus (1842–1849) en Veronica (1843, trouwde in 1868 met Adalbertus Książek). "
            "Martha en Matheus stierven in september 1849 kort na elkaar, in het jaar van de grote cholera-epidemie.",
       recs=[("Huwelijk 1836", "6VSB-K45C"), ("Begrafenis 1845", "6VST-8YG1")])
person("salomea_kargol", "Salomea Kargol", "f", "24-10-1814", "1-12-1855", "Wokowice", line=L,
       note="Dochter van Casimir Kargol en Agnes Książek. Weduwe in 1845; hertrouwde waarschijnlijk in 1850 met Simon "
            "Bach en overleed in 1855 in Wokowice.",
       recs=[("Doop 1814", "6V3G-W9RW"), ("Begrafenis 1855 (waarschijnlijk)", "6VST-VD3C")])
person("ferenc_kargol", "Ferenc (Franciscus) Kargol", "m", "9-10-1836", "26-6-1903", "Wokowice", fs="GQZ4-NK8", line=L,
       note="Geboren op huis nr. 57 in Wokowice, parochie Szczepanów. Zijn vader stierf toen hij negen was. Hij trouwde "
            "drie keer: in 1856, op zijn 19e, met Marianna Gładysz (zij stierf in april 1860, twee kinderen stierven als "
            "baby); op 2 juli 1860 met Marianna Latocha; en op 2 juli 1872, tien weken na haar dood, met Salomea Żurek "
            "(1849–1923). Met Salomea kreeg hij nog minstens negen kinderen, van wie de meesten jong stierven. "
            "Overleed op 66-jarige leeftijd op huis nr. 57.",
       recs=[("Doop 1836", "6V3V-J4C6"), ("Huwelijk 1856", "6V3M-6VNZ"), ("Huwelijk 1860", "6V3M-8WQS"),
             ("Huwelijk 1872", "6V3M-HT3X"), ("Begrafenis 1903", "6V3S-SM59")])
person("maria_latocha", "Marianna (Mária) Latocha", "f", "16-3-1832", "25-4-1872", "Wokowice", fs="GQZ4-JWC", line=L,
       note="Geboren op huis nr. 40 in Wokowice, een paar huizen van de Kargols, als dochter van Michael Latocha en "
            "Marianna Budzioch. Trouwde op 2 juli 1860 met Ferenc Kargol. Overleed op 25 april 1872 en werd twee dagen "
            "later in Szczepanów begraven. Haar zoon János was toen vier. Haar zus Agnes trouwde in 1863 met Stanislaus "
            "Kargol, haar broer Blasius in hetzelfde jaar met Elisabeth Kargol.",
       recs=[("Doop 1832", "6V3F-13NR"), ("Huwelijk 1860", "6V3M-8WQS")])
person("michael_latocha", "Michael Latocha", "m", "27-9-1806", "10-3-1870", "Wokowice", line=L,
       note="Geboren op huis nr. 40 in Wokowice, zoon van Martinus Latocha. Trouwde op 18 februari 1828, 22 jaar oud, "
            "met Marianna Budzioch, die toen pas 15 was. Kinderen o.a. Marianna (1832), Agnes (1835), Andreas "
            "(1837–1841), Blasius (1840), Veronica (1843), Michael (1844–1866), Martina (1844), Victoria (1846–1865) en "
            "Hyacinthus (1849–1853).",
       recs=[("Doop 1806", "6V3N-2MJV"), ("Huwelijk 1828", "6VSB-TX7T")])
person("marianna_budzioch", "Marianna Budzioch", "f", "3-6-1813", "19-10-1880", "Wokowice", line=L,
       note="Dochter van Joannes Budzioch en Agnes. Trouwde op haar 15e met Michael Latocha. Overleed in 1880 op huis nr. 40.",
       recs=[("Doop 1813", "6V3K-S7P4"), ("Begrafenis 1880", "6VST-8WSX")])
person("martinus_latocha", "Martinus Latocha", "m", "6-10-1783", "21-6-1849", "Wokowice", line=L,
       note="Zoon van Gaspar Latocha en Anna. Woonde op huis nr. 40 in Wokowice. Overleed in juni 1849, het jaar van de cholera.",
       recs=[("Doop 1783", "6VS1-3JQK"), ("Begrafenis 1849", "6VST-DKRC")])
person("marianna_drelicharz", "Marianna (Drelicharz?)", "f", None, None, "Wokowice", line=L,
       note="Bij de doop van haar zoon Michael (1806) staat alleen 'Marianna'. Bij de begrafenis van Martinus (1849) heet "
            "zijn vrouw Marianna Drelicharz, maar er komt ook een Martinus Latocha met Marianna Kwaśniak voor.")
person("gaspar_latocha", "Gaspar Latocha", "m", "ca. 1745", "16-12-1805", "Szczepanów", line=L,
       note="Oudste bekende Latocha. Verloor in maart 1798 binnen enkele dagen drie kinderen.")
person("anna_latocha", "Anna", "f", None, None, None, line=L)
person("joannes_budzioch", "Joannes Budzioch", "m", None, None, "Wokowice", line=L,
       note="Kinderen o.a. Joannes (1807), Agnes (1809), Josephus (1812), Marianna (1813), Salomea (1816), Sophia (1817), Helena (1821).")
person("agnes_budzioch", "Agnes", "f", None, None, None, line=L)
person("janos_kargol", "János Lőrinc Kargol", "m", "6-6-1867", "25-8-1936", "Wokowice", fs="LY13-M7K", line=L,
       note="Gedoopt als Joannes Laurentius op 7 juni 1867 in Szczepanów, geboren op huis nr. 57 in Wokowice. Zijn "
            "moeder stierf toen hij vier was. Trok naar Boedapest en werkte daar als hulpje van metselaars "
            "(kőműves napszámos). Bleef Oostenrijks staatsburger: in 1899 staat hij ingeschreven als 'Oostenrijks "
            "onderdaan uit Galicië, met woonrecht in Szczepanów (Wokowice)'. Woonde in Boedapest VIII (Köztemető út 87, "
            "1896), VII (Rózsa utca 15, 1897; Peterdy utca 11/A, 1899), in Újpest (Váci út 53, 1901) en vanaf ongeveer "
            "1908 in Kispest (Nagysándor József utca 157; in 1936 Kossuth Lajos utca 214). Bij de geboorte van Miklós in "
            "1908 staat hij in het register als 'Kargul János, rooms-katholiek, 40, dagloner'. Overleed op 25 augustus 1936 "
            "in het 10e district (Kőbánya); de overlijdensakte noemt zijn ouders 'Kargol Ferenc en Latóka Mária'.",
       recs=[("Doop 1867", "6VSB-7ZQM"), ("Overlijden 1936", "WQKQ-3NW2")])
person("marianna_kargol_1865", "Marianna Kargol", "f", "22-4-1865", None, "Wokowice", line=L,
       note="Oudere zus van János. Mogelijk dezelfde als de Maria, dochter van Franciscus Kargol en Maria Latocha, die "
            "op 16 januari 1898 in Szczepanów trouwde met Josephus Kargol.",
       recs=[("Doop 1865", "6V3N-K1YK"), ("Huwelijk 1898 (mogelijk)", "6V3M-9R35")])
person("ferenc_kargol_1869", "Franciscus Kargol", "m", "22-8-1869", "29-1-1870", "Wokowice", fs="G569-BKC", line=L,
       note="Stierf vijf maanden oud.", recs=[("Doop 1869", "6V3K-X8HL"), ("Begrafenis 1870", "6V3K-8KS1")])
person("henrik_kargol", "Henricus Joannes Kargol", "m", "12-1-1871", "22-5-1871", "Wokowice", fs="G56S-WZ8", line=L,
       note="Stierf vier maanden oud.", recs=[("Doop 1871", "6VSB-LCBC"), ("Begrafenis 1871", "6VSB-DR9M")])
person("salomea_zurek", "Salomea Żurek", "f", "ca. 1849", "1-1-1923", "Wokowice", line=L,
       note="Derde vrouw van Ferenc Kargol (1872), stiefmoeder van János. Kinderen o.a. Joannes (1873–1873), Salomea (1874), "
            "Franciscus Joannes (1875), Josephus Alexander (1877), Salomea (1882–1882), Franciscus (1884–1887) en "
            "Adalbertus (1886–1886). Overleed op huis nr. 57.",
       recs=[("Huwelijk 1872", "6V3M-HT3F"), ("Begrafenis 1923", "6V3S-SZL3")])

person("zsofia_kargol", "Zsófia Kargol", "f", "10-1-1896", "1993", "Boedapest", fs="G6LZ-1J3", line=L,
       note="Trouwde op 26 april 1915 in Pesterzsébet met Lajos Ambrus (geb. 1885). Kinderen: László (1912), "
            "Teréz (15-10-1915), Károly (1917) en György (1925). Werd 97.",
       recs=[("Huwelijk 1915", "6V9P-Y4JZ"), ("Geboorte dochter Teréz 1915", "6V1L-781G")])
person("lajos_ambrus", "Lajos Ambrus", "m", "1885", None, None, fs="G6LZ-RLS", line=L)
person("szaniszlo_kargol", "Szaniszló Kargol", "m", "8-5-1897", "12-7-1976", "Boedapest", fs="G6L7-4H2", line=L,
       note="Zijn naam is de Hongaarse vorm van Stanislaus, de heilige die in Szczepanów geboren is, het dorp van zijn "
            "vader. Trouwde op 20 mei 1918 in Boedapest met Karolina Horváth (geb. 1897). Zoon László, geboren 19-7-1920.",
       recs=[("Overlijden 1976", "6J3Z-CHQ5"), ("Geboorte zoon László 1920", "6JBS-4255")])
person("karolina_horvath", "Karolina Horváth", "f", "1897", None, None, fs="G6L7-94B", line=L)
person("anna_kargol", "Anna Kargol", "f", "28-6-1899", "7-10-1901", "Boedapest", fs="G6LQ-DQD", line=L,
       note="Overleed op tweejarige leeftijd in Újpest.")
person("andras_kagol", "András Kagol (Kargol)", "m", "7-3-1901", None, "Boedapest", fs="G3S4-W4N", line=L,
       note="Geboren in de binnenstad van Boedapest (Belváros-Lipótváros, 5e district). Woonde in 1926 op Báthory utca 10 "
            "in het 5e district. Trouwde daar op 5 januari 1926 met Mária Fridlik (akte nr. 11). In de akten wisselt "
            "zijn achternaam: Kagol, Kágol, Kargol.",
       recs=[("Huwelijk 1926", "QLLC-SLCN")])
person("maria_kargol", "Mária Kargol", "f", "12-6-1903", None, "Bánhida", fs="GDRM-J7G", line=L,
       note="Geboren in Bánhida (nu Tatabánya), ruim 50 km van Boedapest; waarom het gezin daar toen was, is onbekend. Trouwde op 20 oktober 1928 in Boedapest met "
            "Ferenc Schneider (1904–1963). Zoon Paul (geb. 21-5-1939 Boedapest) vertrok in 1957 naar de Verenigde Staten; "
            "zoon Ferenc stierf als baby in mei 1945.",
       recs=[("Overlijden zoontje Ferenc 1945", "QP5Y-36DB"), ("Zoon Paul in de VS", "6K7G-DX6D")])
person("ferenc_schneider", "Ferenc Schneider", "m", "1904", "1963", None, fs="GDRM-VH3", line=L)
person("miklos_kargul", "Miklós Kargul", "m", "5-12-1908", "3-7-1985", "Kispest", fs="LJ1J-RHB", line=L,
       note="Geboren in Kispest (Petőfi utca 148). Op zijn geboorteakte staat: 'het kind is, net als zijn vader, "
            "Oostenrijks onderdaan uit Galicië met woonrecht in Szczepanów'. Woonde rond 1931 in Várpalota met Terézia "
            "Oszvári; trouwde op 27 november 1937 in Boedapest met Erzsébet Tóth (1914–1992). Zoon Miklós (1938–2016).")
person("erzsebet_toth", "Erzsébet Tóth", "f", "1914", "1992", None, fs="LY1Q-H59", line=L)
person("ilona_kargol", "Ilona Kargol", "f", "1910", "19-2-1911", "Kispest", fs="G6LQ-LY8", line=L,
       note="Overleed drie maanden oud in Kispest.", recs=[("Overlijden 1911", "6V12-53YD")])
person("zoon_kargol_1914", "Zoon Kargol", "m", "10-9-1914", "10-9-1914", "Boedapest", fs="PS4S-B57", line=L,
       note="Doodgeboren zoon.", recs=[("Geboorteakte 1914", "6BN2-HBBJ")])

# --- Savrnoch / Chovan (Lúčky, Liptov -> Boedapest) ---
S = "savrnoch"
person("mihaly_savrnoch", "Mihály Savrnoch", "m", "ca. 1830", "24-4-1897", "Lúčky", fs="L75F-18V", line=S,
       note="Geboren in Lúčky in de streek Liptov (nu Slowakije). Kwam tussen 1880 en 1883 met zijn gezin naar "
            "Boedapest. Overleed op Népszínház utca 55 in het 8e district.")
person("maria_chovan", "Mária Chovan", "f", "26-4-1849", "21-1-1924", "Lúčky", fs="L75F-18K", line=S,
       note="Gedoopt in Lúčky op 26 april 1849, dochter van András Chovan en Mária Siroky. Overleed in Pesterzsébet.")
person("andras_chovan", "András Chovan", "m", None, None, "Lúčky", fs="G6GX-Q1N", line=S)
person("maria_siroky", "Mária Siroky", "f", None, None, "Lúčky", fs="G6GX-DKJ", line=S)
person("zsuzsanna_savrnoch", "Zsuzsanna Savrnoch", "f", "30-9-1875", "19-10-1945", "Lúčky", fs="LY1S-PL6", line=S,
       note="Geboren in Lúčky en daar op 2 oktober 1875 gedoopt. Kwam als kind naar Boedapest. Kreeg met János Kargol "
            "acht kinderen. Overleed in oktober 1945 in het 12e district van Boedapest, 71 jaar oud. In akten ook "
            "Savernoch, Savernok, Saverno of Saurnoch genoemd. In 1911 zat ze vier maanden in de gevangenis (13 mei – "
            "13 september) wegens hulp bij een diefstal. Het gevangenisregister beschrijft haar: 1,50 m, stevig, rond "
            "gezicht, lichtbruin haar, blauwe ogen. Moedertaal Slowaaks, sprak ook Hongaars en Duits, kon niet lezen of "
            "schrijven, zes kinderen, 'kosten niet te verhalen' (geen bezit).",
       recs=[("Overlijden 1945", "QPLV-Q91D"),
             ("Gevangenisregister 1911 (scan)", "https://www.familysearch.org/en/tree/person/memories/LY13-M7K")])
person("anna_savrnoch", "Anna Savrnoch", "f", "27-9-1877", "1919", "Lúčky", fs="LY1H-P8Y", line=S,
       note="Trouwde op 11 juni 1899 in Boedapest met Géza Giczy (geb. 1876); vier kinderen.")
person("jozsef_savrnoch", "József Savrnoch", "m", "14-3-1880", "28-11-1903", "Lúčky", fs="LY1H-G83", line=S,
       note="Overleed op 23-jarige leeftijd in Boedapest (Teleki tér 25).")
person("maria_savrnoch", "Mária Savrnoch", "f", "6-12-1883", None, "Boedapest", fs="L75F-18J", line=S,
       note="Het eerste kind dat in Boedapest geboren werd; gedoopt in de Terézváros-parochie.")
person("janos_savrnoch", "János Savrnoch", "m", "9-3-1885", "9-4-1960", "Boedapest", fs="G6L9-FZV", line=S,
       note="Trouwde in 1914 met Erzsébet Karaffa. Woonde op het eind in Kacsa utca 9 (2e district).")

# --- Fridlik / Kunyik (Pilis) ---
F = "fridlik"
person("istvan_fridlik", "István Fridlik", "m", None, None, "Pilisszántó", fs="G3S4-JRQ", line=F)
person("erzsebet_kunyik", "Erzsébet Kunyik", "f", None, None, "Pilisszántó", fs="LH5Q-HGK", line=F,
       note="De familie Kunyik woonde al vóór 1850 in Tinnye, het buurdorp van Pilisszántó. Of Erzsébet daar vandaan "
            "komt, is nog niet bewezen.")
person("maria_fridlik", "Mária Fridlik", "f", "4-9-1894", "21-5-1961", "Pilisszántó", fs="G3S4-4TB", line=F,
       note="Geboren in Pilisszántó, een Slowaaks dorp in het Pilisgebergte ten noordwesten van Boedapest. "
            "Trouwde op 31-jarige leeftijd met András Kagol. In de huwelijksakte staat 'Fridlik, niet Fridrik'.",
       recs=[("Overlijden 1961", "XSLW-5N71")])

# --- Bán / Zele (Szabolcs) ---
B = "ban"
person("sandor_ban", "Sándor Bán", "m", None, None, None, line=B, recs=[("Genoemd in huwelijk zoon 1896", "6NK9-HP42")])
person("julianna_hagymasi", "Juliánna Hagymási", "f", None, None, None, line=B)
person("istvan_ban", "István Bán", "m", "1870", None, "Nagyhalász", fs="GKW8-KGC", line=B,
       note="Trouwde op 9 januari 1896 in Nagyhalász (comitaat Szabolcs, Noordoost-Hongarije) met Borbála Zele. "
            "Het gezin verhuisde tussen de dorpen van de streek: Nyírbogdány (1896), Dombrád (1901), Nagyhalász (1902), "
            "Ibrány (1904).", recs=[("Huwelijk 1896", "6NK9-HP42")])
person("borbala_zele", "Borbála Zele", "f", "1878", None, None, fs="GKW8-JMP", line=B,
       note="Dochter van Gáspár Zele en Veronika Kovács. Een Borbála Zele met precies deze ouders werd in 1878 gedoopt "
            "in Füzesabony (comitaat Heves); waarschijnlijk is zij het, maar dat is nog niet bewezen.")
person("gaspar_zele", "Gáspár Zele", "m", None, None, None, fs="G581-HL7", line=B)
person("veronika_kovacs", "Veronika Kovács", "f", None, None, None, fs="G581-N8T", line=B)
person("ferencz_ban", "Ferencz Bán", "m", "7-5-1896", None, "Nyírbogdány", line=B, recs=[("Geboorte 1896", "6NVB-BQTQ")])
person("jozsef_ban_1901", "József Bán", "m", None, "29-5-1901", "Dombrád", line=B, note="Jong gestorven.")
person("margit_ban", "Margit Bán", "f", None, "10-9-1902", "Nagyhalász", line=B, note="Jong gestorven.")
person("jozsef_ban", "József Bán", "m", "7-1-1904", "15-2-1958", "Ibrány", fs="P6XX-89L", line=B,
       note="Geboren in Ibrány (Szabolcs). Kreeg dezelfde naam als een broertje dat in 1901 was gestorven. Trouwde op "
            "19 maart 1927 met Margit Borbély en verhuisde later naar Boedapest, waar hij in februari 1958 overleed.",
       recs=[("Geboorte 1904", "6NV1-X6WP"), ("Huwelijk 1927", "6V1T-7LBS"), ("Overlijden 1958", "6GL3-TVR3")])
person("gyorgy_ban", "György Bán", "m", "1914", None, None, fs="GKW8-ZXK", line=B,
       note="Trouwde op 13 juni 1936 met Anna Csák.", recs=[("Huwelijk 1936", "6V1T-4P6R")])

# --- Borbély / Csernai (Szabolcs) ---
O = "borbely"
person("janos_borbely", "János Borbély", "m", None, None, None, fs="GXMS-MPZ", line=O)
person("zsuzsanna_berecz", "Zsuzsánna Berecz", "f", None, None, None, fs="GXM9-B3G", line=O)
person("sandor_borbely", "Sándor Borbély", "m", "19-5-1887", None, None, fs="GJGV-STB", line=O,
       note="Trouwde op 29 november 1910 in Vasmegyer (Szabolcs) met Karolina Csernai. Het gezin woonde later in "
            "Nyírbogdány.")
person("karolina_csernai", "Karolina Csernai", "f", "1892", None, None, fs="LCSX-HVZ", line=O)
person("margit_borbely", "Margit Borbély", "f", "1909", None, None, fs="P6XX-LF9", line=O,
       note="Trouwde op 19 maart 1927 met József Bán; ze was toen ongeveer 18. Volgens de stamboom geboren in 1909, "
            "een jaar vóór het huwelijk van haar ouders; dat moet nog gecontroleerd worden.",
       recs=[("Huwelijk 1927", "6V1T-7LBS")])
person("julianna_borbely", "Julianna Borbély", "f", "1911", "30-9-1911", "Vasmegyer", fs="GJGV-9YK", line=O)
person("sandor_borbely_1913", "Sándor Borbély", "m", "19-11-1913", "1997", "Nyírbogdány", fs="GJGV-MCG", line=O)
person("ilona_borbely", "Ilona Borbély", "f", "1918", "2004", None, fs="GJGJ-TNX", line=O)
person("erzsebet_borbely", "Erzsébet Borbély", "f", "1921", None, None, fs="GJGV-79T", line=O,
       note="Trouwde op 4 september 1939 in Nyírbogdány met István Erős.")

# --- The couple ---
person("laszlo_ban", "László Bán", "m", "1934", "2021", None, fs="GP82-VG8", line=B,
       note="Zoon van József Bán en Margit Borbély. Trouwde met de dochter van András Kagol en Mária Fridlik. "
            "Zijn geboorteakte is nog niet gevonden (akten uit de jaren 1930 zijn online nauwelijks doorzoekbaar).")
person("dochter_kagol", "Dochter van András en Mária", "f", None, None, None, line=L,
       note="Nog levend of recent overleden; daarom zonder naam en data op deze site.")

# Couples: husband, wife, marriage, children, parents (= couple ids of the husband's and wife's parents)
C = {
    "c_root": dict(h="laszlo_ban", w="dochter_kagol", marr=None, children=[], parents=["c_ban_borbely", "c_kagol_fridlik"]),
    "c_ban_borbely": dict(h="jozsef_ban", w="margit_borbely", marr="19-3-1927", children=["laszlo_ban"],
                          parents=["c_ban_zele", "c_borbely_csernai"]),
    "c_kagol_fridlik": dict(h="andras_kagol", w="maria_fridlik", marr="5-1-1926, Boedapest", children=["dochter_kagol"],
                            parents=["c_kargol_savrnoch", "c_fridlik_kunyik"]),
    "c_ban_zele": dict(h="istvan_ban", w="borbala_zele", marr="9-1-1896, Nagyhalász",
                       children=["ferencz_ban", "jozsef_ban_1901", "margit_ban", "jozsef_ban", "gyorgy_ban"],
                       parents=["c_ban_hagymasi", "c_zele_kovacs"]),
    "c_borbely_csernai": dict(h="sandor_borbely", w="karolina_csernai", marr="29-11-1910, Vasmegyer",
                              children=["margit_borbely", "julianna_borbely", "sandor_borbely_1913", "ilona_borbely",
                                        "erzsebet_borbely"], parents=["c_borbely_berecz", None]),
    "c_kargol_savrnoch": dict(h="janos_kargol", w="zsuzsanna_savrnoch", marr="4-8-1895, Boedapest",
                              children=["zsofia_kargol", "szaniszlo_kargol", "anna_kargol", "andras_kagol", "maria_kargol",
                                        "miklos_kargul", "ilona_kargol", "zoon_kargol_1914"],
                              parents=["c_kargol_latocha", "c_savrnoch_chovan"]),
    "c_fridlik_kunyik": dict(h="istvan_fridlik", w="erzsebet_kunyik", marr=None, children=["maria_fridlik"], parents=[None, None]),
    "c_ban_hagymasi": dict(h="sandor_ban", w="julianna_hagymasi", marr=None, children=["istvan_ban"], parents=[None, None]),
    "c_zele_kovacs": dict(h="gaspar_zele", w="veronika_kovacs", marr=None, children=["borbala_zele"], parents=[None, None]),
    "c_borbely_berecz": dict(h="janos_borbely", w="zsuzsanna_berecz", marr=None, children=["sandor_borbely"], parents=[None, None]),
    "c_kargol_latocha": dict(h="ferenc_kargol", w="maria_latocha", marr="2-7-1860, Szczepanów",
                             children=["marianna_kargol_1865", "janos_kargol", "ferenc_kargol_1869", "henrik_kargol"],
                             parents=["c_adalbert_salomea", "c_latocha_budzioch"]),
    "c_adalbert_salomea": dict(h="adalbert_kargol", w="salomea_kargol", marr="26-1-1836, Szczepanów",
                               children=["ferenc_kargol"], parents=["c_simon_lis", "c_casimir_ksiazek"]),
    "c_latocha_budzioch": dict(h="michael_latocha", w="marianna_budzioch", marr="18-2-1828, Szczepanów",
                               children=["maria_latocha"], parents=["c_martin_latocha", "c_budzioch"]),
    "c_martin_latocha": dict(h="martinus_latocha", w="marianna_drelicharz", marr=None, children=["michael_latocha"],
                             parents=["c_gaspar_latocha", None]),
    "c_gaspar_latocha": dict(h="gaspar_latocha", w="anna_latocha", marr=None, children=["martinus_latocha"],
                             parents=[None, None]),
    "c_budzioch": dict(h="joannes_budzioch", w="agnes_budzioch", marr=None, children=["marianna_budzioch"],
                       parents=[None, None]),
    "c_simon_lis": dict(h="simon_kargol", w="catharina_lis", marr="16-2-1806, Szczepanów", children=["adalbert_kargol"],
                        parents=["c_casimir_grochola", "c_lis"]),
    "c_casimir_ksiazek": dict(h="casimir_kargol", w="agnes_ksiazek", marr=None, children=["salomea_kargol"],
                              parents=[None, None]),
    "c_casimir_grochola": dict(h="casimir_kargol_sr", w="agnes_grochola", marr=None, children=["simon_kargol"],
                               parents=[None, None]),
    "c_lis": dict(h="stanislaus_lis", w="theresia_lis", marr=None, children=["catharina_lis"], parents=[None, None]),
    "c_savrnoch_chovan": dict(h="mihaly_savrnoch", w="maria_chovan", marr=None,
                              children=["zsuzsanna_savrnoch", "anna_savrnoch", "jozsef_savrnoch", "maria_savrnoch", "janos_savrnoch"],
                              parents=[None, "c_chovan_siroky"]),
    "c_chovan_siroky": dict(h="andras_chovan", w="maria_siroky", marr=None, children=["maria_chovan"], parents=[None, None]),
}
# Spouses of children (shown in the family panel)
SPOUSE = {"zsofia_kargol": "lajos_ambrus", "szaniszlo_kargol": "karolina_horvath", "maria_kargol": "ferenc_schneider",
          "miklos_kargul": "erzsebet_toth", "andras_kagol": "maria_fridlik", "jozsef_ban": "margit_borbely",
          "zsuzsanna_savrnoch": "janos_kargol", "ferenc_kargol": "maria_latocha", "laszlo_ban": "dochter_kagol"}

for cid, c in C.items():
    c["id"] = cid
for pid, sp in SPOUSE.items():
    P[pid]["spouse"] = sp

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "data", "familie.json")
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump({"people": P, "couples": C, "root": "c_root"}, fh, ensure_ascii=False, indent=1)
print(len(P), "personen,", len(C), "paren ->", os.path.normpath(out))
