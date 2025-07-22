---
title: ""
permalink: /researches/
author_profile: true
---

<style>
/* 为引言添加的古典样式 */
.epigraph {
  text-align: center; /* 居中对齐 */
  margin-bottom: 2.5rem; /* 与下方标题的间距 */
  font-family: 'Times New Roman', Times, serif; /* 使用 Times New Roman 字体 */
  font-style: italic; /* 斜体 */
  font-weight: 200; /* 使用更细的字重 */
  color: #555; /* 使用深灰色，比纯黑更柔和 */
}

.page__inner-wrap {
    max-width: 1600px !important;
}

/* 通用字体微调，营造精致感 */
body {
    font-size: 0.95em;
    line-height: 1.75;
}

/* 列表网格 */
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
    padding: 0.8rem 1.2rem; /* <-- 修改这里，减小了上下和左右的内边距 */
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
    line-height: 1.75;
    flex-wrap: wrap;
}

/* 编号样式 */
.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 200;
    font-size: 0.95em;
    color: #333;
    min-width: 2em;
    text-align: right;
}

/* 内容文字微调 */
.publication-content {
    flex: 1;
    min-width: 0;
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
    font-size: 0.95em;
    font-weight: 300;
}

/* 作者高亮 */
.my-name {
    color: #002FA7;
    font-weight: 300;
}

/* 小标题美化 */
h2 {
    font-weight: 200;
    font-size: 1.1em;
    margin-top: 2rem;
}

/* Conference 卡片样式 */
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
    font-weight: 300;
    font-size: 0.95em;
    line-height: 1.6;
}

/* 移动端优化 */
@media (max-width: 768px) {
    .publication-card {
        padding: 1rem;
    }

    .conference-card {
        font-size: 0.85em;
    }
}
</style>

<p class="epigraph">“The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice.”</p>

<h2>Journal Articles</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2025). 从“机事”到“机心”：与智能技术的深度意义交互及当代青年的数字生命观形成. <em>新闻与传播研究, 32</em>(6), 17-29.
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="my-name">Lan, J.</span>, Huang, Y. (2025). Performing Intimacy: Curating the Self-presentation in Human–AI Relationships. <em>Emerging Media, 3</em>(2), 305-317.
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            Mou, Y.*, <span class="my-name">Lan, J.</span>*, & Huang, Y. (2023). Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach. <em>New Media & Society, 27</em>(5), 2684-2702. (*co-first author)
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2023). 机器写作中的性别刻板印象: 基于实验研究的实然探讨. <em>中国网络传播研究, 1</em>(1), 236-266.
        </div>
    </div>
</div>

<h2>Preprints</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            Mou, Y., <span class="my-name">Lan, J.</span>*, Lu, J., Wang, J. (2025). Emerging Media Use and Acceptance of Digital Immortality: A Cluster Analysis among Chinese Young Generations. <em>arXiv preprint arXiv:2505.01355.</em>（*Corresponding author）
        </div>
    </div>
</div>

<h2>Conference Presentations</h2>
<div class="conference-grid">
    <div class="conference-card">111th NCA</div>
    <div class="conference-card">JSF-PCST Tokyo</div>
    <div class="conference-card">4S 2025</div>
    <div class="conference-card">108th AEJMC</div>
    <div class="conference-card">IAMCR 2025</div>
    <div class="conference-card">75th ICA</div>
    <div class="conference-card">PCST-Suzhou 2024</div>
    <div class="conference-card">110th NCA</div>
    <div class="conference-card">第五届公共传播学术论坛</div>
    <div class="conference-card">74th ICA</div>
    <div class="conference-card">21st CIRC</div>
    <div class="conference-card">SICSS-Singapore 2024</div>
    <div class="conference-card">重庆大学首届“弘毅学术论坛”</div>
    <div class="conference-card">Mobile Studies Congress 2023</div>
    <div class="conference-card">73rd ICA</div>
    <div class="conference-card">2022 SJTU-ICA Forum</div>
</div>
