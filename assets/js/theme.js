/* Theme control: auto (follow the system), light, dark.
   The stored value is applied by a short inline script in <head> so the
   page never paints in the wrong theme first. This file only wires the
   button. */

(function () {
  var btn = document.querySelector('[data-theme-toggle]');
  if (!btn) return;

  var KEY = 'aiml-theme';
  var ORDER = ['auto', 'light', 'dark'];
  var root = document.documentElement;

  function current() {
    var t = root.getAttribute('data-theme');
    return t === 'light' || t === 'dark' ? t : 'auto';
  }

  function render() {
    var mode = current();
    // The glyph is set from this attribute in CSS. The label is the only
    // thing a screen reader gets, since the button carries no text.
    btn.setAttribute('data-mode', mode);
    btn.setAttribute('title', 'Colour theme: ' + mode);
    btn.setAttribute(
      'aria-label',
      'Colour theme: ' + mode + '. Activate to change.'
    );
  }

  btn.addEventListener('click', function () {
    var next = ORDER[(ORDER.indexOf(current()) + 1) % ORDER.length];
    if (next === 'auto') {
      root.removeAttribute('data-theme');
      try { localStorage.removeItem(KEY); } catch (e) {}
    } else {
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    }
    render();
  });

  render();
})();
