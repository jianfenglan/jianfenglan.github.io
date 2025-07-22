---
title: ""
permalink: /explorations/
author_profile: true
---

<style>
/* 强制拓宽本页面的主内容区域 */
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
}

/*
.gallery-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}
*/

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
    margin: 0;
    font-size: 1.2em;
    color: #333;
    font-weight: 200;
    text-align: right; 
}

/* Removed paragraph style as it's no longer used */
/*
.gallery-caption p {
    font-weight: 200;
}
*/

/* --- Hiding the modal pop-up styles --- */
/*
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
*/
</style>

<div class="gallery-grid">

    <div class="gallery-card">
        <img src="{{ '/images/Wakayama.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Wakayama 🇯🇵<br>April, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Osaka.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Osaka 🇯🇵<br>April, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Kyoto.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kyoto 🇯🇵<br>April, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Kobe_Maiko.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Kobe 🇯🇵<br>April, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Jeju.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Jeju 🇰🇷<br>February, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Macau.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Macau 🇲🇴<br>January, 2025</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/NOLA1.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>New Orleans 🇺🇸<br>November, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Bluemountains.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Blue Mountains 🇦🇺<br>July, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Sydney.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Sydney 🇦🇺<br>June, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Goldcoast.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Gold Coast🇦🇺<br>June, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Singapore.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Singapore 🇸🇬<br>June, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Busan.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Busan 🇰🇷<br>April, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Seoul.jpeg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Seoul 🇰🇷<br>April, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/HK.png' | relative_url }}">
        <div class="gallery-caption">
            <h3>Hong Kong 🇭🇰<br>February, 2024</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Niagara.jpg' | relative_url }}">
        <div class="gallery-caption">
            <h3>Niagara Fall 🇨🇦<br>May, 2023</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Toronto.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Toronto 🇨🇦<br>May, 2023</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Pattaya.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Pattaya 🇹🇭<br>July, 2017</h3>
        </div>
    </div>

    <div class="gallery-card">
        <img src="{{ '/images/Bangkok.JPG' | relative_url }}">
        <div class="gallery-caption">
            <h3>Bangkok 🇹🇭<br>July, 2017</h3>
        </div>
    </div>

</div>
