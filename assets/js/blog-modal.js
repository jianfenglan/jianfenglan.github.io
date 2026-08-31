function openModal(card) {
  const title = card.getAttribute('data-title') || '';
  const meta = card.getAttribute('data-meta') || '';
  const content = card.getAttribute('data-content') || '';
  const cardImage = card.querySelector('.news-image img');

  document.getElementById('modal-title').innerText = title;
  document.getElementById('modal-meta').innerText = meta;
  document.getElementById('modal-body').innerHTML = content;

  const modalImageWrap = document.getElementById('modal-image-wrap');
  const modalImage = document.getElementById('modal-image');

  if (cardImage && cardImage.getAttribute('src')) {
    modalImage.src = cardImage.src;
    modalImage.alt = cardImage.alt || title;
    modalImageWrap.style.display = 'block';
  } else {
    modalImage.removeAttribute('src');
    modalImage.alt = '';
    modalImageWrap.style.display = 'none';
  }

  const modal = document.getElementById('news-modal');
  modal.classList.add('show');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('news-modal').classList.remove('show');
  document.body.style.overflow = '';
}

document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('news-modal');
  const modalContent = document.querySelector('.modal-content');

  if (!modal || !modalContent) return;

  modal.addEventListener('click', function (event) {
    if (event.target === this) closeModal();
  });

  modalContent.addEventListener('click', function (event) {
    event.stopPropagation();
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeModal();
  });
});
