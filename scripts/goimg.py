import sys, time, re
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
# usage: goimg.py OWC N [N...] -> for each image number, opens it and downloads dist.jpg as img_<tag>_<N>.jpg
owc=sys.argv[1]; tag=sys.argv[2]; nums=[int(x) for x in sys.argv[3:]]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg=[x for x in b.contexts[0].pages if "familysearch.org" in x.url][0]
    pg.bring_to_front()
    pg.goto(f"https://www.familysearch.org/search/image/index?owc={owc}&cc=1452460"); time.sleep(10)
    for n in nums:
        box=pg.locator("input[type=number], input[aria-label*='mage'], input[aria-label*='Image']").first
        box.fill(str(n)); box.press("Enter"); time.sleep(6)
        url=pg.url
        m=re.search(r"3:1:[A-Z0-9-]+", url) or re.search(r"3:1:[A-Z0-9-]{10,}", pg.content())
        ark=m.group(0) if m else None
        print(n, url[:120], ark)
        if ark:
            r=pg.request.get(f"https://sg30p0.familysearch.org/service/records/storage/deepzoomcloud/dz/v1/{ark}/dist.jpg")
            if r.ok: open(f"img_{tag}_{n}.jpg","wb").write(r.body()); print("  saved", len(r.body()))
