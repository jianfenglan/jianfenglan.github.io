---
title: ""
permalink: /news/
author_profile: true
---
<style>
 
    /* 新闻列表容器 */
    .news-list {
        display: grid;
        grid-template-columns: 1fr;
        gap: 2.5rem;
        margin: 2rem 0;
    }
    /* 单个新闻卡片的样式 */
    .news-card {
        display: flex;
        flex-direction: row; 
        align-items: center; 
        gap: 2rem;
        background: white;
        border: 1px solid #e9e9e9;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .news-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    /* 图片容器样式 */
    .news-image {
        flex: 0 0 35%; 
        width: 35%;
    }
    .news-image img {
        width: 100%;
        height: auto;
        border-radius: 8px;
        display: block;
    }
    /* 文字内容容器样式 */
    .news-content {
        flex: 1;
    }
    
    .news-meta {
        margin-top: 0.75rem;
        text-align: center;
        /* --- 改动3: 增大行高，增加日期和地点的间距 --- */
        line-height: 1.8; 
    }
    .news-meta p {
        margin: 0;
        font-size: 0.85em;
        color: #888;
    }

    .news-content h3 {
        margin: 0 0 0.75rem 0;
        /* --- 改动1: 标题字号改小 --- */
        font-size: 1.2em; 
        line-height: 1.3;
    }
    .news-content p {
        margin: 0 0 1em 0;
        color: #333;
        line-height: 1.7;
        text-align: justify;
        /* --- 改动2: 正文字号改小 --- */
        font-size: 0.95em;
    }
    .news-content p:last-of-type {
        margin-bottom: 0;
    }

    /* 响应式设计 */
    @media (max-width: 768px) {
        .news-card {
            flex-direction: column;
            align-items: stretch;
        }
        .news-image {
            width: 100%;
        }
    }
</style>

<div class="news-list">

 <div class="news-card">
        <div class="news-image">
            <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}">
            <div class="news-meta">
                <p>📅 June 15, 2025</p>
                <p>📍 Denver 🇺🇸</p>
            </div>
        </div>
        <div class="news-content">
            <h3>ICA 2025</h3>
            <p>
               I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.
            </p>
            <p>
               Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.
            </p>
        </div>
    </div>

    <div class="news-card">
        <div class="news-image">
            <img src="{{ '/images/news/NCA.png' | relative_url }}">
            <div class="news-meta">
                <p>📅 November 22, 2024</p>
                <p>📍 New Orleans 🇺🇸</p>
            </div>
        </div>
        <div class="news-content">
            <h3>NCA 2024</h3>
            <p>
                My journey at NCA begins with magic! I'm thrilled to have so many friends by my side.
            </p>
            <p>
                I would especially like to thank Dr. Patrick, and Dr. Dongjing for including me at The Tenth Annual U.S.-China Communication Scholars Summit and for providing the opportunity to share my latest work.
            </p>
            <p>
                This year, I'm honored to serve as the Student Committee Chair for ACCS and as the Graduate Student Representative for CATF division in NCA. Feel free to reach out with any suggestions or for more information.
            </p>
        </div>
    </div>

    <div class="news-card">
        <div class="news-image">
            <img src="{{ '/images/news/ICA2024.png' | relative_url }}">
            <div class="news-meta">
                <p>📅 June 23, 2024</p>
                <p>📍 Gold Coast 🇦🇺</p>
            </div>
        </div>
        <div class="news-content">
            <h3>ICA 2024</h3>
            <p>
                I thoroughly enjoyed my time in Australia. Cozy was the word I used most frequently during my stay.
            </p>
            <p>
                This year, I and my colleague Kelsie, Christina and Zhi shared two papers about AIGC regulation, emerging media usage and body image issues of adolescents in China.
            </p>
            <p>
                Academic research not only provided a sense of achievement but also fostered valuable friendships. Delighted to meet everyone here!
            </p>
        </div>
    </div>

    <div class="news-card">
        <div class="news-image">
            <img src="{{ '/images/news/SICSS.png' | relative_url }}">
            <div class="news-meta">
                <p>📅 June 7, 2024</p>
                <p>📍 NUS, Singapore 🇸🇬</p>
            </div>
        </div>
        <div class="news-content">
            <h3>SICSS-Singapore</h3>
            <p>
                This summer, I'm really honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Han Li, Rongxin, Anita, Jinyuan, Xuejiao and Renwen for their uncompromising care and careful organization.
            </p>
            <p>
                Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend you sign up for the future SICSS-Singapore event and you won't regret for this decision.
            </p>
        </div>
    </div>

    <div class="news-card">
        <div class="news-image">
            <img src="{{ '/images/news/ICA2023.png' | relative_url }}">
            <div class="news-meta">
                <p>📅 May 25, 2023</p>
                <p>📍 Toronto 🇨🇦</p>
            </div>
        </div>
        <div class="news-content">
            <h3>ICA 2023</h3>
            <p>
                This is my inaugural experience of attending ICA!
            </p>
            <p>
                I was eager to engage in discourse, to gain insight, and to pursue academic inquiry. Fortunately, I received considerable assistance and support. I regard this academic excursion as a pivotal experience in my life, one that also initiated a new phase.
            </p>
        </div>
    </div>


</div>
