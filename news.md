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
    border-top: 1px solid #eee;
}

/* 响应式两列排布 */
@media (min-width: 768px) {
    .news-list {
        grid-template-columns: repeat(2, 1fr);
    }
}
</style>

<div class="news-list">

<div class="news-card">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <div class="meta">📅 June 15, 2025 | 📍 Denver 🇺🇸</div>
        <p>
            I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.
        </p>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
    </div>
</div>

<div class="news-card">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <div class="meta">📅 November 22, 2024 | 📍 New Orleans 🇺🇸</div>
        <p>
            My journey at NCA begins with magic! I'm thrilled to have so many friends by my side. I would especially like to thank Dr. Patrick and Dr. Dongjing for including me at the U.S.-China Scholars Summit.
        </p>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}">
    </div>
</div>

<div class="news-card">
    <div class="news-content">
        <h3>ICA 2024</h3>
        <div class="meta">📅 June 23, 2024 | 📍 Gold Coast 🇦🇺</div>
        <p>
            I thoroughly enjoyed my time in Australia. This year, I and my colleagues shared papers about AIGC regulation and media use among Chinese adolescents. Academic research not only provided a sense of achievement but also fostered valuable friendships.
        </p>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
    </div>
</div>

<div class="news-card">
    <div class="news-content">
        <h3>SICSS-Singapore</h3>
        <div class="meta">📅 June 7, 2024 | 📍 NUS, Singapore 🇸🇬</div>
        <p>
            I'm honored to attend SICSS at National University of Singapore. Talks and discussions were insightful and full of joy. Thanks to the organizers and speakers for their generous sharing.
        </p>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/SICSS.png' | relative_url }}">
    </div>
</div>

<div class="news-card">
    <div class="news-content">
        <h3>ICA 2023</h3>
        <div class="meta">📅 May 25, 2023 | 📍 Toronto 🇨🇦</div>
        <p>
            My first ICA experience! I was eager to engage, learn, and share. This academic trip marked a pivotal moment in my scholarly life.
        </p>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2023.png' | relative_url }}">
    </div>
</div>

</div>
