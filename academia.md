---
title: ""
permalink: /academia/
author_profile: true
---

<style>
/* 1. 全局字体和布局 */
.page__inner-wrap {
    max-width: 1600px !important;
}

/* 通用字体微调，营造精致感 */
body {
    font-size: 0.95em;
    line-height: 1.75;
    font-weight: 400;
}

/* 链接/DOI的灰色，用于弱化辅助信息 */
.publication-link, 
.auxiliary-text {
    color: #999;
    font-size: 0.9em;
    text-decoration: none;
    transition: color 0.2s ease;
    display: block;
    margin-top: 0.2rem;
    line-height: 1.6;
}

.publication-link:hover {
    color: #666;
    text-decoration: underline;
}

/* 2. 小标题美化：取消加粗，保持正常字重 */
h2 {
    font-weight: 400; 
    font-size: 1.1em;
    margin-top: 2rem;
}

/* 3. 列表通用样式 */
.publication-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    counter-reset: pub-counter;
    margin-top: 1rem;
}

/* 卡片样式优化 */
.publication-card {
    display: flex;
    align-items: flex-start;
    gap: 1em;
    background: #fff;
    border: none;
    border-radius: 16px;
    padding: 0.8rem 1.2rem;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    line-height: 1.75;
    flex-wrap: wrap;
}

/* 编号样式 */
.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 400;
    font-size: 0.95em;
    color: #333;
    min-width: 2em;
    text-align: right;
}

/* 内容文字微调：确保内容主体不加粗 */
.publication-content {
    flex: 1;
    min-width: 0;
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
    font-size: 0.95em;
    font-weight: 400;
}

/* 新增：论文标题样式 */
.publication-title {
    display: block;
    margin-bottom: 0.3rem;
    line-height: 1.75;
}

/* 新增：作者行样式 */
.publication-authors {
    display: block;
    line-height: 1.75;
    margin-bottom: 0.3rem;
}

/* 新增：期刊信息行样式 */
.publication-venue {
    display: block;
    line-height: 1.75;
}

/* 作者高亮：保持原有样式 */
.my-name {
    color: #002FA7;
    font-weight: 400;
}

/* 新增：inline 辅助文本样式（用于通讯作者和共同一作标记）*/
.auxiliary-text-inline {
    color: #999;
    font-size: 0.9em;
}

/* 4. Conference/Review 卡片样式：确保内容不加粗 */
.conference-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
}

.conference-card {
    background: white;
    border: none;
    border-radius: 12px;
    padding: 0.5rem 1rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
    font-weight: 400;
    font-size: 0.95em;
    line-height: 1.6;
}

/* 5. 无编号列表 */
.no-counter-list {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1rem;
}

/* 无编号卡片样式 */
.no-counter-card {
    background: #fff;
    border: none;
    border-radius: 16px;
    padding: 0.8rem 1.2rem;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    line-height: 1.75;
    width: auto; 
    display: block; 
}

/* 无编号内容 */
.no-counter-content {
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
    font-size: 0.95em;
    font-weight: 400;
}

/* 第一行/主标题样式：取消加粗，恢复正常字重 */
.no-counter-content .first-line {
    font-weight: 400;
    display: block;
    line-height: 1.75;
}

/* 6. 移动端优化 */
@media (max-width: 768px) {
    .publication-card {
        padding: 1rem;
    }

    .conference-card {
        font-size: 0.85em;
    }
    
    .no-counter-card {
        padding: 1rem;
    }
}

.quote-style {
    font-family: 'Times New Roman', serif;
    font-style: italic;
    color: #002fa7;
    text-align: center;
    font-size: 0.95em;
    margin-top: 1.5rem;
}
</style>

<div class="quote-style">
    <em>「Être sur des charbons ardents」</em>
</div>

<h2>Journal Articles</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions.</span>
            <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.,*</span> <span class="auxiliary-text-inline">(*Corresponding author)</span></span>
            <span class="publication-venue"><em>Psychology of Popular Media</em>. 2025. Advance online publication.</span>
            <a href="https://doi.org/10.1037/ppm0000636" class="publication-link" target="_blank">https://doi.org/10.1037/ppm0000636</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">从"机事"到"机心"：与智能技术的深度意义交互及当代青年的数字生命观形成.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>新闻与传播研究</em>. 2025, 32(6): 17-29.</span>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span>, Huang, Y.</span>
            <span class="publication-venue"><em>Emerging Media</em>. 2025, 3(2): 305-317.</span>
            <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank">https://doi.org/10.1177/27523543251334157</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach.</span>
            <span class="publication-authors">Mou, Y., <span class="my-name">Lan, J.</span>, & Huang, Y., <span class="auxiliary-text-inline">(Co-first author with Mou Y.)</span></span>
            <span class="publication-venue"><em>New Media & Society</em>. 2023, 27(5): 2684-2702.</span>
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank">https://doi.org/10.1177/14614448231212822</a>
        </div>
    </div>
