/* Theme control: light or dark, nothing else.

   The stored choice, or the system preference when there is none, is
   applied by a short inline script in <head>, so the page never paints in
   the wrong theme and the button never shows the wrong glyph. This file
   only handles the click. */

(function () {
  var btn = document.querySelector('[data-theme-toggle]');
  if (!btn) return;

  var KEY = 'aiml-theme';
  var root = document.documentElement;

  function other() {
    return root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  }

  function render() {
    // The icon shows the theme you are in; the label says what a click does.
    var label = 'Switch to ' + other() + ' theme';
    btn.setAttribute('title', label);
    btn.setAttribute('aria-label', label);
  }

  btn.addEventListener('click', function () {
    var next = other();
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
    render();
  });

  render();
})();
