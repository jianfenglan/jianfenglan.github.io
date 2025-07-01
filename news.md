---
title: ""
permalink: /news/
author_profile: true
---

<style>
.news-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
    margin: 2rem 0;
}
.news-card {
    display: flex;
    flex-direction: column;
    background: #fff;
    border: 1px solid #e6e6e6;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
}
.news-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}
.news-content {
    padding: 1.5rem;
}
.news-content h3 {
    font-size: 1.3em;
    margin: 0 0 0.5rem;
    color: #222;
}
.news-content .meta {
    font-size: 0.85em;
    color: #777;
    margin-bottom: 1rem;
}
.news-image img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    margin-bottom: -5px;
}

/* 弹窗样式同 articles 页面 */
.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    inset: 0;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(6px);
    justify-content: center;
    padding: 6rem 1rem;
}
.modal-content {
    background: #fff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    max-width: 700px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
    word-wrap: break-word;
    overflow-y: auto;
    max-height: calc(100vh - 12rem);
    margin: auto 0;
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
@media (max-width: 768px) {
    .modal-overlay {
        padding: 7rem 1rem;
    }
    .modal-content {
        max-height: calc(100vh - 14rem);
    }
}
</style>

<div class="news-list">
  <!-- 统一用 data-detail 注入完整 HTML -->
  <div class="news-card" data-detail="
    <h2>ICA 2025</h2>
    <div class='meta'>📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    <p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. ...</p>
    <img src='{{ '/images/news/ICA2025.jpg' | relative_url }}' style='width:100%; border-radius: 8px; margin-top:1rem;'>
  "></div>

  <div class="news-card" data-detail="
    <h2>NCA 2024</h2>
    <div class='meta'>📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    <p>My journey at NCA 2024 is off to a magical start! …</p>
    <img src='{{ '/images/news/NCA.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top:1rem;'>
  "></div>

  <!-- 其他若干条… -->
</div>

<!-- 弹窗 DOM 与 articles 页面保持一致 -->
<div id="news-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button">×</span>
    <div id="modal-body">Loading…</div>
  </div>
</div>

<script>
  const modal = document.getElementById('news-modal');
  const modalBody = document.getElementById('modal-body');
  const closeBtn = modal.querySelector('.close-button');

  // 卡片点击打开
  document.querySelectorAll('.news-card').forEach(card => {
    card.addEventListener('click', () => {
      modalBody.innerHTML = card.getAttribute('data-detail') || 'No details.';
      modal.classList.add('show');
      modal.style.display = 'flex';
    });
  });

  // 关闭按钮
  closeBtn.addEventListener('click', () => {
    modal.classList.remove('show');
    setTimeout(() => modal.style.display = 'none', 200);
  });

  // 点击遮罩空白处关闭
  modal.addEventListener('click', e => {
    if (e.target === modal) {
      modal.classList.remove('show');
      setTimeout(() => modal.style.display = 'none', 200);
    }
  });
</script>
