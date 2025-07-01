---
title: ""
permalink: /news/
author_profile: true
---

<style>
/* 卡片列表网格布局 */
.news-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
    margin: 2rem 0;
}

/* 卡片基础样式 - 全新、更安全的版本 */
.news-card {
    display: flex; /* 启用 flex 布局 */
    flex-direction: row; /* 水平排列 */
    background: #fff;
    border: 1px solid #e6e6e6;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    overflow: hidden; /* 必须保留，确保圆角生效 */
    transition: all 0.3s ease;
    cursor: pointer;
    min-height: 180px; /* 设置一个最小高度，避免内容过少时卡片太扁 */
}

.news-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

/* 卡片左侧：文字内容 */
.news-content {
    flex: 1 1 60%; /* flex-grow, flex-shrink, flex-basis. 更灵活的宽度设置 */
    padding: 1.5rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.news-content h3 {
    font-size: 1.3em;
    margin: 0 0 0.5rem;
    color: #222;
}

.news-content .meta {
    font-size: 0.85em;
    color: #777;
}

/* 卡片右侧：图片区域 */
.news-image {
    flex: 1 1 40%;
    background-size: cover; /* 背景图覆盖整个区域 */
    background-position: center; /* 图片居中显示 */
    min-width: 120px; /* 保证图片区域不会被过度挤压 */
}

/* 移除 .news-image img 的特定样式，因为我们不再使用 <img> 标签 */

/* --- 弹窗样式 (保持上次的修正) --- */
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
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    max-width: 700px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
    overflow: hidden;
    margin-top: 5rem;
    max-height: calc(100vh - 10rem);
    display: flex;
    flex-direction: column;
}

.modal-overlay.show .modal-content {
    transform: scale(1);
}

.modal-scroll-wrapper {
    padding: 2rem;
    overflow-y: auto;
    word-wrap: break-word;
}

/* 为弹窗内的图片添加圆角 */
#modal-body img {
    max-width: 100%;
    height: auto;
    margin-top: 15px;
    border-radius: 14px;
}

#modal-title {
    margin-bottom: 0.75rem;
}

#modal-meta {
    margin-bottom: 1.5rem;
    font-size: 0.85em;
    color: #777;
}

.close-button {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    cursor: pointer;
    color: #666;
    z-index: 10;
}

/* 手机页面响应式调整 */
@media (max-width: 768px) {
    .news-card {
        flex-direction: column; /* 在手机上恢复为上下布局 */
    }
    .news-image {
        min-height: 180px; /* 在手机上给图片一个最小高度 */
    }
    .modal-content {
        margin-top: 7rem;
        max-height: calc(100vh - 12rem);
    }
}
</style>

<div class="news-list">

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2025</h2>" data-meta="📅 June 15, 2025 | 📍 Denver 🇺🇸" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p><p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    </div>
    <div class="news-image" style="background-image: url('{{ '/images/news/ICA2025.jpg' | relative_url }}');"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>NCA 2024</h2>" data-meta="📅 November 22, 2024 | 📍 New Orleans 🇺🇸" data-content="<p>My journey at NCA 2024 is off to a magical start! I’m thrilled to be surrounded by so many supportive friends and colleagues.</p><p>I extend my heartfelt gratitude to Dr. Patrick and Dr. Dongjing for inviting me to the Tenth Annual U.S.-China Communication Scholars Summit and giving me the opportunity to present my latest research.</p><p>This year, I’m honored to serve as the Student Committee Chair for ACCS and the Graduate Student Representative for the CATF division at NCA. I welcome your suggestions and invite you to reach out for more information.</p><p>A delightful highlight this year is the addition of a Zumba party—dancing truly brings so much joy!</p> <img src='{{ '/images/news/NCA1.jpg' | relative_url }}'><img src='{{ '/images/news/NCA2.jpg' | relative_url }}'> ">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    </div>
    <div class="news-image" style="background-image: url('{{ '/images/news/NCA.png' | relative_url }}');"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2024</h2>" data-meta="📅 June 23, 2024 | 📍 Gold Coast 🇦🇺" data-content="<p>I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.</p><p>This year, I and my colleague Kelsie, Christina and Zhi shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.</p><p>Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!</p> <img src='{{ '/images/news/ICA202401.JPG' | relative_url }}'><img src='{{ '/images/news/ICA202402.JPG' | relative_url }}'>  ">
    <div class="news-content">
        <h3>ICA 2024</h3>
        <div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
    </div>
    <div class="news-image" style="background-image: url('{{ '/images/news/ICA2024.png' | relative_url }}');"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>SICSS-Singapore</h2>" data-meta="📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬" data-content="<p>This summer, I'm really honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.</p><p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS-Singapore event and you won't regret for this decision.</p> <img src='{{ '/images/news/SICSS01.JPG' | relative_url }}'><img src='{{ '/images/news/SICSS02.jpg' | relative_url }}'>  ">
    <div class="news-content">
        <h3>SICSS-Singapore</h3>
        <div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
    </div>
    <div class="news-image" style="background-image: url('{{ '/images/news/SICSS.png' | relative_url }}');"></div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2023</h2>" data-meta="📅 May 25, 2023 | 📍 Toronto 🇨🇦" data-content="<p>This is my inaugural experience of attending ICA!</p><p>I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.</p> <img src='{{ '/images/news/ICA2301.JPG' | relative_url }}'><img src='{{ '/images/news/ICA2302.jpg' | relative_url }}'> ">
    <div class="news-content">
        <h3>ICA 2023</h3>
        <div class="meta">📅 May 25, 2023 | 📍 Toronto 🇨🇦</div>
    </div>
    <div class="news-image" style="background-image: url('{{ '/images/news/ICA2023.png' | relative_url }}');"></div>
</div>

</div>

<div id="news-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button" onclick="closeModal()">×</span>
    <div class="modal-scroll-wrapper">
        <div id="modal-title"></div>
        <div id="modal-meta"></div>
        <div id="modal-body"></div>
    </div>
  </div>
</div>

<script>
function openModal(card) {
  const title = card.getAttribute('data-title');
  const meta = card.getAttribute('data-meta');
  const content = card.getAttribute('data-content');

  document.getElementById('modal-title').innerHTML = title;
  document.getElementById('modal-meta').innerHTML = meta;
  document.getElementById('modal-body').innerHTML = content;

  const modal = document.getElementById('news-modal');
  modal.style.display = 'flex';
  setTimeout(() => { modal.classList.add('show'); }, 10); 
}

function closeModal() {
  const modal = document.getElementById('news-modal');
  modal.classList.remove('show');
  setTimeout(() => { modal.style.display = 'none'; }, 300);
}

document.getElementById('news-modal').addEventListener('click', function(e) {
  if (e.target === this) {
    closeModal();
  }
});

document.querySelector('.modal-content').addEventListener('click', function(e) {
  e.stopPropagation();
});
</script>
