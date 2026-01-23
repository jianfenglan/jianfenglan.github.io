---
title: ""
permalink: /elsewhere/
author_profile: true
---

<style>

/* 强制拓宽页面主内容区域 */
.page__inner-wrap {
    max-width: 1600px !important;
}

/* 网格布局 */
.gallery-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
    padding: 1rem 0;
}

/* 卡片样式优化 */
.gallery-card {
    border: none;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
}

.gallery-card img {
    width: 100%;
    object-fit: cover;
    display: block;
    height: auto;
    /* --- 新增修改点 开始 --- */
    filter: grayscale(100%); /* 1. 默认设置为黑白 */
    transition: filter 0.4s ease; /* 2. 添加平滑过渡效果 */
    /* --- 新增修改点 结束 --- */
}

/* --- 新增CSS规则 开始 --- */
/* 3. 鼠标悬停在卡片上时，图片恢复彩色 */
.gallery-card:hover img {
    filter: grayscale(0%);
}
/* --- 新增CSS规则 结束 --- */


/* 标题文字样式优化 */
.gallery-caption {
    padding: 1rem 1.5rem;
    text-align: center;
    font-size: 0.95em;
    color: #555;
    background: #fdfdfd;
}

.gallery-caption h3 {
    margin: 0;
    font-size: 0.95em;
    line-height: 1.8;
    color: #333;
    font-weight: 400;
    text-align: right;
}

    .quote-style {
  font-family: 'Times New Roman', serif;
  font-style: italic;
  color: #002fa7; /* 克莱因蓝 */
  text-align: center;
  font-size: 0.95em;
  margin-top: 1.5rem;
}

</style>


<div class="gallery-grid">
 
<div class="gallery-card">
    <img src="{{ '/images/NewC.png' | relative_url }}">
    <div class="gallery-caption"><h3>New Castle 🇦🇺<br>January, 2026</h3></div>
  </div>
  
<div class="gallery-card">
    <img src="{{ '/images/Tokyo.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Tokyo 🇯🇵<br>November, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Hukou.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Hukou Waterfall 🇨🇳<br>October, 2025</h3></div>
  </div>
  
  <div class="gallery-card">
    <img src="{{ '/images/Osaka.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Osaka 🇯🇵<br>April, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Kyoto.png' | relative_url }}">
    <div class="gallery-caption"><h3>Kyoto 🇯🇵<br>April, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Kobe_Maiko.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Kobe 🇯🇵<br>April, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Jeju.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Jeju 🇰🇷<br>February, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Macao.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Macao 🇲🇴<br>January, 2025</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/NOLA1.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>New Orleans 🇺🇸<br>November, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Huangshan.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Yellow Mountains (Huangshan)🇨🇳<br>July, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Bluemoutains.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Blue Mountains 🇦🇺<br>June, 2024</h3></div>
  </div>
  
  <div class="gallery-card">
    <img src="{{ '/images/Sydney.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Sydney 🇦🇺<br>June, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Goldcoast.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Gold Coast 🇦🇺<br>June, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Singapore.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Singapore 🇸🇬<br>June, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Busan.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Busan 🇰🇷<br>April, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Seoul.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Seoul 🇰🇷<br>April, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/HK.png' | relative_url }}">
    <div class="gallery-caption"><h3>Hong Kong 🇭🇰<br>February, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Wuzhen.jpeg' | relative_url }}">
    <div class="gallery-caption"><h3>Wuzhen 🇨🇳<br>January, 2024</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Muztagata.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Muztagata 🇨🇳<br>July, 2023</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Niagara.jpg' | relative_url }}">
    <div class="gallery-caption"><h3>Niagara Falls 🇨🇦<br>May, 2023</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Toronto.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Toronto 🇨🇦<br>May, 2023</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Pattaya.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Pattaya 🇹🇭<br>July, 2017</h3></div>
  </div>

  <div class="gallery-card">
    <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
    <div class="gallery-caption"><h3>Bangkok 🇹🇭<br>July, 2017</h3></div>
  </div>

</div>
