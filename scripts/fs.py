import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
out, q = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    pg.goto("https://www.familysearch.org/en/search/record/results?"+q+"&count=100", wait_until="domcontentloaded")
    for _ in range(20):
        time.sleep(1.5)
        t=pg.inner_text("body")
        if "Record Search Results" in t and "Links" in t: break
    time.sleep(1.5); t=pg.inner_text("body")
    open(out,"w",encoding="utf-8").write(pg.url+"\n"+t)
    links=pg.eval_on_selector_all("a[href*='ark:/61903/1:1:']","els=>els.map(e=>e.innerText.trim()+'\t'+e.href)")
    open(out[:-4]+".links","w",encoding="utf-8").write("\n".join(dict.fromkeys(links)))
    print(pg.url, len(t), len(links))
