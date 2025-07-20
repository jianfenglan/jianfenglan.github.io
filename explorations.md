---
title: ""
permalink: /explorations/
author_profile: true
---

<style>
/* 强制拓宽本页面的主内容区域 - 这部分保持不变 */
.page__inner-wrap {
    max-width: 1600px !important;
}

.gallery-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
    padding: 1rem 0;
}

.gallery-card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
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
    text-align: center; /* 居中整个容器，但内部元素需要进一步对齐 */
    font-size: 0.9em;
    color: #555;
    background: #fdfdfd;
}

.gallery-caption h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.2em;
    color: #333;
    font-weight: 200;
    text-align: right;
}

.gallery-caption p {
    font-weight: 200;
}

/* --- 以下是新增的弹窗样式 --- */
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
    font-weight: 200;
}

#modal-meta {
    font-size: 0.9em;
    color: #777;
    margin-bottom: 1.5rem;
    font-weight: 200;
}

#modal-body p {
    font-size: 0.95em;
    line-height: 1.7;
    color: #333;
    margin-bottom: 1em;
    text-align: justify;
    font-weight: 200;
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

    <div class="gallery-card" onclick="openModal(this)" data-title="Wakayama" data-meta="12 March, 2025" data-content="<p>My trip to Wakayama was completely unplanned.</p>">
        <img src="{{ '/images/Wakayama.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Wakayama</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Osaka" data-meta="10 March, 2025" data-content="<p>Of course I got lost in Namba. But I genuinely appreciate the laid-back vibe of the people in Osaka.</p>">
        <img src="{{ '/images/Osaka.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Osaka</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Kyoto" data-meta="7 March, 2025" data-content="<p>The night before visiting the Senbon Torii, I rewatched <em>Memoirs of a Geisha</em>.</p>">
        <img src="{{ '/images/Kyoto.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kyoto</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Kobe" data-meta="5 March, 2025" data-content="<p>I visited Maiko to see the Akashi Kaikyo Bridge, just like in <em>Suzume</em>, absolutely breathtaking.</p>">
        <img src="{{ '/images/Kobe_Maiko.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kobe</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Jeju" data-meta="23 February, 2025" data-content="<p>The weather on Jeju Island is unpredictable.</p>">
        <img src="{{ '/images/Jeju.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Jeju</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Macau" data-meta="31 January, 2025" data-content="<p>Only the egg tart is worth trying.</p>">
        <img src="{{ '/images/Macau.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Macau</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="New Orleans" data-meta="20 November, 2024" data-content="<p>Folks swear the Gypsies in front of St. Louis Cathedral are the most gifted fortune-tellers, weaving magic with every reading. But with countless stalls sparkling under the cathedral’s shadow, how do I pick the right one to reveal my fate?</p>">
        <img src="{{ '/images/NOLA.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>New Orleans</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Sydney" data-meta="29 June, 2024" data-content="<p>Never wander under dense tree cover at night.</p>">
        <img src="{{ '/images/Sydney.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Sydney</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Gold Coast" data-meta="20 June, 2024" data-content="<p>I wish I could’ve lingered there a bit longer.</p>">
        <img src="{{ '/images/Goldcoast.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Gold Coast</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Brisbane" data-meta="16 June, 2024" data-content="<p>Is there anywhere in Brisbane that hasn’t been taken over by ibises?</p>">
        <img src="{{ '/images/Brisbane.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Brisbane</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Singapore" data-meta="4 June, 2024" data-content="<p>I highly recommend cycling along the East Coast. Imagine gazing out at the Strait of Malacca, reaching Marina Bay, and then wrapping it up with a delicious lunch in Chinatown.</p>">
        <img src="{{ '/images/Singapore.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Singapore</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Busan" data-meta="6 April, 2024" data-content="<p>Standing on the breakwater at Haeundae, a slightly anxious thought popped into my head — if a tsunami hit , which way would I run?</p>">
        <img src="{{ '/images/Busan.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Busan</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Seoul" data-meta="1 April, 2024" data-content="<p>I heard that wearing a hanbok grants free admission to Gyeongbokgung Palace. I was too shy to try.</p>">
        <img src="{{ '/images/Seoul.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Seoul</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Hong Kong" data-meta="14 February, 2024" data-content="<p>Starting from Central and hiking up to the Peak is a pleasant experience. There's a saying that couples who walk along Findlay Road will break up.</p>">
        <img src="{{ '/images/HK.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Hong Kong</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Niagara Fall" data-meta="28 May, 2023" data-content="<p>I didn’t take the boat ride for a closer view because I was afraid of getting my clothes wet.</p>">
        <img src="{{ '/images/Niagara.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Niagara Fall</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Toronto" data-meta="25 May, 2023" data-content="<p>Toronto island is an enssitial.</p>">
        <img src="{{ '/images/Toronto.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Toronto</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Pattaya" data-meta="23 July, 2017" data-content="<p>Don't go to Pattaya with you mom.</p>">
        <img src="{{ '/images/Pattaya.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Pattaya</h3>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Bangkok" data-meta="21 July, 2017" data-content="<p>Everything here is casual.</p>">
        <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Bangkok</h3>
        </div>
    </div>

</div>

<div id="gallery-modal" class="modal-overlay">
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

  const modal = document.getElementById('gallery-modal');
  modal.classList.add('show');
  modal.style.display = 'flex';
}

function closeModal() {
  const modal = document.getElementById('gallery-modal');
  modal.classList.remove('show');
  setTimeout(() => { modal.style.display = 'none'; }, 200);
}

// 点击遮罩关闭
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
    if (modal.style.display === 'flex') {
      closeModal();
    }
  }
});
</script>
