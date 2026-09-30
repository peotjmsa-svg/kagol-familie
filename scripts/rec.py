import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    for a in sys.argv[1:]:
        pg.goto(f"https://www.familysearch.org/ark:/61903/1:1:{a}?lang=en", wait_until="domcontentloaded")
        for _ in range(15):
            time.sleep(1.2); t=pg.inner_text("body")
            if "Document Information" in t or "Collection" in t and len(t)>1500: break
        time.sleep(1); t=pg.inner_text("body")
        open(f"rec_{a}.txt","w",encoding="utf-8").write(t)
        pass
