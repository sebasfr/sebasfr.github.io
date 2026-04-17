/* Mobile drawer: open/close with focus trap, ESC close, ARIA toggles.
   Targets the <aside id="mobile-drawer"> and <button id="drawer-toggle"> pair
   created in _includes/mobile_drawer.liquid. ES2015; no deps. */
(function () {
  "use strict";

  var toggle = document.getElementById("drawer-toggle");
  var close = document.getElementById("drawer-close");
  var drawer = document.getElementById("mobile-drawer");
  if (!toggle || !drawer) return;

  var lastFocus = null;
  var focusableSelector =
    "a[href], button:not([disabled]), [tabindex]:not([tabindex='-1'])";

  function getFocusable() {
    return Array.prototype.slice.call(drawer.querySelectorAll(focusableSelector));
  }

  function openDrawer() {
    lastFocus = document.activeElement;
    drawer.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
    document.documentElement.classList.add("drawer-open");
    var f = getFocusable();
    if (f.length) f[0].focus();
    document.addEventListener("keydown", onKey);
  }

  function closeDrawer() {
    drawer.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    document.documentElement.classList.remove("drawer-open");
    document.removeEventListener("keydown", onKey);
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  }

  function onKey(e) {
    if (e.key === "Escape") {
      e.preventDefault();
      closeDrawer();
      return;
    }
    if (e.key !== "Tab") return;
    var f = getFocusable();
    if (!f.length) return;
    var first = f[0];
    var last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  toggle.addEventListener("click", function () {
    if (drawer.hidden) openDrawer();
    else closeDrawer();
  });
  if (close) close.addEventListener("click", closeDrawer);

  // Close when a drawer link is clicked (single-page nav flow).
  drawer.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (a) closeDrawer();
  });
})();
