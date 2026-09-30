import sys, time, re
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    for pid in sys.argv[1:]:
        pg.goto(f"https://www.familysearch.org/en/tree/person/sources/{pid}", wait_until="domcontentloaded")
        for _ in range(20):
            time.sleep(1.5)
            if "Created" in pg.inner_text("body"): break
        time.sleep(2)
        html=pg.content()
        arks=list(dict.fromkeys(re.findall(r"ark:/61903/1:1:([A-Z0-9-]+)", html)))
        t=pg.inner_text("body"); i=t.find("Sources ("); e=t.find("About\nVolunteer")
        print("#####",pid, arks); print(" | ".join(x for x in t[i:e].split("\n") if x.strip())[:1500])
