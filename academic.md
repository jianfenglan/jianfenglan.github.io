---
title: ""
permalink: /academic/
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
    display: inline-block;
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
    margin-top: 3rem; 
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 0.5rem;
}

/* 新增：图例说明样式 */
.publication-legend {
    color: #999;
    font-size: 0.9em;
    margin-top: -1rem;      /* 拉近与上方标题的距离 */
    margin-bottom: 1.5rem;  /* 与下方列表保持距离 */
    line-height: 1.5;
}

/* 优化上标样式 */
sup {
    vertical-align: super;
    font-size: smaller;
    line-height: 0;
}

.my-name {
    color: #002FA7;
    font-weight: 400;
}

/* =========================================
   2. Publications (左文右图 - 完整显示版)
   ========================================= */
.publication-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    counter-reset: pub-counter;
}

.publication-card {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    background: #fff;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
}

/* 序号样式 */
.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 400;
    font-size: 0.95em;
    color: #999;
    margin-right: 1.2rem;
    flex-shrink: 0;
    margin-top: 0;
}

/* 左侧：文字内容容器 */
.publication-content {
    flex: 1;
    min-width: 0;
    padding-right: 2rem; 
}

.publication-title {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 400; 
    color: #333;
    line-height: 1.6;
    font-size: 1.05em;
}

.publication-authors, 
.publication-venue {
    display: block;
    line-height: 1.6;
    margin-bottom: 0.3rem;
    color: #555;
}

/* 右侧：图片容器 - 调整为完整显示 */
.publication-image-wrapper {
    width: 300px;  
    height: 180px; 
    flex-shrink: 0;
    background-color: #fff;
    display: flex;
    align-items: flex-start; 
    justify-content: flex-end; 
}

.publication-image {
    width: 100%;
    height: 100%;
    object-fit: contain; 
    object-position: right top; 
    transition: transform 0.3s ease;
}

.publication-card:hover .publication-image {
    transform: scale(1.02);
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
    align-items: center;
    gap: 0.8rem;
    font-size: 0.95em;
    border: 1px solid transparent;
    transition: all 0.2s ease;
}

.conference-card:hover {
    border-color: #eee;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08);
}

.conference-logo {
    width: 28px;
    height: 28px;
    object-fit: contain;
}

/* 去除可能存在的加粗 */
.conference-card span, 
.conference-card div,
.conference-card strong {
    font-weight: 400 !important;
}

/* =========================================
   4. Editorial & Reviewing (精致小卡片模式)
   ========================================= */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); 
    gap: 1.5rem;
    margin-top: 1rem;
}

.gallery-card {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.gallery-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
}

/* 图片包裹层 */
.gallery-image-wrapper {
    width: 100%;
    height: 200px; 
    background-color: #fff; 
    position: relative;
    padding-top: 1rem; 
}

.gallery-image {
    width: 100%;
    height: 100%;
    object-fit: contain; 
    object-position: center;
    display: block;
}

/* 文字内容区域 */
.gallery-content {
    padding: 1rem;
    text-align: center;
    background: #fff;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.gallery-title {
    display: block;
    font-weight: 400; 
    margin-bottom: 0.2rem;
    line-height: 1.4;
    color: #333;
}

/* =========================================
   5. 移动端适配 (核心修复)
   ========================================= */
@media (max-width: 768px) {
    /* Publications: 移动端修复 */
    .publication-card {
        /* 1. 改为 column (正向)，保证 序号->文字->图片 的顺序 */
        flex-direction: column; 
        align-items: flex-start; /* 左对齐 */
        padding: 1.2rem;
        position: relative; /* 为序号定位做准备 */
    }

    .publication-card::before {
        /* 2. 序号样式调整：不需要单独占一行，紧凑一点 */
        margin-right: 0;
        margin-bottom: 0.5rem;
        font-weight: 500;
        color: #002FA7; /* 移动端给序号加点颜色突出一下 */
    }

    .publication-content {
        padding-right: 0;
        width: 100%;
        margin-bottom: 1rem; /* 3. 文字和下方图片增加间距 */
    }

    .publication-image-wrapper {
        width: 100%; 
        height: auto; 
        max-height: 220px; /* 限制最大高度，防止竖图太占地 */
        justify-content: center; /* 移动端图片居中 */
        align-items: center;
    }
    
    .publication-image {
        object-position: center; /* 移动端图片居中显示 */
    }
    
    /* Editorial: 移动端适配 */
    .gallery-grid {
         grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
         gap: 1rem;
    }
    
    .gallery-image-wrapper {
        height: 180px; 
    }
}
</style>

<h2>Publications</h2>

<div class="publication-legend">
    * = Corresponding author<br>
    + = Co-first author<br>
   Illustrations generated by Gemini 3.1 Pro Nano Banana
</div>

