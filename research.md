---
title: ""
permalink: /research/
author_profile: true
---

<style>
/* =========================================
   1. 全局基础设置
   ========================================= */
.page__inner-wrap {
    max-width: 1600px !important;
}

body {
    font-size: 0.95em;
    line-height: 1.75;
    font-weight: 400;
}

/* 链接与辅助文本颜色 */
.publication-link, 
.auxiliary-text,
.auxiliary-text-inline {
    color: #999;
    font-size: 0.9em;
    text-decoration: none;
    transition: color 0.2s ease;
}

.publication-link {
    display: inline-block; /* 改为 inline-block 以便更好排版 */
    margin-top: 0.2rem;
}

.publication-link:hover {
    color: #666;
    text-decoration: underline;
}

.auxiliary-text {
    display: block;
    line-height: 1.6;
}

h2 {
    font-weight: 400; 
    font-size: 1.1em;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid #f0f0f0; /* 加个淡淡的下划线区分区块 */
    padding-bottom: 0.5rem;
}

.my-name {
    color: #002FA7;
    font-weight: 400;
}

/* =========================================
   2. Publications (左文右图布局)
   ========================================= */
.publication-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    counter-reset: pub-counter;
}

.publication-card {
    display: flex;
    justify-content: space-between; /* 两端对齐：左文右图 */
    align-items: flex-start; /* 顶部对齐 */
    background: #fff;
    border-radius: 16px;
    padding: 1.2rem;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden; /* 防止图片溢出圆角 */
}

/* 序号样式 */
.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 400;
    font-size: 0.95em;
    color: #999;
    margin-right: 1rem;
    flex-shrink: 0; /* 防止序号被压缩 */
    margin-top: 0; /* 对齐微调 */
}

/* 左侧：文字内容容器 */
.publication-content {
    flex: 1; /* 占据剩余空间 */
    min-width: 0;
    padding-right: 1.5rem; /* 给文字和图片之间留空隙 */
}

.publication-title {
    display: block;
    margin-bottom: 0.4rem;
    font-weight: 500; /* 标题稍微加重一点点区分度，也可改为400 */
    color: #333;
    line-height: 1.6;
}

.publication-authors, 
.publication-venue {
    display: block;
    line-height: 1.6;
    margin-bottom: 0.2rem;
    color: #555;
}

/* 右侧：图片容器 */
.publication-image-wrapper {
    width: 200px; /* 图片固定宽度 */
    height: 130px; /* 图片固定高度 */
    flex-shrink: 0; /* 防止被挤压 */
    border-radius: 8px;
    overflow: hidden;
    background-color: #f9f9f9; /* 图片加载前的背景色 */
    border: 1px solid #eee;
}

.publication-image {
    width: 100%;
    height: 100%;
    object-fit: cover; /* 保证图片填满容器且不变形（裁剪） */
    object-position: center;
    transition: transform 0.3s ease;
}

.publication-card:hover .publication-image {
    transform: scale(1.05); /* 鼠标悬停时图片微放大特效 */
}

/* =========================================
   3. Conference & Services (Logo + 文字)
   ========================================= */
.conference-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.conference-card {
    background: white;
    border-radius: 12px;
    padding: 0.6rem 1rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
    display: flex;
    align-items: center; /* 垂直居中 */
    gap: 0.8rem;
    font-size: 0.95em;
}

.conference-logo {
    width: 24px;  /* 小图标尺寸 */
    height: 24px;
    object-fit: contain;
}

/* =========================================
   4. Editorial & Reviewing (垂直卡片：上图下文)
   ========================================= */
.gallery-grid {
    display: grid;
    /* 自动适应宽度，最小宽度180px */
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); 
    gap: 1.5rem;
    margin-top: 1rem;
}

.gallery-card {
    background: #fff;
    border-radius: 12px;
    padding: 1.2rem;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: transform 0.2s ease;
}

.gallery-card:hover {
    transform: translateY(-3px);
}

.gallery-image {
    height: 100px; /* 期刊封面高度 */
    width: auto;
    max-width: 100%;
    object-fit: contain;
    margin-bottom: 1rem;
    border-radius: 4px;
}

.gallery-content {
    width: 100%;
}

.gallery-title {
    display: block;
    font-weight: 500;
    margin-bottom: 0.3rem;
    line-height: 1.4;
}

/* =========================================
   5. 移动端适配
   ========================================= */
@media (max-width: 768px) {
    /* Publications: 移动端改为垂直排列，图片在上方 */
    .publication-card {
        flex-direction: column-reverse; /* 文字在下，图片在上 */
        align-items: center;
    }

    .publication-card::before {
        align-self: flex-start; /* 序号回到左上角 */
        margin-bottom: 0.5rem;
    }

    .publication-content {
        padding-right: 0;
        width: 100%;
    }

    .publication-image-wrapper {
        width: 100%; /* 图片全宽 */
        height: 160px;
        margin-bottom: 1rem;
    }
}
</style>

