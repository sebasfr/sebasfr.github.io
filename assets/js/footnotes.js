/* Marginal footnotes. On >=900px, clones each canonical footnote into an
   <aside class="margin-note" role="doc-footnote"> inside .post-margin and
   aligns it vertically with the sup ref. All ids/hrefs on the clones are
   stripped to avoid duplicate-id a11y violations. On desktop the canonical
   .footnotes list is `display: none` via CSS, so these margin clones ARE the
   canonical footnotes for both sighted and AT users. On mobile the script
   no-ops and the inline canonical list is shown as usual.
   ES2015; no deps. */
(function () {
  "use strict";

  var MQ = window.matchMedia("(min-width: 900px)");
  var post = document.querySelector(".post-body");
  var margin = document.querySelector(".post-margin");
  if (!post || !margin) return;

  var footnotes = post.querySelector(".footnotes");
  if (!footnotes) return;
  var items = footnotes.querySelectorAll("ol > li");
  if (!items.length) return;

  function buildMarginNote(index, li, ref) {
    var aside = document.createElement("aside");
    aside.className = "margin-note";
    aside.setAttribute("role", "doc-footnote");

    var idx = document.createElement("span");
    idx.className = "margin-note-index";
    idx.textContent = String(index) + ".";
    aside.appendChild(idx);

    // Clone the li's children, strip ids/hrefs on anything cloned.
    var body = document.createElement("div");
    body.className = "margin-note-body";
    var children = li.cloneNode(true);
    var strip = children.querySelectorAll("[id]");
    for (var i = 0; i < strip.length; i++) strip[i].removeAttribute("id");
    var links = children.querySelectorAll("a[href^='#']");
    for (var j = 0; j < links.length; j++) {
      // remove the backlink arrow entirely
      if (links[j].classList.contains("reversefootnote")) {
        links[j].parentNode && links[j].parentNode.removeChild(links[j]);
      } else {
        links[j].removeAttribute("href");
      }
    }
    // Move cloned children into body
    while (children.firstChild) body.appendChild(children.firstChild);
    aside.appendChild(body);
    return aside;
  }

  var asides = [];

  function build() {
    // clear previous
    while (margin.firstChild) margin.removeChild(margin.firstChild);
    asides = [];
    var refs = {};
    var seen = {};

    for (var i = 0; i < items.length; i++) {
      var li = items[i];
      var id = li.id || "";
      var refId = id ? id.replace("fn:", "fnref:") : null;
      if (!refId || seen[id]) continue;
      seen[id] = true;
      var ref = document.getElementById(refId);
      if (!ref) continue;
      refs[id] = ref;
      var aside = buildMarginNote(i + 1, li, ref);
      margin.appendChild(aside);
      asides.push({ ref: ref, el: aside });
    }
    position();
  }

  function position() {
    if (!asides.length) return;
    var postRect = post.getBoundingClientRect();
    var taken = 0;
    for (var i = 0; i < asides.length; i++) {
      var a = asides[i];
      var refRect = a.ref.getBoundingClientRect();
      var top = refRect.top - postRect.top;
      if (top < taken) top = taken;
      a.el.style.top = top + "px";
      taken = top + a.el.offsetHeight + 16;
    }
  }

  function enable() {
    build();
    window.addEventListener("resize", onResize);
    window.addEventListener("load", position);
  }

  function disable() {
    window.removeEventListener("resize", onResize);
    while (margin.firstChild) margin.removeChild(margin.firstChild);
    asides = [];
  }

  var rafId = null;
  function onResize() {
    if (rafId) cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(position);
  }

  if (MQ.matches) enable();

  MQ.addEventListener
    ? MQ.addEventListener("change", function (e) { e.matches ? enable() : disable(); })
    : MQ.addListener(function (e) { e.matches ? enable() : disable(); });
})();
