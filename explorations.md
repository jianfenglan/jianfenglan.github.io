---
title: ""
permalink: /explorations/
author_profile: true
---

<style>
    /* 强制拓宽本页面的主内容区域 */

    .gallery-grid {
        display: grid;
        /* --- 改动 1: 设置为单列布局 --- */
        grid-template-columns: 1fr;
        gap: 2.5rem; /* 增大了卡片之间的垂直间距 */
        padding: 1rem 0;
    }

    .gallery-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .gallery-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .gallery-card img {
        width: 100%;
        /* --- 改动 2: 移除了固定高度，让图片可以按比例显示为大图 --- */
        /* height: 250px; */
        object-fit: cover;
        display: block;
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
</style>


<div class="gallery-grid">
    <div class="gallery-card">
        <img src="{{ '/images/Osaka.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Osaka 🇯🇵</h3>
            <p>10 March, 2025</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Kyoto.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Kyoto 🇯🇵</h3>
            <p>7 March, 2025</p>
        </div>
    </div>


     <div class="gallery-card">
        <img src="{{ '/images/Jeju.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Jeju Island 🇰🇷</h3>
            <p>23 February, 2025</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Macau.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Macau 🇲🇴</h3>
            <p>31 January, 2025</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/NOLA.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 New Orleans 🇺🇸</h3>
            <p>20 November, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Huangshan.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Huangshan 🇨🇳</h3>
            <p>23 July, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Sydney.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Sydney 🇦🇺</h3>
            <p>29 June, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Goldcoast.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Gold Coast 🇦🇺</h3>
            <p>20 June, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Singapore.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Singapore 🇸🇬</h3>
            <p>4 June, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Busan.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Busan 🇰🇷</h3>
            <p>4 April, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Seoul.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Seoul 🇰🇷</h3>
            <p>1 April, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/HK.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Hong Kong 🇭🇰</h3>
            <p>14 February, 2024</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Baisha.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Baisha Lake 🇨🇳</h3>
            <p>12 July, 2023</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Kashgar.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Kashgar 🇨🇳</h3>
            <p>9 July, 2023</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Niagara.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Niagara Fall 🇨🇦</h3>
            <p>28 May, 2023</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Toronto.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Toronto 🇨🇦</h3>
            <p>25 May, 2023</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Hangzhou.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Hangzhou 🇨🇳</h3>
            <p>23 January, 2023</p>
        </div>
    </div>

     <div class="gallery-card">
        <img src="{{ '/images/Sanya.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Sanya 🇨🇳</h3>
            <p>9 July, 2022</p>
        </div>
    </div>

         <div class="gallery-card">
        <img src="{{ '/images/Pattaya.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Pattaya 🇹🇭</h3>
            <p>23 July, 2017</p>
        </div>
    </div>

         <div class="gallery-card">
        <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>📍 Bangkok 🇹🇭</h3>
            <p>21 July, 2017</p>
        </div>
    </div>
    
</div>
