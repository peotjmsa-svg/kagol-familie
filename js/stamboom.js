// Voorouderboom per echtpaar (D3). Onderaan het paar László Bán × dochter Kagol, daarboven hun ouders, enzovoort.
(function () {
  "use strict";
  const BOX_W = 250, BOX_H = 62, GAP_X = 24, GAP_Y = 70;
  let DATA, svg, g, zoom, selected;

  const LINE_COLOR = (line) => getComputedStyle(document.documentElement).getPropertyValue("--" + (line || "muted")).trim();
  const P = (id) => DATA.people[id];
  const years = (p) => {
    if (!p) return "";
    const y = (s) => (s ? String(s).split("-").pop().replace("ca. ", "ca. ") : "");
    const b = y(p.born), d = y(p.died);
    if (!b && !d) return "";
    return (b || "?") + " – " + (d || "");
  };
  const fmtDate = (s) => {
    if (!s) return "";
    const m = String(s).match(/^(\d+)-(\d+)-(\d+)$/);
    if (!m) return s;
    const maand = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"];
    return `${+m[1]} ${maand[+m[2] - 1]} ${m[3]}`;
  };
  const esc = (s) => String(s || "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function toHierarchy(cid) {
    const c = DATA.couples[cid];
    const node = { id: cid, c };
    const kids = (c.parents || []).filter(Boolean).map(toHierarchy);
    if (kids.length) node.children = kids;
    return node;
  }

  function draw() {
    const root = d3.hierarchy(toHierarchy(DATA.root));
    d3.tree().nodeSize([BOX_W + GAP_X, BOX_H + GAP_Y]).separation((a, b) => (a.parent === b.parent ? 1 : 1.15))(root);
    // Root at the bottom: flip y
    root.each((d) => (d.y = -d.y));

    svg = d3.select("#tree").append("svg");
    g = svg.append("g");
    zoom = d3.zoom().scaleExtent([0.25, 2.5]).on("zoom", (e) => g.attr("transform", e.transform));
    svg.call(zoom);

    g.selectAll("path.link").data(root.links()).join("path").attr("class", "link")
      .attr("d", (l) => {
        const sx = l.source.x, sy = l.source.y - BOX_H / 2, tx = l.target.x, ty = l.target.y + BOX_H / 2, my = (sy + ty) / 2;
        return `M${sx},${sy} C${sx},${my} ${tx},${my} ${tx},${ty}`;
      });

    const node = g.selectAll("g.couple").data(root.descendants()).join("g")
      .attr("class", "couple").attr("transform", (d) => `translate(${d.x - BOX_W / 2},${d.y - BOX_H / 2})`)
      .style("cursor", "pointer").on("click", (e, d) => select(d.data.id));
    node.append("rect").attr("width", BOX_W).attr("height", BOX_H).attr("rx", 8);
    node.each(function (d) {
      const n = d3.select(this), h = P(d.data.c.h), w = P(d.data.c.w);
      [[h, 0], [w, BOX_H / 2]].forEach(([p, y]) => {
        n.append("rect").attr("class", "bar").attr("x", 0).attr("y", y + 4).attr("width", 5).attr("height", BOX_H / 2 - 8)
          .attr("rx", 2).style("fill", LINE_COLOR(p && p.line));
        const yr = n.append("text").attr("class", "years").attr("x", BOX_W - 10).attr("y", y + 20).attr("text-anchor", "end").text(years(p));
        const nm = n.append("text").attr("x", 14).attr("y", y + 20).text(p ? p.name : "onbekend");
        nm.append("title").text(p ? p.name : "");
        // Shorten long names so they never run into the years
        const room = BOX_W - 24 - yr.node().getComputedTextLength() - 8;
        let full = p ? p.name : "onbekend", cut = full.length;
        while (nm.node().getComputedTextLength() > room && cut > 4) nm.text(full.slice(0, --cut) + "…");
      });
    });

    // Fit to view
    const b = g.node().getBBox(), W = svg.node().clientWidth, H = svg.node().clientHeight;
    let s = Math.min(1, 0.92 * Math.min(W / b.width, H / b.height));
    // Keep the text readable: never start smaller than 0.6 (phone) / 0.85 (desktop); start at the bottom couple
    const minS = W < 800 ? 0.6 : 0.85;
    if (s < minS) {
      s = minS;
      svg.call(zoom.transform, d3.zoomIdentity.translate(W / 2, H - 20 - s * BOX_H).scale(s));
    } else {
      svg.call(zoom.transform, d3.zoomIdentity.translate(W / 2 - s * (b.x + b.width / 2), H / 2 - s * (b.y + b.height / 2)).scale(s));
    }

    d3.select("#zin").on("click", () => svg.transition().call(zoom.scaleBy, 1.3));
    d3.select("#zout").on("click", () => svg.transition().call(zoom.scaleBy, 1 / 1.3));
  }

  function coupleOf(pid) {
    // the couple in which this person is husband or wife (for navigating from the children list)
    return Object.values(DATA.couples).find((c) => c.h === pid || c.w === pid);
  }

  function personHtml(p, role) {
    if (!p) return "";
    const d = [];
    if (p.born) d.push("geboren " + fmtDate(p.born) + (p.place ? ", " + esc(p.place) : ""));
    else if (p.place) d.push(esc(p.place));
    if (p.died) d.push("overleden " + fmtDate(p.died));
    const src = (p.sources || []).map((s) => `<a href="${s.url}" target="_blank" rel="noopener">${esc(s.label)}</a>`).join(" ");
    return `<div class="person"><span class="line-tag t-${p.line}">${role}</span><h3>${esc(p.name)}</h3>
      <div class="dates">${d.join(" · ")}</div>${p.note ? `<p>${esc(p.note)}</p>` : ""}
      ${src ? `<div class="src">Bronnen: ${src}</div>` : ""}</div>`;
  }

  function select(cid) {
    selected = cid;
    d3.selectAll("g.couple").classed("selected", (d) => d.data.id === cid);
    const c = DATA.couples[cid], h = P(c.h), w = P(c.w);
    const kids = (c.children || []).map((k) => {
      const p = P(k), sp = p.spouse && P(p.spouse), cc = coupleOf(k);
      const nav = cc && cc.id !== cid ? ` <a href="#" data-c="${cc.id}">→ gezin</a>` : "";
      return `<li><b>${esc(p.name)}</b> <span class="dates">${years(p)}</span>${sp ? ", x " + esc(sp.name) : ""}${nav}</li>`;
    }).join("");
    document.getElementById("panel").innerHTML = `
      <h2>${esc(h.name)} &amp; ${esc(w.name)}</h2>
      ${c.marr ? `<div class="dates">Getrouwd ${esc(fmtDate(c.marr.split(",")[0]))}${c.marr.includes(",") ? "," + esc(c.marr.split(",").slice(1).join(",")) : ""}</div>` : ""}
      ${personHtml(h, "man")}${personHtml(w, "vrouw")}
      ${kids ? `<div class="person"><h3>Kinderen</h3><ul>${kids}</ul></div>` : ""}`;
    document.querySelectorAll("#panel a[data-c]").forEach((a) => a.addEventListener("click", (e) => {
      e.preventDefault(); select(a.dataset.c);
    }));
  }

  fetch("data/familie.json").then((r) => r.json()).then((d) => {
    DATA = d;
    draw();
    select(d.root);
  });
})();