<div class="publication-list">

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Empowering Civic Engagement in AI Governance: A Two-wave Panel Study on AI Literacy and Participatory Governance of Generative AI in China.</span>
            <span class="publication-authors">Lin, Z., Jin, Q, <span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>Telecommunications Policy</em>, 2026.</span>
             <a href="https://doi.org/10.1016/j.telpol.2026.103190" class="publication-link" target="_blank">Access</a>
        </div>
        <div class="publication-image-wrapper">
            <img src="/images/logo/forTele.png" alt="Visualization" class="publication-image">
        </div>
    </div>
    
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">人、物、机器：重思“机器问题”与机器人权利——专访大卫·贡克尔.</span>
            <span class="publication-authors"><span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>国际新闻界</em>, 2026.</span>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forGJXWJ.png" alt="Research Visualization" class="publication-image">
        </div>
    </div>
    
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions.</span>
            <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.*</span></span>
            <span class="publication-venue"><em>Psychology of Popular Media</em>, 2025.</span>
            <a href="https://doi.org/10.1037/ppm0000636" class="publication-link" target="_blank">Access</a>
        </div>
        <div class="publication-image-wrapper">
            <img src="/images/logo/forPPM.png" alt="Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Book Review: Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>AI & Society</em>, 2025.</span>
            <a href="https://doi.org/10.1007/s00146-025-02693-0" class="publication-link" target="_blank">Access</a>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forAISco.png" alt="Book Cover" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">从"机事"到"机心"：与智能技术的深度意义交互及当代青年的数字生命观形成.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>新闻与传播研究</em>, 2025.</span>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forXWCBYJ.png" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span>, Huang, Y.</span>
            <span class="publication-venue"><em>Emerging Media</em>, 2025.</span>
            <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank">Access</a>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forEMM.png" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders.</span>
            <span class="publication-authors">Mou, Y.<sup>+</sup>, <span class="my-name">Lan, J.<sup>+</sup></span>, & Huang, Y.</span>
            <span class="publication-venue"><em>New Media & Society</em>, 2023.</span>
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank">Access</a>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forNMS.png" alt="Research Visualization" class="publication-image">
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">机器写作中的性别刻板印象: 基于实验研究的实然探讨.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>中国网络传播研究</em>, 2023.</span>
        </div>
        <div class="publication-image-wrapper">
             <img src="/images/logo/forZGWLCB.png" alt="Research Visualization" class="publication-image">
        </div>
    </div>
</div>

<h2>Conference Presentations</h2>
<div class="conference-grid">
   <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo">
        <span>ICA 2026</span>
    </div>
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
    <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/ACCS.png" class="conference-logo">
        <div>
            <span>Student Committee Chair (2024-2026)</span>
            <div style="font-size:0.85em; color:#888;">Association for Chinese Communication Studies</div>
        </div>
    </div>
    <div class="conference-card" style="width: auto;">
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <div>
            <span>Graduate Student Representative (2024-2025)</span>
            <div style="font-size:0.85em; color:#888;">Communication and the Future Division, NCA</div>
        </div>
    </div>
</div>

<h2>Editorial Duties</h2>
<div class="gallery-grid">
    <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/BDS.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">Big Data & Society</span>
            <span class="auxiliary-text">Assistant Editor<br>(2024-current)</span>
        </div>
    </div>
    <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/EMM.jpg" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">Emerging Media</span>
            <span class="auxiliary-text">Editorial Assistant<br>(2023-2025)</span>
        </div>
    </div>
</div>

<h2>Journal Review</h2>
<div class="gallery-grid">
   <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/NMS.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">New Media & Society</span>
        </div>
    </div>
    <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/PPM.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">Psychology of Popular Media</span>
        </div>
    </div>
    <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/AISco.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">AI & Society</span>
        </div>
    </div>
     <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/IJHCI.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">International Journal of Human-Computer Interaction</span>
        </div>
    </div>  
      <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/FIP.png" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">Frontiers in Psychology</span>
        </div>
    </div>
</div>

<h2>Conference Review</h2>
<div class="conference-grid">
    <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/ICA.png" class="conference-logo">
        <div>
            <span>International Communication Association</span>
        </div>
    </div>
      <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <div>
            <span>National Communication Association</span>
        </div>
    </div>
      <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/AEJMC.jpeg" class="conference-logo">
        <div>
            <span>The Association for Education in Journalism and Mass Communication</span>
        </div>
    </div>
     <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/IAMCR1.png" class="conference-logo">
        <div>
            <span>International Association for Media and Communication Research</span>
        </div>
    </div>
         <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/AIS.png" class="conference-logo">
        <div>
            <span>Association for Information Systems</span>
        </div>
    </div>
 <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/KACA.png" class="conference-logo">
        <div>
            <span>Korean American Communication Association</span>
        </div>
    </div>
</div>
