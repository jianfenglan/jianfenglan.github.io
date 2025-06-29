---
title: ""
permalink: /explorations/
author_profile: true
---

<style>
    /* 强制拓宽本页面的主内容区域 */

    .gallery-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 2.5rem; /* 控制卡片之间的垂直间距 */
        padding: 1rem 0;
    }

    .gallery-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer; /* 添加手型光标，提示可点击 */
    }

    .gallery-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .gallery-card img {
        width: 100%;
        object-fit: cover;
        display: block;
        height: auto;
    }

    .gallery-caption {
        padding: 1rem 1.5rem;
        text-align: center;
        font-size: 0.9em;
        color: #555;
        background: #fdfdfd;
    }

    .gallery-caption h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.2em;
        color: #333;
    }

    /* --- 以下是弹窗样式 (与 news 页面保持一致) --- */
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
    
    #modal-title {
        margin-top: 0;
        margin-bottom: 0.75rem;
    }

    #modal-meta {
        font-size: 0.9em;
        color: #777;
        margin-bottom: 1.5rem;
    }
    
    #modal-body p {
        font-size: 0.95em;
        line-height: 1.7;
        color: #333;
        margin-bottom: 1em;
        text-align: justify;
    }
    
    #modal-body p:last-of-type {
        margin-bottom: 0;
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

<div class="gallery-grid">

    <div class="gallery-card" onclick="openModal(this)" data-title="Wakayama 🇯🇵" data-meta="12 March, 2025" data-content="<p>Our trip to Wakayama was completely unplanned, yet it felt like we had stumbled into a hidden paradise. This city, once glorious, welcomed us as we narrowly caught the last bus from the seaside back to town at 4 p.m. 🙈</p>">
        <img src="{{ '/images/Wakayama.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Wakayama 🇯🇵</h3>
            <p>12 March, 2025</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Osaka 🇯🇵" data-meta="10 March, 2025" data-content="<p>As expected, we got lost in Namba 🗺. But I genuinely appreciate the laid-back vibe of the people in Osaka.</p>">
        <img src="{{ '/images/Osaka.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Osaka 🇯🇵</h3>
            <p>10 March, 2025</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Kyoto 🇯🇵" data-meta="7 March, 2025" data-content="<p>The night before visiting the Senbon Torii ⛩️, my friends and I rewatched Memoirs of a Geisha. So the next day, I really wore a kimono👘 and clacked through Kyoto in wooden sandals.</p>">
        <img src="{{ '/images/Kyoto.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kyoto 🇯🇵</h3>
            <p>7 March, 2025</p>
        </div>
    </div>
    
    <div class="gallery-card" onclick="openModal(this)" data-title="Bangkok 🇹🇭" data-meta="21 July, 2017" data-content="<p>Love food here. 🥰</p>">
        <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Bangkok 🇹🇭</h3>
            <p>21 July, 2017</p>
        </div>
    </div>

</div>

<div id="gallery-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button" onclick="closeModal()">&times;</span>
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

    // 将内容填充到弹窗里
    document.getElementById('modal-title').innerHTML = title;
    document.getElementById('modal-meta').innerHTML = meta;
    document.getElementById('modal-body').innerHTML = content;

    // 获取ID为 'gallery-modal' 的弹窗元素并显示它
    const modal = document.getElementById('gallery-modal');
    modal.style.display = 'flex';
    
    // 延迟一小下再添加 'show' 类以触发CSS动画
    // (这是 news 页面能够成功显示动画的简单做法)
    setTimeout(() => {
        modal.classList.add('show');
    }, 10); 
}

function closeModal() {
    // 获取ID为 'gallery-modal' 的弹窗元素
    const modal = document.getElementById('gallery-modal');
    modal.classList.remove('show');
    
    // 等待动画（0.3秒）结束后再彻底隐藏
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300); // 这个时间应与 CSS transition 时间（0.3s）一致
}

// 点击遮罩层（灰色背景）关闭弹窗
window.addEventListener('click', function(e) {
    const modal = document.getElementById('gallery-modal');
    if (e.target === modal) {
        closeModal();
    }
});

// 按下 Escape 键关闭弹窗
window.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const modal = document.getElementById('gallery-modal');
        // 检查弹窗是否正显示
        if (modal.style.display === 'flex') {
            closeModal();
        }
    }
});
</script>
