import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
db, q = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "mnl.gov.hu" in x.url][0]
    pg.goto(f"https://adatbazisokonline.mnl.gov.hu/adatbazis/{db}", wait_until="domcontentloaded"); time.sleep(2)
    inp = pg.locator("#q")
    inp.fill(q); inp.press("Enter"); time.sleep(4)
    t=pg.inner_text("body"); print(pg.url)
    i=t.find("találat"); print(t[i-20:i+6000])
