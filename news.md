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
</style>

<div class="news-list">

<div class="news-card" onclick="openModal(this)" data-title="ICA 2025" data-meta="📅 June 15, 2025 | 📍 Denver 🇺🇸" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p><p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="NCA 2024" data-meta="📅 November 22, 2024 | 📍 New Orleans 🇺🇸" data-content="<p>My journey at NCA begins with magic! I'm thrilled to have so many friends by my side.</p><p>I would especially like to thank Dr. Patrick, and Dr. Dongjing for including me at The Tenth Annual U.S.-China Communication Scholars Summit and for providing the opportunity to share my latest work.</p><p>This year, I'm honored to serve as the Student Committee Chair for ACCS and as the Graduate Student Representative for CATF division in NCA. Feel free to reach out with any suggestions or for more information.</p>">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2024" data-meta="📅 June 23, 2024 | 📍 Gold Coast 🇦🇺" data-content="<p>I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.</p><p>This year, I and my colleague Kelsie, Christina and Zhi shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.</p><p>Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!</p>">
    <div class="news-content">
        <h3>ICA 2024</h3>
        <div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="SICSS-Singapore" data-meta="📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬" data-content="<p>This summer, I'm really honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.</p><p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS-Singapore event and you won't regret for this decision.</p>">
    <div class="news-content">
        <h3>SICSS-Singapore</h3>
        <div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/SICSS.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2023" data-meta="📅 May 25, 2023 | 📍 Toronto 🇨🇦" data-content="<p>This is my inaugural experience of attending ICA!</p><p>I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.</p>">
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

  document.getElementById('modal-title').innerText = title;
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

// 点击遮罩关闭
window.addEventListener('click', function(e) {
  const modal = document.getElementById('news-modal');
  if (e.target === modal) {
    closeModal();
  }
});
</script>
