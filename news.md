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

.news-content p {
    font-size: 0.95em;
    line-height: 1.7;
    color: #333;
    margin-bottom: 1em;
    text-align: justify;
}

.news-content p:last-of-type {
    margin-bottom: 0;
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
    max-width: 700px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
    overflow-y: auto;
    max-height: 90vh;
    word-wrap: break-word;
}

.modal-content h2 {
    font-size: 1.5em;
    margin-bottom: 0.75rem;
    color: #222;
}

#modal-meta {
    margin-bottom: 1.5rem;
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

<div class="news-list">

<!-- 每张卡片结构（略） -->
<!-- 此处插入你的每个 news-card，保持 data-title="<h2>标题</h2>" 不变 -->

<!-- 示例（保留一张卡片为例，其余照抄） -->
<div class="news-card" onclick="openModal(this)" data-title="<h2>ICA 2025</h2>" data-meta="📅 June 15, 2025 | 📍 Denver 🇺🇸" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p><p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<!-- 其余 news-card 按照上面的格式继续填入 -->

</div>

<!-- Modal -->
<div id="news-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button" onclick="closeModal()">&times;</span>
    <div id="modal-title"></div> <!-- 用 div 容纳 h2 -->
    <div class="meta" id="modal-meta"></div>
    <div id="modal-body"></div>
  </div>
</div>

<script>
function openModal(card) {
  const title = card.getAttribute('data-title');
  const meta = card.getAttribute('data-meta');
  const content = card.getAttribute('data-content');

  document.getElementById('modal-title').innerHTML = title;
  document.getElementById('modal-meta').innerText = meta;
  document.getElementById('modal-body').innerHTML = content;

  const modal = document.getElementById('news-modal');
  modal.classList.add('show');
  modal.style.display = 'flex';
}

function closeModal() {
  const modal = document.getElementById('news-modal');
  modal.classList.remove('show');
  setTimeout(() => { modal.style.display = 'none'; }, 200);
}

window.addEventListener('click', function(e) {
  const modal = document.getElementById('news-modal');
  if (e.target === modal) {
    closeModal();
  }
});
</script>
