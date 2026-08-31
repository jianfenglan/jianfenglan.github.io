document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('news-modal');
  const modalContent = modal && modal.querySelector('.modal-content');
  const closeButton = modal && modal.querySelector('.close-button');
  const cards = document.querySelectorAll('.news-list .news-card');

  if (!modal || !modalContent) return;

  function openModal(card) {
    const titleNode = card.querySelector('.news-content h3');
    const metaNode = card.querySelector('.news-meta');
    const cardImage = card.querySelector('.news-image img');
    const title = titleNode ? titleNode.textContent.trim() : '';
    const meta = metaNode ? metaNode.textContent.trim() : '';
    const content = card.getAttribute('data-content') || '';

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

    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('show');
    document.body.style.overflow = '';
  }

  cards.forEach(function (card) {
    card.addEventListener('click', function () {
      openModal(card);
    });
  });

  if (closeButton) {
    closeButton.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', function (event) {
    if (event.target === modal) closeModal();
  });

  modalContent.addEventListener('click', function (event) {
    event.stopPropagation();
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && modal.classList.contains('show')) {
      closeModal();
    }
  });
});
