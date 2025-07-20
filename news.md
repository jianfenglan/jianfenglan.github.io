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
    flex-direction: row;
    background: #fff;
    border: 1px solid #e6e6e6;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    overflow: hidden; /* Ensure content doesn't spill out if constrained */
    transition: all 0.3s ease;
    cursor: pointer;
}

.news-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.news-content {
    flex: 4;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    /* --- NEW --- */
    min-height: 0; /* Allows content to shrink correctly within flexbox */
    /* If content frequently overflows and you want scrollbars within the text area: */
    /* overflow-y: auto; */
    /* --- END NEW --- */
}

.news-image {
    flex: 6;
    /* --- NEW --- */
    height: 100%; /* Make image container fill the card height */
    /* --- END NEW --- */
}

.news-image img {
    width: 100%;
    height: 100%; /* Make the image fill its parent container */
    display: block;
    object-fit: cover; /* This is key: scales and crops image to fill container */
}

.news-content h3 {
    font-size: 0.95em;
    margin: 0 0 0.5rem;
    color: #333;
    font-weight: 300;
}

.news-content .meta {
    font-size: 0.85em;
    color: #333;
    font-weight: 300; /* Adjusted to 300 for consistency */
}

.news-content p {
    font-size: 0.95em;
    line-height: 1.7;
    color: #333;
    margin-bottom: 1em;
    text-align: justify;
    font-weight: 300; /* Adjusted to 300 for consistency */
}

.news-content p:last-of-type {
    margin-bottom: 0;
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
    max-height: calc(100vh - 10rem);
    word-wrap: break-word;
    margin-top: 5rem;
}

/* 新增：为弹窗正文（#modal-body）里的图片添加样式 */
#modal-body img {
    max-width: 100%;
    height: auto;
    margin-top: 15px;
    border-radius: 14px;
}

#modal-title {
    margin-bottom: 0.75rem;
    font-weight: 300;
}

#modal-meta {
    margin-bottom: 1.5rem;
    font-weight: 300;
}

/* 新增：为弹窗正文中的 p 标签设置字重 */
#modal-body p {
    font-weight: 300; /* Adjusted to 300 for consistency */
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
    color: #333;
}

@media (max-width: 768px) {
    .news-card {
        flex-direction: column;
        /* --- NEW --- */
        height: auto; /* Allow height to adjust on small screens */
        /* --- END NEW --- */
    }
    .news-image {
        height: 200px; /* Fixed height for image on mobile for consistency */
    }
    .modal-content {
        margin-top: 7rem;
        max-height: calc(100vh - 12rem);
    }
}
</style>

<div class="news-list">


<div class="news-card" onclick="openModal(this)" data-title="IAMCR 2025" data-meta="July 15, 2025 | Singapore" data-content="<p>While my physical form was tragically unable to grace the halls of IAMCR 2025 this year, my fantastic colleague and co-author, Jingyi Li, represented us beautifully.<br><br>Holding in Asia, this year's IAMCR conference attracted so many scholars and friends from China. While I definitely felt a pang of FOMO, it was quickly replaced by pride in Jingyi's stellar delivery and the vibrant community gathered there.<br><br>Maybe next year I'll figure out how to teleport!</p>">
    <div class="news-content">
        <h3>IAMCR 2025</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/IAMCR2025.jpg' | relative_url }}">
    </div>
</div>


<div class="news-card" onclick="openModal(this)" data-title="ICA 2025" data-meta="June 15, 2025 | Denver" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p><p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="NCA 2024" data-meta="November 22, 2024 | New Orleans" data-content="<p>My journey at NCA 2024 is off to a magical start! I’m thrilled to be surrounded by so many supportive friends and colleagues.</p><p>I extend my heartfelt gratitude to Dr. Patrick and Dr. Dongjing for inviting me to the Tenth Annual U.S.-China Communication Scholars Summit and giving me the opportunity to present my latest research.</p><p>This year, I’m honored to serve as the Student Committee Chair for ACCS and the Graduate Student Representative for the CATF division at NCA. I welcome your suggestions and invite you to reach out for more information.</p> ">
    <div class="news-content">
        <h3>NCA 2024</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2024" data-meta="June 23, 2024 | Gold Coast" data-content="<p>I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.</p><p>This year, I and my colleague Kelsie, Christina and Zhi shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.</p><p>Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!</p>">
    <div class="news-content">
        <h3>ICA 2024</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="SICSS-Singapore" data-meta="June 7, 2024 | Singapore" data-content="<p>This summer, I'm really honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.</p><p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS-Singapore event and you won't regret for this decision.</p>">
    <div class="news-content">
        <h3>SICSS-Singapore</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/SICSS01.JPG' | relative_url }}">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2023" data-meta="May 25, 2023 | Toronto" data-content="<p>This is my inaugural experience of attending ICA!</p><p>I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.</p>">
    <div class="news-content">
        <h3>ICA 2023</h3>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2302.jpg' | relative_url }}">
    </div>
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
document.getElementById('news-modal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

// 阻止模态框内容上的点击事件冒泡
document.querySelector('.modal-content').addEventListener('click', function(e) {
    e.stopPropagation();
});
</script>
