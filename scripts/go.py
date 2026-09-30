import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
# usage: go.py outprefix url [url...]
pref=sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx=b.contexts[0]
    pg=[x for x in ctx.pages if x.url.startswith("http") and "family-trees" not in x.url]
    pg=pg[0] if pg else ctx.new_page()
    for k,u in enumerate(sys.argv[2:]):
        pg.goto(u, wait_until="domcontentloaded"); time.sleep(3)
        t=pg.inner_text("body")
        fn=f"{pref}_{k}.txt"; open(fn,"w",encoding="utf-8").write(pg.url+"\n"+t)
        print("=====",u,"->",fn,len(t))
