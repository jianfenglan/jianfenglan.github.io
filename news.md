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

/* 弹窗样式 */
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

  <!-- ICA 2025 -->
  <div class="news-card" data-detail="
    <h2>ICA 2025</h2>
    <div class='meta'>📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    <p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p>
    <p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>
    <img src='{{ '/images/news/ICA2025.jpg' | relative_url }}' style='width:100%; border-radius:8px; margin-top:1rem;'>
  ">
    <div class="news-content">
      <h3>ICA 2025</h3>
      <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
    </div>
    <div class="news-image">
      <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
  </div>

  <!-- NCA 2024 -->
  <div class="news-card" data-detail="
    <h2>NCA 2024</h2>
    <div class='meta'>📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    <p>My journey at NCA 2024 is off to a magical start! I’m thrilled to be surrounded by so many supportive friends and colleagues.</p>
    <p>I extend my heartfelt gratitude to Dr. Patrick and Dr. Dongjing for inviting me to the Tenth Annual U.S.-China Communication Scholars Summit and giving me the opportunity to present my latest research.</p>
    <p>This year, I’m honored to serve as the Student Committee Chair for ACCS and the Graduate Student Representative for the CATF division at NCA. I welcome your suggestions and invite you to reach out for more information.</p>
    <p>A delightful highlight this year is the addition of a Zumba party—dancing truly brings so much joy!</p>
    <img src='{{ '/images/news/NCA1.jpg' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
    <img src='{{ '/images/news/NCA2.jpg' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
  ">
    <div class="news-content">
      <h3>NCA 2024</h3>
      <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
    </div>
    <div class="news-image">
      <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
  </div>

  <!-- ICA 2024 -->
  <div class="news-card" data-detail="
    <h2>ICA 2024</h2>
    <div class='meta'>📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
    <p>I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.</p>
    <p>This year, my colleagues Kelsie, Christina and Zhi and I shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.</p>
    <p>Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!</p>
    <img src='{{ '/images/news/ICA202401.JPG' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
    <img src='{{ '/images/news/ICA202402.JPG' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
  ">
    <div class="news-content">
      <h3>ICA 2024</h3>
      <div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
    </div>
    <div class="news-image">
      <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
    </div>
  </div>

  <!-- SICSS-Singapore -->
  <div class="news-card" data-detail="
    <h2>SICSS‑Singapore</h2>
    <div class='meta'>📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
    <p>This summer, I'm really honored to attend SICSS‑Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.</p>
    <p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS‑Singapore event and you won't regret this decision.</p>
    <img src='{{ '/images/news/SICSS01.JPG' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
    <img src='{{ '/images/news/SICSS02.jpg' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
  ">
    <div class="news-content">
      <h3>SICSS‑Singapore</h3>
      <div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
    </div>
    <div class="news-image">
      <img src="{{ '/images/news/SICSS.png' | relative_url }}">
    </div>
  </div>

  <!-- ICA 2023 -->
  <div class="news-card" data-detail="
    <h2>ICA 2023</h2>
    <div class='meta'>📅 May 25, 2023 | 📍 Toronto 🇨🇦</div>
    <p>This is my inaugural experience of attending ICA!</p>
    <p>I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.</p>
    <img src='{{ '/images/news/ICA2301.JPG' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
    <img src='{{ '/images/news/ICA2302.jpg' | relative_url }}' style='max-width:100%; height:auto; margin-top:15px;'>
  ">
    <div class="news-content">
      <h3>ICA 2023</h3>
      <div class="meta">📅 May 25, 2023 | 📍 Toronto 🇨🇦</div>
    </div>
    <div class="news-image">
      <img src="{{ '/images/news/ICA2023.png' | relative_url }}">
    </div>
  </div>

</div>

<!-- 弹窗结构 -->
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

  // 点击卡片打开弹窗
  document.querySelectorAll('.news-card').forEach(card => {
    card.addEventListener('click', () => {
      modalBody.innerHTML = card.getAttribute('data-detail') || 'No details.';
      modal.classList.add('show');
      modal.style.display = 'flex';
    });
  });

  // 点击关闭按钮
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
