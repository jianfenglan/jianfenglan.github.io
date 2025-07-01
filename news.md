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

/* 卡片基础样式 */
.news-card {
    display: flex; /* 改为 flex 布局，实现左右排列 */
    flex-direction: row; /* 明确为水平方向 */
    align-items: stretch; /* 让子项高度撑满容器 */
    background: #fff;
    border: 1px solid #e6e6e6;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
    height: 200px; /* 为卡片设置一个固定高度 */
}

.news-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

/* 卡片左侧：文字内容区域 */
.news-content {
    flex: 6; /* 分配 6 份宽度 */
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center; /* 垂直居中 */
}

.news-content h3 {
    font-size: 1.3em;
    margin: 0 0 0.5rem;
    color: #222;
}

.news-content .meta {
    font-size: 0.85em;
    color: #777;
    margin-bottom: 0; /* 移除底部边距，因为内容已居中 */
}

.news-content p {
    display: none; /* 在卡片视图中隐藏详细描述 */
}

/* 卡片右侧：图片区域 */
.news-image {
    flex: 4; /* 分配 4 份宽度 */
}

.news-image img {
    width: 100%;
    height: 100%; /* 高度充满容器 */
    display: block;
    object-fit: cover; /* 保持图片比例并裁剪 */
}

/* --- 弹窗样式 --- */
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

/* 弹窗外部容器 */
.modal-content {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    max-width: 700px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
    overflow: hidden; /* 隐藏内部溢出，确保圆角一直可见 */
    margin-top: 5rem;
    max-height: calc(100vh - 10rem); /* 整体最大高度 */
    display: flex;
    flex-direction: column;
}

.modal-overlay.show .modal-content {
    transform: scale(1);
}

/* 新增：弹窗内部可滚动区域 */
.modal-scroll-wrapper {
    padding: 2rem;
    overflow-y: auto; /* 只让这个区域滚动 */
    word-wrap: break-word;
}

/* 弹窗内容中的图片样式 */
#modal-body img {
    max-width: 100%;
    height: auto;
    margin-top: 15px;
    border-radius: 14px; /* 为图片添加圆角 */
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
    z-index: 10; /* 确保关闭按钮在最上层 */
}

/* 手机页面调整 */
@media (max-width: 768px) {
    .news-card {
        flex-direction: column; /* 在手机上恢复为垂直布局 */
        height: auto; /* 高度自动 */
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
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>NCA 2024</h2>" data-meta="📅 November 22, 2024 | 📍 New Orleans 🇺🇸" data-content="<p>My journey at NCA 2024 is off to a magical start! I’m thrilled to be surrounded by so many supportive friends and colleagues.</p><p>I extend my heartfelt gratitude to Dr. Patrick and Dr. Dongjing for inviting me to the Tenth Annual U.S.-China Communication Scholars Summit and giving me the opportunity to present my latest research.</p><p>This year, I’m honored to serve as the Student Committee Chair for ACCS and the Graduate Student Representative for the CATF division at NCA. I welcome your suggestions and invite you to reach out for more information.</p><p>A delightful highlight this year is the addition of a Zumba party—dancing truly brings so much joy!</p> <img src='{{ '/images/news/NCA1.jpg' | relative_url }}'><img src='{{ '/images/news/NCA2.jpg' | relative_url }}'> ">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2024</h2>" data-meta="📅 June 23, 2024 | 📍 Gold Coast 🇦🇺" data-content="<p>I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.</p><p>This year, I and my colleague Kelsie, Christina and Zhi shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.</p><p>Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!</p> <img src='{{ '/images/news/ICA202401.JPG' | relative_url }}'><img src='{{ '/images/news/ICA202402.JPG' | relative_url }}'>  ">
    <div class="news-content">
        <h3>ICA 2024</h3>
        <div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>SICSS-Singapore</h2>" data-meta="📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬" data-content="<p>This summer, I'm really honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.</p><p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS-Singapore event and you won't regret for this decision.</p> <img src='{{ '/images/news/SICSS01.JPG' | relative_url }}'><img src='{{ '/images/news/SICSS02.jpg' | relative_url }}'>  ">
    <div class="news-content">
        <h3>SICSS-Singapore</h3>
        <div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/SICSS.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="<h2 style='font-size: 2.5em; margin-bottom: 10px;'>ICA 2023</h2>" data-meta="📅 May 25, 2023 | 📍 Toronto 🇨🇦" data-content="<p>This is my inaugural experience of attending ICA!</p><p>I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.</p> <img src='{{ '/images/news/ICA2301.JPG' | relative_url }}'><img src='{{ '/images/news/ICA2302.jpg' | relative_url }}'> ">
    <div class="news-content">
        <h3>ICA 2023</h3>
        <div class="meta">📅 May 25, 2023 | 📍 Toronto 🇨🇦</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2023.png' | relative_url }}">
    </div>
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

  // 使用 innerHTML 来正确渲染 HTML 标签
  document.getElementById('modal-title').innerHTML = title;
  document.getElementById('modal-meta').innerHTML = meta;
  document.getElementById('modal-body').innerHTML = content;

  const modal = document.getElementById('news-modal');
  modal.style.display = 'flex';
  // 延迟添加 show 类以触发 CSS 过渡效果
  setTimeout(() => { modal.classList.add('show'); }, 10); 
}

function closeModal() {
  const modal = document.getElementById('news-modal');
  modal.classList.remove('show');
  // 在过渡动画结束后再隐藏元素
  setTimeout(() => { modal.style.display = 'none'; }, 300);
}

// 点击遮罩关闭
document.getElementById('news-modal').addEventListener('click', function(e) {
  if (e.target === this) {
    closeModal();
  }
});

// 阻止事件冒泡到遮罩层
document.querySelector('.modal-content').addEventListener('click', function(e) {
  e.stopPropagation();
});
</script>
