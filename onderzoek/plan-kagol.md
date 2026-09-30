# Research plan: the Kagol/Kargol line back in time

Scope (user, 2026-09-30): only the direct Kagol/Kargol line and the women who married into it. Goal: go back as
far as the records allow. Other families (Savrnoch, Fridlik, Borbély) and side branches are out of scope.
An earlier plan about András Kagol's own life (occupation, death, children) is kept at the bottom as "later".

## The line so far (all Wokowice, parish Szczepanów, unless noted)

| Gen. | Man | Wife | Source strength |
|------|-----|------|-----------------|
| 1 | András Kagol, b. 1901 Budapest | Mária Fridlik | civil records |
| 2 | János Lőrinc Kargol, 1867–1936, Budapest | Zsuzsanna Savrnoch | civil + church, proven |
| 3 | Ferenc (Franciscus) Kargol, 1836–1903, house 57 | Marianna Latocha, 1832–1872 (house 40) | church records, proven |
| 4 | Wojciech (Adalbertus) Kargol, ca. 1817–1845, house 57 | Salomea Kargol, 1814–1855 | marriage 1836 names both sets of parents |
| 5 | Simon Kargol, ca. 1777–1834, house 57 | Catharina Lis, ca. 1788 | marriage 1806, burial 1834 |
| 6 | Casimir Kargol, ca. 1751–1815, house 57 | Agnes Grochola | burial 1815; children's baptisms 1776–1789 |
| 7 | ? | ? | **the wall: nothing indexed before ca. 1772 for baptisms** |

Second Kargol line through Salomea (gen. 4): her father Casimir Kargol × Agnes Książek. Probably the Casimir born
1773, son of Antonius Kargol, who married an Agnes on 26 Feb 1797 – to be proven.

## What the sources allow

- **FamilySearch "Poland, Church Books"** (logged in): Szczepanów marriages are indexed back to **1654**, burials back to
  about 1789, baptisms only from about **1772**. The scans are browsable: baptisms on film **004666200** (704 images),
  marriages on film **004666204** (761 images). Before 1772 the baptisms must be read from the scans (Latin handwriting).
- **House numbers** start with the Austrian census of about 1784. Before that, people can only be matched by names,
  ages, godparents and witnesses.
- **Josephine cadastre (Metryka józefińska, 1785–1788)** and **Franciscan cadastre (Metryka franciszkańska, ca. 1820)**:
  land registers per village, listing the owner of every house number and his land. These would show who held
  house 57 in Wokowice and how much land the Kargols had. Kept in Lviv (TsDIAL, fond 19) and the National Archives in
  Kraków; partly online (szukajwarchiwach.gov.pl, TsDIAL scans).
- **szukajwarchiwach.gov.pl**: Szczepanów parish books 1890–1919 (free scans); useful only to check the Wokowice
  family after János left.
- **Geneteka** (Polish Genealogical Society index): check whether Szczepanów is indexed there, possibly with years that
  FamilySearch lacks.

## Steps

1. **Close the gaps in what we have** (quick, index only)
   - Prove Salomea's father: open the 1797 marriage (Casimir × Agnes), check the bride's surname is Książek; find
     Salomea's parents' other children. If proven, the Antonius Kargol × Eva line (married 9 Nov 1760) becomes a second
     Kargol line into the 1700s.
   - Simon's baptism (ca. 1777–1778): browse film 004666200 around 1776–1779 for "Simon, son of Casimir Kargol and Agnes".
   - Catharina Lis: confirm her 1788 baptism (house number, parents Stanislaus Lis and Theresia).
2. **Break through the wall at Casimir (born ca. 1751)**
   - Browse film 004666204 (marriages) around **1770–1777** for Casimir Kargol × Agnes Grochola: the entry may give
     his age, his house and sometimes his father.
   - Browse film 004666200 (baptisms) around **1749–1753** for a Casimir Kargol; note parents and godparents.
   - Cross-check with the indexed Kargol marriages of **1745–1752** (Stanislaus × Regina Boryczkówna 1747,
     Thomas × Regina Kuba 1750, Albertus × Marianna 1751, ...) to find the likely parents.
   - Check Kargol burials 1789–1815 with no house number or with house 57 (for example Adalbertus Kargol b. 1718 d. 1800,
     Agatha Kargol b. 1724 d. 1796 "daughter of Blasius Kargol").
3. **Go further back through the marriage index (1654–1750)**
   - Build a table of all indexed Kargol marriages in Szczepanów 1654–1777 and link generations by names and dates.
   - For each step, open the scan to read ages, fathers and witnesses.
4. **Land and house: the Josephine cadastre (1785–1788) for Wokowice**
   - Find out if the Wokowice/Szczepanów volume survives and is online (TsDIAL fond 19, szukajwarchiwach). If so, read
     who owned house 57 and how much land. Same for the Franciscan cadastre (ca. 1820).
5. **Wives' lines, one generation each** (only as far as needed to fix the Kargol line): Grochola, Lis, Latocha
   (already back to Gaspar, ca. 1745), Budzioch, Książek.
6. **Where the name comes from**: check the oldest entries (1654 and before) and local histories of Szczepanów and
   Wokowice for the Kargol family (village history, parish history).

## How results are recorded
Every find goes into `onderzoek/familysearch.md` with the record id or film and image number. Proven links go into
`scripts/build_data.py` and the site; probable links are marked "waarschijnlijk" on the site.

## Later: András Kagol's own life (earlier plan)
Occupation, addresses and death of András Kagol; children's births 1926–1940; Budapest address books; citizenship
(the family were Austrian/Galician subjects); the daughter and László Bán after 1956.
