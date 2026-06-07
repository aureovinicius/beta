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

// Expandir/recolher box de grupo (cargos) na landing
(function () {
  document.addEventListener("click", function (ev) {
    var head = ev.target.closest ? ev.target.closest(".grupo-head") : null;
    if (!head) return;
    var box = head.parentElement.querySelector(".grupo-cargos");
    var aberto = head.getAttribute("aria-expanded") === "true";
    head.setAttribute("aria-expanded", aberto ? "false" : "true");
    if (box) box.hidden = aberto;
  });
})();

// Busca de concursos na landing (filtra cards, boxes de grupo e cargos)
(function () {
  var input = document.getElementById("busca-concursos");
  if (!input) return;
  var grid = document.querySelector(".concurso-grid");
  var empty = document.getElementById("sem-concursos");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(":scope > .concurso-card"));
  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (card) {
      var grupo = card.classList.contains("grupo-card");
      var matchSelf = (card.getAttribute("data-search") || "").indexOf(q) !== -1;
      var matchCargo = false;
      if (grupo) {
        Array.prototype.slice.call(card.querySelectorAll(".cargo-card")).forEach(function (cc) {
          var hit = !q || (cc.getAttribute("data-search") || "").indexOf(q) !== -1;
          cc.style.display = hit ? "" : "none";
          if (hit) matchCargo = true;
        });
      }
      var visible = !q || matchSelf || matchCargo;
      card.style.display = visible ? "" : "none";
      if (visible) shown++;
      if (grupo) {
        var head = card.querySelector(".grupo-head");
        var box = card.querySelector(".grupo-cargos");
        var abrir = !!q && visible;
        if (head) head.setAttribute("aria-expanded", abrir ? "true" : "false");
        if (box) box.hidden = !abrir;
      }
    });
    if (empty) empty.hidden = shown !== 0;
  });
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
