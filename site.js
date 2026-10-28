// Shared by every page (English and French).

// Assemble the email address at runtime to keep it away from simple scrapers.
(function () {
  var addr = ['heightcube', 'website'].join('+') + '@' + ['gmail', 'com'].join('.');
  document.querySelectorAll('[data-mail]').forEach(function (a) {
    a.href = 'mailto:' + addr;
    if (a.hasAttribute('data-mail-text')) a.textContent = addr;
  });
})();

// Barnsley fern, colored from the CSS palette. Grows in gently unless reduced motion is set.
(function () {
  var canvas = document.getElementById('fern');
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext('2d');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)');
  var dark = matchMedia('(prefers-color-scheme: dark)');
  var TOTAL = 90000, STEP = 1500, frame = 0, width = 0;

  function rgb(name) {
    var h = getComputedStyle(document.documentElement).getPropertyValue(name).trim().slice(1);
    return [0, 2, 4].map(function (i) { return parseInt(h.substr(i, 2), 16); });
  }

  function draw() {
    cancelAnimationFrame(frame);
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = canvas.width = Math.round(canvas.clientWidth * dpr);
    var h = canvas.height = Math.round(canvas.clientHeight * dpr);
    width = canvas.clientWidth;
    var img = ctx.createImageData(w, h), px = img.data;
    var a = rgb('--fern-a'), b = rgb('--fern-b');
    var scale = Math.min(w / 6, h / 11.2), ox = w / 2 - 0.24 * scale, oy = h - 0.6 * scale;
    var x = 0, y = 0, n = 0;

    function plot(count) {
      for (var i = 0; i < count; i++) {
        var r = Math.random(), nx;
        if (r < 0.01) { nx = 0; y = 0.16 * y; }
        else if (r < 0.86) { nx = 0.85 * x + 0.04 * y; y = -0.04 * x + 0.85 * y + 1.6; }
        else if (r < 0.93) { nx = 0.2 * x - 0.26 * y; y = 0.23 * x + 0.22 * y + 1.6; }
        else { nx = -0.15 * x + 0.28 * y; y = 0.26 * x + 0.24 * y + 0.44; }
        x = nx;
        var px_ = Math.round(ox + x * scale), py = Math.round(oy - y * scale);
        if (px_ < 0 || py < 0 || px_ >= w || py >= h) continue;
        var t = y / 10, k = (py * w + px_) * 4;
        px[k] = a[0] + (b[0] - a[0]) * t;
        px[k + 1] = a[1] + (b[1] - a[1]) * t;
        px[k + 2] = a[2] + (b[2] - a[2]) * t;
        px[k + 3] = 255;
      }
      n += count;
      ctx.putImageData(img, 0, 0);
    }

    if (reduce.matches) { plot(TOTAL); return; }
    (function grow() {
      plot(STEP);
      if (n < TOTAL) frame = requestAnimationFrame(grow);
    })();
  }

  draw();
  var timer;
  window.addEventListener('resize', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { if (canvas.clientWidth !== width) draw(); }, 200);
  });
  dark.addEventListener('change', draw);
})();
