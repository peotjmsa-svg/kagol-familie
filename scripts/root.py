import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for c in b.contexts for x in c.pages if "family-trees" in x.url][0]
    for i in sys.argv[1:]:
        pg.goto(f"https://www.myheritage.nl/family-trees/sonja-oosterom-florian-hillen/OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI?rootIndivudalID={i}&familyTreeID=1", wait_until="domcontentloaded")
        time.sleep(5)
        for lab in ("FEITEN","DIRECTE FAMILIE"):
            try:
                pg.get_by_text(lab, exact=False).first.click(force=True, timeout=3000); time.sleep(1)
            except Exception as e: print("noclick", lab)
        pg.screenshot(path=f"root_{i}.png")
        h = pg.content(); open(f"root_{i}.html","w",encoding="utf-8").write(h)
        t = pg.inner_text("body"); open(f"root_{i}.txt","w",encoding="utf-8").write(t)
        k = t.find("Profiel"); print("=====", i); print(t[max(0,k-300):k+1500])
