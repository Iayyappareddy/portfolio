/* script.js — Ayyappa Reddy Portfolio (theme toggle + mobile menu) */
document.addEventListener('DOMContentLoaded', function () {
const root = document.documentElement;
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  root.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
  document.getElementById('themeToggle').addEventListener('click', () => {
    const current = root.getAttribute('data-theme');
    root.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
  });

  const mobileMenu = document.getElementById('mobileMenu');
  document.getElementById('menuToggle').addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => mobileMenu.classList.remove('open'));
  });
});
