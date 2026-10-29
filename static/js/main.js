/* Bhuvaneshwari M — portfolio interactions. No dependencies. */
(() => {
  "use strict";

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- theme (dark by default) ---------- */
  const root = document.documentElement;
  $("#themebtn")?.addEventListener("click", () => {
    const next = root.dataset.theme === "light" ? "dark" : "light";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
  });

  /* ---------- header: solid on scroll, progress bar ---------- */
  const header = $(".header");
  const bar = $("#progress");
  const onScroll = () => {
    header?.classList.toggle("is-scrolled", scrollY > 40);
    const max = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  const navToggle = $(".navtoggle");
  const navList = $("#navlist");
  const setMenu = (open) => {
    navToggle?.setAttribute("aria-expanded", open);
    navToggle?.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    navList?.classList.toggle("is-open", open);
    header?.classList.toggle("is-scrolled", open || scrollY > 40);
  };
  navToggle?.addEventListener("click", () => setMenu(navToggle.getAttribute("aria-expanded") !== "true"));
  $$("#navlist a").forEach((a) => a.addEventListener("click", () => setMenu(false)));

  /* ---------- active nav link ---------- */
  const navLinks = $$("[data-nav]");
  const sectionObs = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) navLinks.forEach((a) => a.classList.toggle("is-active", a.dataset.nav === e.target.id));
    }),
    { rootMargin: "-45% 0px -50% 0px" }
  );
  navLinks.forEach((a) => {
    const sec = document.getElementById(a.dataset.nav);
    if (sec) sectionObs.observe(sec);
  });

  /* ---------- reveal on scroll ---------- */
  const revealObs = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-in");
      revealObs.unobserve(e.target);
    }),
    { threshold: 0.1 }
  );
  $$(".reveal").forEach((el) => revealObs.observe(el));

  /* ---------- count-up stats ---------- */
  const countObs = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = +el.dataset.count;
      countObs.unobserve(el);
      if (reduced) return;
      const t0 = performance.now();
      const step = (t) => {
        const p = Math.min(1, (t - t0) / 1400);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }),
    { threshold: 0.6 }
  );
  $$("[data-count]").forEach((el) => countObs.observe(el));

  /* ---------- typed role titles ---------- */
  const typed = $("#typed");
  if (typed && !reduced) {
    const roles = JSON.parse(typed.dataset.roles || "[]");
    let r = 0, i = roles[0]?.length || 0, deleting = true;
    const tick = () => {
      const word = roles[r];
      i += deleting ? -1 : 1;
      typed.textContent = word.slice(0, i);
      let wait = deleting ? 40 : 80;
      if (!deleting && i === word.length) { deleting = true; wait = 2200; }
      else if (deleting && i === 0) { deleting = false; r = (r + 1) % roles.length; wait = 300; }
      setTimeout(tick, wait);
    };
    setTimeout(tick, 2600);
  }

  /* ---------- skill filter tabs ---------- */
  const tabs = $$(".tab");
  const tiles = $$(".tile");
  tabs.forEach((tab) =>
    tab.addEventListener("click", () => {
      const g = tab.dataset.group;
      tabs.forEach((t) => {
        t.classList.toggle("is-on", t === tab);
        t.setAttribute("aria-selected", t === tab);
      });
      tiles.forEach((tile) => {
        tile.classList.toggle("is-hidden", g !== "*" && tile.dataset.group !== g);
        tile.classList.add("is-in");
      });
    })
  );

  /* ---------- project dialogs + gallery ---------- */
  $$("[data-open]").forEach((btn) =>
    btn.addEventListener("click", () => {
      const dlg = document.getElementById(btn.dataset.open);
      if (!dlg) return;
      dlg.showModal();
      document.body.classList.add("has-dlg");
    })
  );

  $$(".dlg").forEach((dlg) => {
    dlg.addEventListener("close", () => document.body.classList.remove("has-dlg"));
    dlg.addEventListener("click", (e) => {
      if (e.target === dlg || e.target.closest("[data-close]")) dlg.close();
    });

    const main = $("[data-main]", dlg);
    const thumbs = $$(".gallery__thumbs button", dlg);
    const counter = $("[data-counter]", dlg);
    if (!main || thumbs.length < 2) return;
    let cur = 0;
    const show = (n) => {
      cur = (n + thumbs.length) % thumbs.length;
      main.src = thumbs[cur].dataset.src;
      thumbs.forEach((b, j) => b.classList.toggle("is-on", j === cur));
      thumbs[cur].scrollIntoView({ block: "nearest", inline: "nearest", behavior: reduced ? "auto" : "smooth" });
      if (counter) counter.textContent = `${cur + 1} / ${thumbs.length}`;
    };
    thumbs.forEach((b, j) => b.addEventListener("click", () => show(j)));
    $$("[data-step]", dlg).forEach((b) => b.addEventListener("click", () => show(cur + +b.dataset.step)));
    dlg.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") show(cur + 1);
      if (e.key === "ArrowLeft") show(cur - 1);
    });
  });

  /* ---------- copy email ---------- */
  $$("[data-copy]").forEach((btn) =>
    btn.addEventListener("click", async () => {
      const ok = $("[data-copied]", btn.parentElement);
      try {
        await navigator.clipboard.writeText(btn.dataset.copy);
        if (ok) { ok.hidden = false; setTimeout(() => (ok.hidden = true), 1800); }
      } catch (e) {
        location.href = `mailto:${btn.dataset.copy}`;
      }
    })
  );
})();
