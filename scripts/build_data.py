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
        + [{"label": lab, "url": FS_REC + rid} for lab, rid in recs],
    }


# --- Kargol (Szczepanów, Galicië -> Boedapest) ---
L = "kargol"
person("ferenc_kargol", "Ferenc Kargol", "m", place="Szczepanów", fs="GQZ4-NK8", line=L,
       note="Woonde in Szczepanów, een dorp bij Brzesko in Galicië (toen Oostenrijk, nu Polen).")
person("maria_latocha", "Mária Latocha", "f", "1833", "25-4-1872", "Szczepanów", fs="GQZ4-JWC", line=L,
       note="Overleed op 25 april 1872 in Szczepanów en werd daar op 27 april begraven. Ze werd maar 39.")
person("janos_kargol", "János Lőrinc Kargol", "m", "6-6-1867", "25-8-1936", "Szczepanów", fs="LY13-M7K", line=L,
       note="Geboren in Szczepanów (Galicië). Trok naar Boedapest en werkte daar als hulpje van metselaars "
            "(kőműves napszámos). Bleef Oostenrijks staatsburger: in 1899 staat hij ingeschreven als 'Oostenrijks "
            "onderdaan uit Galicië, met woonrecht in Szczepanów'. Woonde in Boedapest VIII (Köztemető út 87, 1896), "
            "VII (Rózsa utca 15, 1897; Peterdy utca 11/A, 1899), in Újpest (Váci út 53, 1901) en vanaf ongeveer 1908 in "
            "Kispest (Nagysándor József utca 157; in 1936 Kossuth Lajos utca 214). Overleed in Boedapest.")
person("ferenc_kargol_1869", "Ferenc Kargol", "m", "1869", None, "Szczepanów", fs="G569-BKC", line=L)
person("ferenc_kargol_1870", "Ferenc Kargol", "m", "1870", "1870", "Szczepanów", fs="G56S-3MB", line=L)
person("henrik_kargol", "Henrik Kargol", "m", "1871", "1871", "Szczepanów", fs="G56S-WZ8", line=L)
person("jozsef_kargol", "József Kargol", "m", None, None, "Szczepanów", fs="G56S-75Q", line=L)

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
            "Savernoch, Savernok, Saverno of Saurnoch genoemd.",
       recs=[("Overlijden 1945", "QPLV-Q91D")])
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
    "c_kargol_latocha": dict(h="ferenc_kargol", w="maria_latocha", marr=None,
                             children=["janos_kargol", "ferenc_kargol_1869", "ferenc_kargol_1870", "henrik_kargol", "jozsef_kargol"],
                             parents=[None, None]),
    "c_savrnoch_chovan": dict(h="mihaly_savrnoch", w="maria_chovan", marr=None,
                              children=["zsuzsanna_savrnoch", "anna_savrnoch", "jozsef_savrnoch", "maria_savrnoch", "janos_savrnoch"],
                              parents=[None, "c_chovan_siroky"]),
    "c_chovan_siroky": dict(h="andras_chovan", w="maria_siroky", marr=None, children=["maria_chovan"], parents=[None, None]),
}
# Spouses of children (shown in the family panel)
SPOUSE = {"zsofia_kargol": "lajos_ambrus", "szaniszlo_kargol": "karolina_horvath", "maria_kargol": "ferenc_schneider",
          "miklos_kargul": "erzsebet_toth", "andras_kagol": "maria_fridlik", "jozsef_ban": "margit_borbely",
          "zsuzsanna_savrnoch": "janos_kargol", "laszlo_ban": "dochter_kagol"}

for cid, c in C.items():
    c["id"] = cid
for pid, sp in SPOUSE.items():
    P[pid]["spouse"] = sp

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "data", "familie.json")
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump({"people": P, "couples": C, "root": "c_root"}, fh, ensure_ascii=False, indent=1)
print(len(P), "personen,", len(C), "paren ->", os.path.normpath(out))
