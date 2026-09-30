import sys, time, re, json
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
# usage: vol.py OWC OUT  -> collects image arks from a waypoint volume page
owc, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    got=[]
    def h(r):
        if "image-data" in r.url or "waypoint" in r.url or "filmdatainfo" in r.url:
            try: got.append(r.json())
            except: pass
    pg.on("response", h)
    pg.goto(f"https://www.familysearch.org/search/image/index?owc={owc}&cc=1452460"); time.sleep(12)
    html=pg.content()
    arks=list(dict.fromkeys(re.findall(r"3:1:[A-Z0-9-]{8,}", html)))
    t=pg.inner_text("body"); m=re.search(r"of\s*(\d+)", t)
    print("images", m.group(1) if m else "?", "arks in html", len(arks), "json", len(got))
    json.dump({"arks":arks,"json":got}, open(out,"w"))