</div>

<h2>Book Reviews</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>AI & Society</em>. 2025. Advance online publication.</span>
            <a href="https://doi.org/10.1007/s00146-025-02693-0" class="publication-link" target="_blank">https://doi.org/10.1007/s00146-025-02693-0</a>
        </div>
    </div>
</div>

<h2>Book Chapters</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">机器写作中的性别刻板印象: 基于实验研究的实然探讨.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>中国网络传播研究</em>. 2023, 1(1): 236-266.</span>
        </div>
    </div>
</div>

<h2>Preprints</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Emerging Media Use and Acceptance of Digital Immortality: A Cluster Analysis among Chinese Young Generations.</span>
            <span class="publication-authors">Mou, Y., <span class="my-name">Lan, J.</span>*, Lu, J., Wang, J., <span class="auxiliary-text-inline">(*Corresponding author)</span></span>
            <span class="publication-venue"><em>arXiv preprint arXiv:2505.01355.</em> 2025.</span>
            <a href="https://doi.org/10.48550/arXiv.2505.01355" class="publication-link" target="_blank">https://doi.org/10.48550/arXiv.2505.01355</a>
        </div>
    </div>
</div>

<h2>Conference Presentations</h2>
<div class="conference-grid">
    <div class="conference-card">NCA 2025</div>
    <div class="conference-card">4S 2025</div>
    <div class="conference-card">AEJMC 2025 🏆</div>
    <div class="conference-card">IAMCR 2025</div>
    <div class="conference-card">ICA 2025</div>
    <div class="conference-card">NCA 2024</div>
    <div class="conference-card">ICA 2024</div>
    <div class="conference-card">ICA 2023</div>
</div>

<h2>Services</h2>
<div class="no-counter-list">
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Student Committee Chair (2024-2026)</span>
            <span class="auxiliary-text">Association for Chinese Communication Studies</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Graduate Student Representative (2024-2025)</span>
            <span class="auxiliary-text">Communication and the Future Division, at NCA</span>
        </div>
    </div>
</div>

<h2>Editorial Duties</h2>
<div class="no-counter-list">
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Assistant Editor</span>
            <span class="auxiliary-text">Big Data & Society (Jan. 2024 - present)</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Editorial Assistant</span>
            <span class="auxiliary-text">Emerging Media (Jan. 2024 - May 2025)</span>
        </div>
    </div>
</div>

<h2>Peer Review for Journal</h2>
<div class="conference-grid">
    <div class="conference-card">New Media & Society</div>
    <div class="conference-card">Psychology of Popular Media</div>
    <div class="conference-card">AI & Society</div>
    <div class="conference-card">Emerging Media</div>
</div>

<h2>Peer Review for Conference</h2>
<div class="conference-grid">
    <div class="conference-card">International Communication Association</div>
    <div class="conference-card">National Communication Association</div>
    <div class="conference-card">Association for Education in Journalism and Mass Communication</div>
    <div class="conference-card">International Association for Media and Communication Research</div>
    <div class="conference-card">The Network for the Public Communication of Science and Technology</div>
    <div class="conference-card">Association for Information Systems</div>
    <div class="conference-card">The Korean American Communication Association</div>
</div>

<h2>Research Assistant</h2>
<div class="no-counter-list">
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Shanghai Jiao Tong University</span>
            <span class="auxiliary-text">Advised by Dr.Yi Mou (Sep. 2021 - present)</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Utrecht University (Online)</span>
            <span class="auxiliary-text">Advised by Dr.Jing Zeng (Jan. 2023 - Jan. 2024)</span>
        </div>
    </div>
</div>

<h2>Teaching Assistant</h2>
<div class="no-counter-list">
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">New Media and Technological Culture</span>
            <span class="auxiliary-text">2025 Fall, Fang Wu, Undergraduate Level</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Quantitative Research Method (JC6504)</span>
            <span class="auxiliary-text">2024 Fall, Yi Mou, Doctoral level</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Human-Machine Communication (JC8209)</span>
            <span class="auxiliary-text">2023/2025 Spring, Yi Mou, Master level</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Qualitative Research Method (JC6012)</span>
            <span class="auxiliary-text">2023 Fall, Fang Wu/Xueqing Li, Master level</span>
        </div>
    </div>
    <div class="no-counter-card">
        <div class="no-counter-content">
            <span class="first-line">Introduction to New Media (JC3163)</span>
            <span class="auxiliary-text">2023/2024 Spring, Yi Mou, Undergraduate Level</span>
        </div>
    </div>
</div>

<h2>Professional Training</h2>
<div class="conference-grid">
    <div class="conference-card">Summer Institute in Computational Social Science—Singapore 2024</div>
</div>
