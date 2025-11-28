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
    font-weight: 500; /* 标题保持极轻微的区分度，如果想完全不加粗可改为400 */
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
    /* 设置一个最大宽高度，让图片在里面自适应 */
    width: 300px;  
    height: 180px; 
    flex-shrink: 0;
    /* 去掉边框和背景色，让不同比例的图片自然悬浮 */
    background-color: #fff;
    display: flex;
    align-items: flex-start; /* 图片顶部对齐 */
    justify-content: flex-end; /* 图片靠右对齐 */
}

.publication-image {
    width: 100%;
    height: 100%;
    /* 关键修改：contain 确保图片完整显示，不裁剪 */
    object-fit: contain; 
    object-position: right top; /* 图片靠右上方显示 */
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

/* 去除服务部分可能存在的加粗 */
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
    /* 减小最小宽度(220->160)，让卡片变小 */
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

/* 图片包裹层：高度减小，背景改白 */
.gallery-image-wrapper {
    width: 100%;
    height: 200px; /* 高度减小 (原280px)，显得更精致 */
    background-color: #fff; /* 改为白色背景，避免未填满时显示灰色 */
    position: relative;
    padding-top: 1rem; /* 给顶部一点呼吸空间 */
}

.gallery-image {
    width: 100%;
    height: 100%;
    /* 关键修改：contain 确保期刊封面完整显示 */
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
    /* 去除加粗 */
    font-weight: 400; 
    margin-bottom: 0.2rem;
    line-height: 1.4;
    color: #333;
}

/* =========================================
   5. 移动端适配
   ========================================= */
@media (max-width: 768px) {
    /* Publications: 移动端改为垂直排列 */
    .publication-card {
        flex-direction: column-reverse;
        align-items: center;
        padding: 1.2rem;
    }

    .publication-card::before {
        align-self: flex-start;
        margin-bottom: 0.5rem;
    }

    .publication-content {
        padding-right: 0;
        width: 100%;
    }

    .publication-image-wrapper {
        width: 100%; 
        height: auto; /* 高度自适应 */
        max-height: 200px;
        margin-bottom: 1.2rem;
        justify-content: center; /* 移动端居中 */
    }
    
    .publication-image {
        object-position: center;
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
<div class="publication-list">
    
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions.</span>
            <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.,*</span> <span class="auxiliary-text-inline">(*Corresponding author)</span></span>
            <span class="publication-venue"><em>Psychology of Popular Media</em> 2025</span>
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
            <span class="publication-venue"><em>AI & Society</em> 2025</span>
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
            <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank">Access</a>
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
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank">Access</a>
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
    <div class="conference-card" style="width: auto;"> 
        <img src="/images/logo/ACCS.png" class="conference-logo">
        <div>
            <span>Student Committee Chair</span>
            <div style="font-size:0.85em; color:#888;">Association for Chinese Communication Studies</div>
        </div>
    </div>
    <div class="conference-card" style="width: auto;">
        <img src="/images/logo/NCA.jpeg" class="conference-logo">
        <div>
            <span>Graduate Student Representative</span>
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
            <span class="gallery-title">Assistant Editor</span>
            <span class="auxiliary-text">Big Data & Society</span>
        </div>
    </div>
    <div class="gallery-card">
        <div class="gallery-image-wrapper">
            <img src="/images/logo/EMM.jpg" class="gallery-image">
        </div>
        <div class="gallery-content">
            <span class="gallery-title">Editorial Assistant</span>
            <span class="auxiliary-text">Emerging Media</span>
        </div>
    </div>
</div>

<h2>Academic Reviewing</h2>
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
</div>
