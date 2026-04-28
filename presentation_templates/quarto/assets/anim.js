/* SFR slide animations — letter-mask, axis-morph, clip-reveal, fade-rise,
   content-sweep, stamp. Mirrors the website's _animations.scss vocabulary
   and re-fires animations on slide change. */
(function () {
  document.documentElement.classList.add('js-motion');

  // Detect Fraunces variation-axis support (Safari guard, see _animations.scss).
  try {
    if (CSS && CSS.supports && CSS.supports('font-variation-settings', '"opsz" 144, "SOFT" 100, "WONK" 1')) {
      document.querySelectorAll('.anim-axis-morph').forEach(el => el.setAttribute('data-fvs-ok', '1'));
    }
  } catch (e) { /* noop */ }

  // Split text inside .anim-letter-mask into per-character spans with --i index.
  function splitLetters(root) {
    root.querySelectorAll('.anim-letter-mask').forEach(host => {
      if (host.dataset.splitDone) return;
      host.dataset.splitDone = '1';
      // Walk text nodes recursively so nested .hero-wordmark-first/.last keep structure.
      const walk = (node, counter) => {
        Array.from(node.childNodes).forEach(child => {
          if (child.nodeType === Node.TEXT_NODE) {
            const frag = document.createDocumentFragment();
            for (const ch of child.nodeValue) {
              const span = document.createElement('span');
              span.className = 'anim-char' + (ch === ' ' ? ' is-space' : '');
              span.style.setProperty('--i', counter.i++);
              span.textContent = ch;
              frag.appendChild(span);
            }
            child.parentNode.replaceChild(frag, child);
          } else if (child.nodeType === Node.ELEMENT_NODE) {
            walk(child, counter);
          }
        });
      };
      walk(host, { i: 0 });
    });
  }

  // Re-trigger CSS animations on a slide by removing+reinserting nodes.
  const ANIM_SELECTOR = [
    '.anim-letter-mask', '.anim-axis-morph', '.anim-clip-reveal',
    '.anim-fade-rise', '.anim-content-sweep', '.anim-stamp'
  ].join(',');

  function retrigger(slide) {
    if (!slide) return;
    slide.querySelectorAll(ANIM_SELECTOR).forEach(el => {
      // Force reflow to restart CSS animations.
      const animsBackup = el.style.animation;
      el.style.animation = 'none';
      // Read offsetHeight to flush.
      // eslint-disable-next-line no-unused-expressions
      void el.offsetHeight;
      el.style.animation = animsBackup;
    });
  }

  // Initial split + first-slide animation on Reveal ready.
  if (window.Reveal) {
    Reveal.on('ready', e => {
      splitLetters(document);
      retrigger(e.currentSlide);
    });
    Reveal.on('slidechanged', e => {
      // Slides not yet visited may still need splitting (Quarto loads all up-front,
      // so this is mostly a safety net).
      splitLetters(e.currentSlide);
      retrigger(e.currentSlide);
    });
  } else {
    document.addEventListener('DOMContentLoaded', () => splitLetters(document));
  }
})();