<h2>Publications</h2>
<div class="publication-list">
    
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions.</span>
            <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.,*</span> <span class="auxiliary-text-inline">(*Corresponding author)</span></span>
            <span class="publication-venue"><em>Psychology of Popular Media</em> 2025</span>
            <a href="https://doi.org/10.1037/ppm0000636" class="publication-link" target="_blank">DOI Link</a>
        </div>
        <div class="publication-image-wrapper">
            <img src="https://placehold.co/400x260/e0e0e0/999?text=Research+Img+1" alt="Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Book Review: Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>AI & Society</em> 2025</span>
            <a href="https://doi.org/10.1007/s00146-025-02693-0" class="publication-link" target="_blank">DOI Link</a>
        </div>
        <div class="publication-image-wrapper">
            <img src="https://placehold.co/400x260/e0e0e0/999?text=Book+Review" alt="Book Cover" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">从"机事"到"机心"：与智能技术的深度意义交互及当代青年的数字生命观形成.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>新闻与传播研究</em> 2025</span>
        </div>
        <div class="publication-image-wrapper">
            <img src="https://placehold.co/400x260/e0e0e0/999?text=Chinese+Paper" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span>, Huang, Y.</span>
            <span class="publication-venue"><em>Emerging Media</em> 2025</span>
            <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank">DOI Link</a>
        </div>
        <div class="publication-image-wrapper">
             <img src="https://placehold.co/400x260/e0e0e0/999?text=Intimacy+Study" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders.</span>
            <span class="publication-authors">Mou, Y.+, <span class="my-name">Lan, J.+</span>, & Huang, Y., <span class="auxiliary-text-inline">(+Co-first author)</span></span>
            <span class="publication-venue"><em>New Media & Society</em> 2023</span>
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank">DOI Link</a>
        </div>
        <div class="publication-image-wrapper">
             <img src="https://placehold.co/400x260/e0e0e0/999?text=Data+Mining" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">机器写作中的性别刻板印象: 基于实验研究的实然探讨.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>中国网络传播研究</em> 2023</span>
        </div>
        <div class="publication-image-wrapper">
             <img src="https://placehold.co/400x260/e0e0e0/999?text=AI+Writing" alt="Research Visualization" class="publication-image">
        </div>
    </div>
</div>

<h2>Conference Presentations</h2>
<div class="conference-grid">
    <div class="conference-card">
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <span>NCA 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/4S.png" class="conference-logo">
        <span>4S 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/AEJMC.jpeg" class="conference-logo">
        <span>AEJMC 2025 🏆</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/IAMCR1.png" class="conference-logo">
        <span>IAMCR 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo">
        <span>ICA 2025</span>
    </div>
        <div class="conference-card">
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <span>NCA 2024</span>
    </div>
        <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo">
        <span>ICA 2024</span>
    </div>
        <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo">
        <span>ICA 2023</span>
    </div>
    </div>

<h2>Services</h2>
<div class="conference-grid">
    <div class="conference-card" style="width: auto;"> <img src="https://placehold.co/50/e0e0e0/333?text=AC" class="conference-logo">
        <div>
            <strong>Student Committee Chair</strong>
            <div style="font-size:0.85em; color:#888;">Assoc. for Chinese Comm. Studies</div>
        </div>
    </div>
    <div class="conference-card" style="width: auto;">
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <div>
            <strong>Grad. Student Rep.</strong>
            <div style="font-size:0.85em; color:#888;">Comm. & Future Division, NCA</div>
        </div>
    </div>
</div>

<h2>Editorial Duties</h2>
<div class="gallery-grid">
    <div class="gallery-card">
        <img src="/images/logo/BDS.png" class="gallery-image">
        <div class="gallery-content">
            <span class="gallery-title">Assistant Editor</span>
            <span class="auxiliary-text">Big Data & Society</span>
        </div>
    </div>
    <div class="gallery-card">
        <img src="/images/logo/EMM.jpg" class="gallery-image">
        <div class="gallery-content">
            <span class="gallery-title">Editorial Assistant</span>
            <span class="auxiliary-text">Emerging Media</span>
        </div>
    </div>
</div>

<h2>Academic Reviewing</h2>
<div class="gallery-grid">
    <div class="gallery-card">
        <img src="/images/logo/NMS.png" class="gallery-image">
        <div class="gallery-content">
            <span class="gallery-title">New Media & Society</span>
        </div>
    </div>
    <div class="gallery-card">
        <img src="https://placehold.co/150x200/e0e0e0/333?text=PPM" class="gallery-image">
        <div class="gallery-content">
            <span class="gallery-title">Psychology of Popular Media</span>
        </div>
    </div>
    <div class="gallery-card">
        <img src="/images/logo/AISco.png" class="gallery-image">
        <div class="gallery-content">
            <span class="gallery-title">AI & Society</span>
        </div>
    </div>
</div>
