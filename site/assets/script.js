// Tema (claro/escuro) com persistência
(function () {
  var root = document.documentElement;
  var saved = localStorage.getItem("tema");
  if (saved) root.setAttribute("data-theme", saved);
  else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches)
    root.setAttribute("data-theme", "dark");

  function syncIcon() {
    var btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = root.getAttribute("data-theme") === "dark" ? "☀️" : "🌙";
  }
  document.addEventListener("click", function (ev) {
    if (ev.target && ev.target.id === "theme-toggle") {
      var dark = root.getAttribute("data-theme") === "dark";
      root.setAttribute("data-theme", dark ? "light" : "dark");
      localStorage.setItem("tema", dark ? "light" : "dark");
      syncIcon();
    }
  });
  syncIcon();
})();

// Busca de disciplinas na home
(function () {
  var input = document.getElementById("search");
  if (!input) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll(".card"));
  var empty = document.getElementById("no-results");
  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (c) {
      var hit = c.getAttribute("data-name").indexOf(q) !== -1;
      c.style.display = hit ? "" : "none";
      if (hit) shown++;
    });
    document.querySelectorAll(".group").forEach(function (g) {
      var any = g.querySelector('.card:not([style*="display: none"])');
      g.style.display = any ? "" : "none";
    });
    if (empty) empty.hidden = shown !== 0;
  });
})();

// Destaque do item ativo no índice lateral
(function () {
  var links = document.querySelectorAll(".toc nav a");
  if (!links.length) return;
  var sections = Array.prototype.slice.call(document.querySelectorAll(".topico"));
  var map = {};
  links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        links.forEach(function (l) { l.classList.remove("active"); });
        var a = map[en.target.id];
        if (a) a.classList.add("active");
      }
    });
  }, { rootMargin: "-30% 0px -60% 0px" });
  sections.forEach(function (s) { obs.observe(s); });
})();
