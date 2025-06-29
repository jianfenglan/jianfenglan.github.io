---
title: ""
permalink: /articles/
author_profile: true
---

<style>
.page__inner-wrap {
    max-width: 1600px !important;
}

.publication-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    counter-reset: pub-counter;
    margin-top: 1rem;
}

.publication-card {
    display: flex;
    align-items: flex-start;
    gap: 1em;
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    line-height: 1.6;
    cursor: pointer;
}

.publication-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}

.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 600;
    font-size: 1.1em;
    color: #888;
    min-width: 2em;
    text-align: right;
}

.publication-thumb {
    width: 100px;
    height: 100px;
    border-radius: 12px;
    object-fit: cover;
    flex-shrink: 0;
}

.publication-content {
    flex: 1;
}

.my-name {
    color: #002FA7;
    font-weight: 700;
}

.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    inset: 0;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(6px);
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: #fff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    max-width: 600px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
}

.modal-overlay.show .modal-content {
    transform: scale(1);
}

.close-button {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    cursor: pointer;
    color: #666;
}
</style>

<h2>📵 Journal Articles</h2>
<div class="publication-list">
  <div class="publication-card" data-detail="test 📄️ 读阅原文: https://journals.sagepub.com/doi/10.1177/27523543251334157">
    <img src="/images/Nara.jpg" alt="cover image" class="publication-thumb">
    <div class="publication-content">
      <span class="my-name">Lan, J.</span>, Huang, Y. (2025).<br>
      Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.<br>
      <em>Emerging Media</em>, Online first.
    </div>
  </div>
  <div class="publication-card" data-detail="test 📄️ 读阅原文: https://journals.sagepub.com/doi/abs/10.1177/14614448231212822">
    <img src="/images/Nara.jpg" alt="cover image" class="publication-thumb">
    <div class="publication-content">
      Mou, Y.*, <span class="my-name">Lan, J.</span>*, & Huang, Y. (2023).<br>
      Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach.<br>
      <em>New Media & Society, 27(5),</em> 2684-2702. (*co-first author)
    </div>
  </div>
  <div class="publication-card" data-detail="test 📄️ 读阅原文: https://kns.cnki.net/kcms2/article/abstract?v=GkDm8A2i92VBZr4Pc9BCTuftHqtLSYVDs72W7FTmGxfw4EkljcxhCMJY_PXcoDUDbJ0UkadB4B8hs0ghaGbIOCDOSUwR5f8KMwCl92uzmX0HhWtKIAC87IOwIsbZroyTNq30gq8ntLqBK7PKGLf8ZPzN9GvOLRd9t6O4RiLs7zE=&uniplatform=NZKPT">
    <img src="/images/Nara.jpg" alt="cover image" class="publication-thumb">
    <div class="publication-content">
            \u牟怡, <span class="my-name">蓝剑锋</span>. (2023).<br>
      机器写作中的性别制定印记: 基于实验研究的实然探讨.<br>
      <em>中国网络传播研究</em>, (1)1:236-266.
    </div>
  </div>
</div>

<!-- Modal -->
<div id="popup-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button">&times;</span>
    <div id="modal-text">Loading...</div>
  </div>
</div>

<script>
  const modal = document.getElementById('popup-modal');
  const modalText = document.getElementById('modal-text');
  const closeBtn = document.querySelector('.close-button');

  document.querySelectorAll('.publication-card').forEach(card => {
    card.addEventListener('click', () => {
      const detail = card.getAttribute('data-detail') || 'No details available.';
      modalText.innerHTML = detail;
      modal.classList.add('show');
      modal.style.display = 'flex';
    });
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('show');
    setTimeout(() => { modal.style.display = 'none'; }, 200);
  });

  modal.addEventListener('click', e => {
    if (e.target === modal) {
      modal.classList.remove('show');
      setTimeout(() => { modal.style.display = 'none'; }, 200);
    }
  });
</script>
