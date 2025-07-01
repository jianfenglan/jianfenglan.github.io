---
title: ""
permalink: /news/
author_profile: true
---

<style>
/* 所有的 CSS 样式完全恢复到您最开始的版本，不做任何改动 */
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
    max-height: calc(100vh - 10rem); /* 留出顶部和底部空间 */
    word-wrap: break-word;
    margin-top: 5rem; /* 添加顶部间距，避免与导航栏重叠 */
}

#modal-title {
    margin-bottom: 0.75rem; /* 为弹窗标题下方添加间距 */
}

#modal-meta {
    margin-bottom: 1.5rem; /* 为弹窗元信息（日期/地点）下方添加较大间距 */
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

/* 手机页面调整 */
@media (max-width: 768px) {
    .modal-content {
        margin-top: 7rem; /* 在小屏幕上增加顶部间距 */
        max-height: calc(100vh - 12rem); /* 调整高度以适应更大间距 */
    }
}
</style>

<div class="news-list">

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2025</h2>" data-meta="📅 June 15, 2025 | 📍 Denver 🇺🇸" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver... (rest of the content)</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>NCA 2024</h2>" data-meta="📅 November 22, 2024 | 📍 New Orleans 🇺🇸" data-content="<p>My journey at NCA 2024 is off to a magical start! ... (rest of the content)</p> <img src='{{ '/images/news/NCA1.jpg' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'><img src='{{ '/images/news/NCA2.jpg' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'> ">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2024</h2>" data-meta="📅 June 23, 2024 | 📍 Gold Coast 🇦🇺" data-content="<p>I thoroughly enjoyed my time in Australia...</p> <img src='{{ '/images/news/ICA202401.JPG' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'><img src='{{ '/images/news/ICA202402.JPG' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'>  ">
    <div class="news-content"><h3>ICA 2024</h3><div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div></div>
    <div class="news-image"><img src="{{ '/images/news/ICA2024.png' | relative_url }}"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>SICSS-Singapore</h2>" data-meta="📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬" data-content="<p>This summer, I'm really honored to attend SICSS-Singapore...</p> <img src='{{ '/images/news/SICSS01.JPG' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'><img src='{{ '/images/news/SICSS02.jpg' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'>  ">
    <div class="news-content"><h3>SICSS-Singapore</h3><div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div></div>
    <div class="news-image"><img src="{{ '/images/news/SICSS.png' | relative_url }}"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2023</h2>" data-meta="📅 May 25, 2023 | 📍 Toronto 🇨🇦" data-content="<p>This is my inaugural experience of attending ICA!...</p> <img src='{{ '/images/news/ICA2301.JPG' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'><img src='{{ '/images/news/ICA2302.jpg' | relative_url }}' style='max-width: 100%; height: auto; margin-top: 15px;'> ">
    <div class="news-content"><h3>ICA 2023</h3><div class="meta">📅 May 25, 2023 | 📍 Toronto 🇨🇦</div></div>
    <div class="news-image"><img src="{{ '/images/news/ICA2023.png' | relative_url }}"></div>
</div>

</div>

<div id="news-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button" onclick="closeModal()">×</span>
    <h3 id="modal-title"></h3>
    <div class="meta" id="modal-meta"></div>
    <div id="modal-body"></div>
  </div>
</div>

<script>
function openModal(card) {
  const title = card.getAttribute('data-title');
  const meta = card.getAttribute('data-meta');
  const content = card.getAttribute('data-content');

  // ★ 修改1：将 .innerText 改为 .innerHTML 来正确渲染HTML标签
  document.getElementById('modal-title').innerHTML = title;
  document.getElementById('modal-meta').innerHTML = meta;
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

// 点击遮罩关闭
document.getElementById('news-modal').addEventListener('click', function(e) {
  if (e.target === this) { // 这个判断很关键，确保是点击在灰色背景上
    closeModal();
  }
});

// ★ 修改2：删除了下面这段可能引起冲突的代码
// document.querySelector('.modal-content').addEventListener('click', function(e) {
//   e.stopPropagation();
// });
</script>
