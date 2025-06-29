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

    <div class="gallery-card" onclick="openModal(this)" data-title="Kobe 🇯🇵" data-meta="5 March, 2025" data-content="<p>Compared to beef, it’s Arima Onsen that truly captivates me and keeps me coming back. 🫧</p>">
        <img src="{{ '/images/Kobe_Maiko.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kobe 🇯🇵</h3>
            <p>5 March, 2025</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Jeju 🇰🇷" data-meta="23 February, 2025" data-content="<p>The island’s weather is so unpredictable — can you imagine? One moment it’s bright and sunny, and the next, snow is falling heavily. 🏝️☀️❄️</p>">
        <img src="{{ '/images/Jeju.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Jeju 🇰🇷</h3>
            <p>23 February, 2025</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Macau 🇲🇴" data-meta="31 January, 2025" data-content="<p>Only the egg tart is worth trying. 😤</p>">
        <img src="{{ '/images/Macau.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Macau 🇲🇴</h3>
            <p>31 January, 2025</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="New Orleans 🇺🇸" data-meta="20 November, 2024" data-content="<p>People say the Gypsies in front of St. Louis Cathedral are the most skilled fortune-tellers. But with so many stalls lined up, how can I ever find the right one? 🔮</p>">
        <img src="{{ '/images/NOLA.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>New Orleans 🇺🇸</h3>
            <p>20 November, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Sydney 🇦🇺" data-meta="29 June, 2024" data-content="<p>Never walk under dense tree cover at night — trust me, you don't wanna know why. 🦇</p>">
        <img src="{{ '/images/Sydney.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Sydney 🇦🇺</h3>
            <p>29 June, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Gold Coast 🇦🇺" data-meta="20 June, 2024" data-content="<p>Even in winter, you can lie on the Gold Coast in a T-shirt, bathing the sunshine. Really wish I could have stayed there a little longer. 😩</p>">
        <img src="{{ '/images/Goldcoast.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Gold Coast 🇦🇺</h3>
            <p>20 June, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Brisbane 🇦🇺" data-meta="16 June, 2024" data-content="<p>Is there anywhere in Brisbane that hasn’t been taken over by ibises? 🐦</p>">
        <img src="{{ '/images/Brisbane.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Brisbane 🇦🇺</h3>
            <p>16 June, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Singapore 🇸🇬" data-meta="4 June, 2024" data-content="<p>I highly recommend cycling along the East Coast — from gazing out at the Strait of Malacca to reaching Marina Bay, and finally wrapping it up with a delicious lunch in Chinatown. 🚴</p>">
        <img src="{{ '/images/Singapore.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Singapore 🇸🇬</h3>
            <p>4 June, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Busan 🇰🇷" data-meta="6 April, 2024" data-content="<p>Standing on the breakwater at Haeundae, I couldn’t help but wonder — if a tsunami🌊 hit, which way would I run? Plus, the night view of Busan from the Hwangnyeongsan mountaintop is absolutely worth the climb</p>">
        <img src="{{ '/images/Busan.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Busan 🇰🇷</h3>
            <p>6 April, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Seoul 🇰🇷" data-meta="1 April, 2024" data-content="<p>I heard that wearing a hanbok grants free admission to Gyeongbokgung Palace. Unfortunately, I was too shy to try it myself — but thanks to that rule, I got to enjoy a different kind of scenery.</p>">
        <img src="{{ '/images/Seoul.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Seoul 🇰🇷</h3>
            <p>1 April, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Hong Kong 🇭🇰" data-meta="14 February, 2024" data-content="<p>Starting from Central and hiking up to the Peak is a truly pleasant experience. There's a saying that couples who walk along Findlay Road will break up — and it seems eerily accurate.</p>">
        <img src="{{ '/images/HK.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Hong Kong 🇭🇰</h3>
            <p>14 February, 2024</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Baisha Lake 🇨🇳" data-meta="12 July, 2023" data-content="<p>This place feels almost unreal, like a dream. White yaks tread through the crystal-clear lake water that ripples like ocean waves, while the distant ivory sand is so pure it could easily be mistaken for snow.</p>">
        <img src="{{ '/images/Baisha.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Baisha Lake 🇨🇳</h3>
            <p>12 July, 2023</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Niagara Fall 🇨🇦" data-meta="28 May, 2023" data-content="<p>There are two things I regret: <br>I didn’t take the boat ride for a closer view because I was afraid of getting my clothes wet；<br>I didn’t take the chance to escape to the U.S. 🫨</p>">
        <img src="{{ '/images/Niagara.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Niagara Fall 🇨🇦</h3>
            <p>28 May, 2023</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Toronto 🇨🇦" data-meta="25 May, 2023" data-content="<p>Toronto island is an enssitial to visit.🥹 And Haidilao isn't affordable. 🤯</p>">
        <img src="{{ '/images/Toronto.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Toronto 🇨🇦</h3>
            <p>25 May, 2023</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Pattaya 🇹🇭" data-meta="23 July, 2017" data-content="<p>Never go to Pattaya with you mom. 🥲</p>">
        <img src="{{ '/images/Pattaya.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Pattaya 🇹🇭</h3>
            <p>23 July, 2017</p>
        </div>
    </div>

    <div class="gallery-card" onclick="openModal(this)" data-title="Bangkok 🇹🇭" data-meta="21 July, 2017" data-content="<p>I love the street food in Bangkok; everything here is so casual, perfect for a first-time international trip. 🥰</p>">
        <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Bangkok 🇹🇭</h3>
            <p>21 July, 2017</p>
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
