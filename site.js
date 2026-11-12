// Shared by every page (English, French, and the German privacy page).

// Assemble the email address at runtime to keep it away from simple scrapers.
(function () {
  var addr = ['heightcube', 'website'].join('+') + '@' + ['gmail', 'com'].join('.');
  document.querySelectorAll('[data-mail]').forEach(function (a) {
    a.href = 'mailto:' + addr;
    if (a.hasAttribute('data-mail-text')) a.textContent = addr;
  });
})();
