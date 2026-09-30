import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    for pid in sys.argv[1:]:
        pg.goto(f"https://www.familysearch.org/en/tree/person/details/{pid}", wait_until="domcontentloaded")
        for _ in range(20):
            time.sleep(1.2); t=pg.inner_text("body")
            if t.count("Kargol")+t.count("Kagol")+t.count("Kargul")+t.count("Savr")+t.count("Fridlik")+t.count("Bán")+t.count("Ban ")+t.count("Borb")+t.count("Zele")>=3: break
        time.sleep(4)
        # expand family sections if any
        t=pg.inner_text("body")
        open(f"tree_{pid}.txt","w",encoding="utf-8").write(t)
        i=t.find("Vitals"); e=t.find("Research Help") if "Research Help" in t else len(t)
        body=[x.strip() for x in t[i:e].split("\n") if x.strip()]
        print("#####",pid); print(" | ".join(body)[:2600])
