/* Motion layer: IntersectionObserver reveals + home page-turn class toggle
   + hero wordmark letter-mask & axis-morph setup.
   Gated by html.js-motion (set synchronously in <head> only when
   prefers-reduced-motion is no-preference). ES2015; no deps. */
(function () {
  "use strict";

  if (!document.documentElement.classList.contains("js-motion")) return;

  function supportsFvsAnimation() {
    if (!window.CSS || typeof window.CSS.supports !== "function") return false;
    var ua = navigator.userAgent || "";
    var isSafari = /^((?!chrome|android).)*safari/i.test(ua);
    return CSS.supports("font-variation-settings", '"WONK" 1') && !isSafari;
  }

  function splitLetters(el) {
    if (!el || el.dataset.splitDone === "1") return;
    var filter = {
      acceptNode: function (textNode) {
        // Whitespace-only text nodes are structural (indentation between
        // sibling elements). Wrapping them in inline-block spans stops
        // whitespace collapse and introduces line-box gaps inside the h1.
        if (!/\S/.test(textNode.nodeValue)) return NodeFilter.FILTER_REJECT;
        // Skip any text inside an .anim-axis-morph — that element needs its
        // text intact so font-variation-settings can animate the whole word.
        var p = textNode.parentNode;
        while (p && p !== el) {
          if (p.classList && p.classList.contains("anim-axis-morph")) {
            return NodeFilter.FILTER_REJECT;
          }
          p = p.parentNode;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    };
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, filter, false);
    var textNodes = [];
    var node;
    while ((node = walker.nextNode())) textNodes.push(node);

    var counter = 0;
    for (var i = 0; i < textNodes.length; i++) {
      var textNode = textNodes[i];
      var chars = Array.from(textNode.nodeValue);
      if (chars.length === 0) continue;
      var frag = document.createDocumentFragment();
      for (var j = 0; j < chars.length; j++) {
        var ch = chars[j];
        var span = document.createElement("span");
        span.className = "anim-char" + (/\s/.test(ch) ? " is-space" : "");
        span.setAttribute("aria-hidden", "true");
        span.style.setProperty("--i", counter++);
        span.textContent = ch;
        frag.appendChild(span);
      }
      textNode.parentNode.replaceChild(frag, textNode);
    }
    el.dataset.splitDone = "1";
  }

  // 1. Reveal-on-scroll for elements with .reveal-on-scroll class.
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            entries[i].target.classList.add("is-visible");
            io.unobserve(entries[i].target);
          }
        }
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.1 }
    );
    var reveals = document.querySelectorAll(".reveal-on-scroll");
    for (var j = 0; j < reveals.length; j++) io.observe(reveals[j]);
  } else {
    // Graceful fallback: reveal everything.
    var fallback = document.querySelectorAll(".reveal-on-scroll");
    for (var k = 0; k < fallback.length; k++) fallback[k].classList.add("is-visible");
  }

  // 2. Page-turn on home — add .page-turn--enter to <main> of body.home
  //    so the initial clip-path reveal animates in.
  if (document.body.classList.contains("home")) {
    var main = document.querySelector("main");
    if (main) main.classList.add("page-turn--enter");
  }

  // 3. Hero wordmark: split glyphs for letter-mask, feature-gate axis morph.
  if (supportsFvsAnimation()) {
    var axisTargets = document.querySelectorAll(".anim-axis-morph");
    for (var a = 0; a < axisTargets.length; a++) {
      axisTargets[a].setAttribute("data-fvs-ok", "1");
    }
  }

  var letterTargets = document.querySelectorAll(".anim-letter-mask");
  for (var l = 0; l < letterTargets.length; l++) splitLetters(letterTargets[l]);
})();
