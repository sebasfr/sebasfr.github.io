/* Motion layer: IntersectionObserver reveals + home page-turn class toggle.
   Gated by html.js-motion (set synchronously in <head> only when
   prefers-reduced-motion is no-preference). ES2015; no deps. */
(function () {
  "use strict";

  if (!document.documentElement.classList.contains("js-motion")) return;

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
})();
