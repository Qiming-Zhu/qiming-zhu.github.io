'use strict';
document.querySelectorAll('[data-language-link]').forEach(link => {
  link.addEventListener('click', () => {
    try { localStorage.setItem('qiming-language', link.dataset.languageLink); } catch (_) {}
  });
});
const viewer = document.getElementById('image-viewer');
if (viewer && typeof viewer.showModal === 'function') {
  let returnFocus;
  document.querySelectorAll('[data-lightbox]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      returnFocus = link;
      const image = link.querySelector('img');
      viewer.querySelector('img').src = link.href;
      const caption = link.dataset.figureCaption || image.alt;
      viewer.querySelector('img').alt = caption;
      viewer.querySelector('p').textContent = caption;
      viewer.showModal();
      document.body.classList.add('viewer-open');
    });
  });
  const close = () => viewer.close();
  viewer.querySelector('button').addEventListener('click', close);
  viewer.addEventListener('click', event => { if (event.target === viewer) close(); });
  viewer.addEventListener('close', () => {
    document.body.classList.remove('viewer-open');
    returnFocus?.focus({ preventScroll: true });
  });
}
