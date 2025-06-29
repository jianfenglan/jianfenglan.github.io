---
title: ""
permalink: /articles/
author_profile: true
---

<style>
/* 页面主宽度 */
.page__inner-wrap {
    max-width: 1600px !important;
}

/* 出版物列表布局 */
.publication-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    counter-reset: pub-counter;
    margin-top: 1rem;
}

/* 每一条出版物卡片样式 */
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

/* 封面图样式 */
.publication-thumb {
    width: 100px;
    height: 100px;
    border-radius: 12px;
    object-fit: cover;
    flex-shrink: 0;
}

/* 文字内容区域 */
.publication-content {
    flex: 1;
}

.my-name {
    color: #002FA7;
    font-weight: 700;
}

/* 链接样式 */
.publication-content a {
    color: #333333;
    text-decoration: none;
    transition: all 0.2s ease-in-out;
}

.publication-content a:hover {
    color: #002FA7;
    border-bottom-color: #002FA7;
    text-decoration: none;
}

/* 模态弹窗样式 */
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

<h2>🗞️ Journal Articles</h2>
<div class="publication-list">

  <!-- 第一篇：包含封面图 -->
  <div class="publication-card" data-detail="test">
    <img src="/images/Nara.jpg" alt="cover image" class="publication-thumb">
    <div class="publication-content">
      <span class="my-name">Lan, J.</span>, Huang, Y. (2025).
      <a href="https://journals.sagepub.com/doi/10.1177/27523543251334157" target="_blank">
        Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.
      </a> <em>Emerging Media</em>, Online first.
    </div>
  </div>

  <!-- 你可以继续添加其他文章卡片 -->
  <!-- 示例（无封面图）：
  <div class="publication-card" data-detail="即将添加详细内容...">
    <div class="publication-content">
      <span class="my-name">Lan, J.</span>, Author B. (2024). Title... <em>Journal</em>, volume(issue), pages.
    </div>
  </div>
  -->

</div>

<!-- 模态弹出层 -->
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
