/* RevSnap Media — site behaviour.
   Rules: GPU-only transforms, no layout thrash, and everything degrades to a
   fully readable static page when JS or motion is unavailable. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---- Nav: solid background once we leave the hero -------------------- */
  var nav = document.querySelector("[data-nav]");
  if (nav) {
    var stuck = false;
    var onScroll = function () {
      var next = window.scrollY > 24;
      if (next !== stuck) {
        stuck = next;
        nav.classList.toggle("is-stuck", stuck);
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Mobile menu ----------------------------------------------------- */
  var toggle = document.querySelector("[data-nav-toggle]");
  var menu = document.querySelector("[data-nav-menu]");
  if (toggle && menu) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("is-open", open);
      document.body.style.overflow = open ? "hidden" : "";
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
    var wideNav = window.matchMedia("(min-width: 861px)");
    var onWide = function (e) {
      if (e.matches) setOpen(false);
    };
    if (wideNav.addEventListener) wideNav.addEventListener("change", onWide);
    else if (wideNav.addListener) wideNav.addListener(onWide);
  }

  /* ---- Scroll reveals -------------------------------------------------- */
  var revealables = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) || reduceMotion.matches) {
    Array.prototype.forEach.call(revealables, function (el) {
      el.classList.add("is-in");
    });
  } else {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -12% 0px", threshold: 0.06 }
    );
    Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
  }

  /* ---- Hero parallax --------------------------------------------------- */
  /* The plate drifts at 18% of scroll speed — weight, not motion for its own
     sake. rAF-gated, transform-only, and switched off entirely below 860px
     (where it competes with mobile scroll) and under reduced-motion. */
  var plate = document.querySelector("[data-parallax]");
  if (plate) {
    var wide = window.matchMedia("(min-width: 861px)");
    var ticking = false;
    var limit = 0;

    var apply = function () {
      ticking = false;
      var y = Math.min(window.scrollY, limit) * 0.18;
      plate.style.transform = "translate3d(0," + y.toFixed(2) + "px,0)";
    };
    var request = function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(apply);
      }
    };
    var measure = function () {
      limit = plate.parentElement ? plate.parentElement.offsetHeight : 0;
    };
    var enable = function () {
      window.removeEventListener("scroll", request);
      if (reduceMotion.matches || !wide.matches) {
        plate.style.transform = "";
        return;
      }
      measure();
      window.addEventListener("scroll", request, { passive: true });
      apply();
    };

    enable();
    window.addEventListener("resize", function () { measure(); enable(); }, { passive: true });
    if (reduceMotion.addEventListener) reduceMotion.addEventListener("change", enable);
  }

  /* ---- Current year + stamped contact --------------------------------- */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  var siteEmail = (window.SITE && SITE.email) || "";
  if (siteEmail) {
    Array.prototype.forEach.call(document.querySelectorAll("[data-email]"), function (el) {
      el.setAttribute("href", "mailto:" + siteEmail);
      if (el.childNodes.length === 1 && el.textContent.indexOf("@") !== -1) {
        el.textContent = siteEmail;
      }
    });
  }

  /* GitHub Pages / local preview have no Netlify Forms sink. Don't fake a
     successful booking — fall back to mailto so the message still reaches Clark. */
  var formHost = window.location.hostname;
  var formsLive = formHost === "revsnapmedia.com" ||
    formHost === "www.revsnapmedia.com" ||
    /\.netlify\.app$/.test(formHost);
  if (!formsLive) {
    Array.prototype.forEach.call(document.querySelectorAll("form[data-netlify]"), function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = siteEmail || "revsnapmedia@gmail.com";
        var subjectEl = form.querySelector("[name=_subject]");
        var subject = (subjectEl && subjectEl.value) || "RevSnap Media inquiry";
        var parts = [];
        Array.prototype.forEach.call(form.elements, function (el) {
          if (!el.name || el.disabled) return;
          if (el.name === "bot-field" || el.name === "form-name" || el.name === "_subject") return;
          if (el.type === "submit" || el.type === "button") return;
          var value = (el.value || "").trim();
          if (!value) return;
          parts.push(el.name + ": " + value);
        });
        window.location.href = "mailto:" + email +
          "?subject=" + encodeURIComponent(subject) +
          "&body=" + encodeURIComponent(parts.join("\n"));
      });
    });
  }

  /* ---- Portfolio sub-filters (Cars: Exotics / Builds / Events) --------- */
  Array.prototype.forEach.call(document.querySelectorAll(".filter-bar"), function (bar) {
    var grid = document.getElementById(bar.getAttribute("data-filter-for"));
    if (!grid) return;
    var buttons = bar.querySelectorAll(".filter-btn");
    var tiles = grid.querySelectorAll(".m-tile");
    var empty = grid.parentElement.querySelector(".portfolio-empty");

    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener("click", function () {
        var value = btn.getAttribute("data-value");
        Array.prototype.forEach.call(buttons, function (b) {
          b.setAttribute("aria-pressed", String(b === btn));
        });
        var anyVisible = false;
        Array.prototype.forEach.call(tiles, function (tile) {
          var match = value === "all" || tile.getAttribute("data-subcat") === value;
          tile.classList.toggle("is-filtered-out", !match);
          if (match) anyVisible = true;
        });
        if (empty) empty.style.display = anyVisible ? "none" : "block";
      });
    });
  });

  /* ---- Lightbox ---------------------------------------------------------
     Keyboard-accessible: focus trap while open, Escape closes, Left/Right
     move within the triggering gallery's currently-visible tiles, and focus
     returns to the thumbnail that opened it. */
  var lb = document.getElementById("lightbox");
  if (lb) {
    var stage = lb.querySelector("[data-lightbox-stage]");
    var closeBtn = lb.querySelector("[data-lightbox-close]");
    var prevBtn = lb.querySelector("[data-lightbox-prev]");
    var nextBtn = lb.querySelector("[data-lightbox-next]");
    var capEl = lb.querySelector("[data-lightbox-cap]");
    var avifSourceEl = lb.querySelector("[data-lightbox-source-avif]");
    var webpSourceEl = lb.querySelector("[data-lightbox-source-webp]");
    var imgEl = lb.querySelector("[data-lightbox-img] img");
    var sizes = [400, 800, 1200, 1600];

    var lastFocused = null;
    var currentList = [];
    var currentIndex = -1;

    function srcset(base, ext) {
      return sizes.map(function (w) { return base + "-" + w + "." + ext + " " + w + "w"; }).join(", ");
    }

    function render(trigger) {
      var base = trigger.getAttribute("data-src");
      var alt = trigger.getAttribute("data-alt") || "";
      avifSourceEl.setAttribute("srcset", srcset(base, "avif"));
      webpSourceEl.setAttribute("srcset", srcset(base, "webp"));
      imgEl.setAttribute("srcset", srcset(base, "jpg"));
      imgEl.src = base + "-1600.jpg";
      imgEl.alt = alt;
      imgEl.width = trigger.getAttribute("data-w");
      imgEl.height = trigger.getAttribute("data-h");
      capEl.textContent = trigger.getAttribute("data-cap") || "";
    }

    function openLightbox(trigger) {
      var group = trigger.closest("[data-lightbox-group]");
      var scoped = group ? group.querySelectorAll(".m-tile") : [trigger];
      currentList = Array.prototype.filter.call(scoped, function (t) {
        return !t.classList.contains("is-filtered-out");
      });
      currentIndex = currentList.indexOf(trigger);
      lastFocused = trigger;
      render(trigger);
      lb.classList.add("is-open");
      lb.setAttribute("aria-hidden", "false");
      document.body.classList.add("lightbox-open");
      document.addEventListener("keydown", onKeydown);
      closeBtn.focus();
    }

    function closeLightbox() {
      lb.classList.remove("is-open");
      lb.setAttribute("aria-hidden", "true");
      document.body.classList.remove("lightbox-open");
      document.removeEventListener("keydown", onKeydown);
      if (lastFocused) lastFocused.focus();
    }

    function step(delta) {
      if (currentList.length < 2) return;
      currentIndex = (currentIndex + delta + currentList.length) % currentList.length;
      render(currentList[currentIndex]);
    }

    function onKeydown(e) {
      if (e.key === "Escape") { closeLightbox(); return; }
      if (e.key === "ArrowRight") { step(1); return; }
      if (e.key === "ArrowLeft") { step(-1); return; }
      if (e.key === "Tab") {
        var focusables = lb.querySelectorAll("button");
        var first = focusables[0], last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault(); last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault(); first.focus();
        }
      }
    }

    Array.prototype.forEach.call(document.querySelectorAll(".m-tile"), function (trigger) {
      trigger.addEventListener("click", function () { openLightbox(trigger); });
    });

    closeBtn.addEventListener("click", closeLightbox);
    prevBtn.addEventListener("click", function () { step(-1); });
    nextBtn.addEventListener("click", function () { step(1); });
    stage.addEventListener("click", function (e) {
      if (e.target === stage) closeLightbox();
    });
  }
})();
