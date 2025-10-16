---
title: ""
permalink: /academia/
author_profile: true
---

<style>


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

/* 内容文字微调 */
.publication-content {
    flex: 1;
    min-width: 0;
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
    font-size: 0.95em;
    font-weight: 400;
}

/* 链接样式 */
.publication-link {
    display: block;
    margin-top: 0.4rem;
    color: #999;
    font-size: 0.9em;
    text-decoration: none;
    transition: color 0.2s ease;
}

.publication-link:hover {
    color: #666;
    text-decoration: underline;
}

/* 作者高亮 */
.my-name {
    color: #002FA7;
    font-weight: 400;
}

/* 小标题美化 */
h2 {
    font-weight: 400;
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
    font-weight: 400;
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

 .quote-style {
  font-family: 'Times New Roman', serif;
  font-style: italic;
  color: #002fa7; /* 克莱因蓝 */
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
            Huang, Y., <span class="my-name">Lan, J.*</span> (2025). Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions. <em>Psychology of Popular Media</em>. Advance online publication. (*Corresponding author)
            <a href="https://doi.org/10.1037/ppm0000636" class="publication-link" target="_blank">https://doi.org/10.1037/ppm0000636</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2025). 从"机事"到"机心"：与智能技术的深度意义交互及当代青年的数字生命观形成. <em>新闻与传播研究, 32</em>(6), 17-29.
            <a href="https://link.cnki.net/doi/CNKI:SUN:YANJ.0.2025-06-002" class="publication-link" target="_blank">https://link.cnki.net/doi/CNKI:SUN:YANJ.0.2025-06-002</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="my-name">Lan, J.</span>, Huang, Y. (2025). Performing Intimacy: Curating the Self-presentation in Human–AI Relationships. <em>Emerging Media, 3</em>(2), 305-317.
              <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank">https://doi.org/10.1177/27523543251334157</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            Mou, Y., <span class="my-name">Lan, J.</span>, & Huang, Y. (2023). Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach. <em>New Media & Society, 27</em>(5), 2684-2702. (Co-first author with Mou Y.)
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank">https://doi.org/10.1177/14614448231212822</a>
        </div>
    </div>
</div>

<h2>Book Reviews</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
         <span class="my-name">Lan, J.</span> (2025). Book Review: Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond. <em>AI & Society</em>. (Accepted)
        </div>
    </div>
    </div>

<h2>Book Chapters</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2023). 机器写作中的性别刻板印象: 基于实验研究的实然探讨. <em>中国网络传播研究, 1</em>(1), 236-266.
             <a href="https://link.cnki.net/doi/CNKI:SUN:ZWCY.0.2023-01-011" class="publication-link" target="_blank">https://link.cnki.net/doi/CNKI:SUN:ZWCY.0.2023-01-011</a>
        </div>
    </div>
    </div>


<h2>Preprints</h2>
<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            Mou, Y., <span class="my-name">Lan, J.</span>*, Lu, J., Wang, J. (2025). Emerging Media Use and Acceptance of Digital Immortality: A Cluster Analysis among Chinese Young Generations. <em>arXiv preprint arXiv:2505.01355.</em>(*Corresponding author)
            <a href="https://doi.org/10.48550/arXiv.2505.01355" class="publication-link" target="_blank">https://doi.org/10.48550/arXiv.2505.01355</a>
        </div>
    </div>
    <div class="publication-card">
        <div class="publication-content">
            <span class="my-name">Lan, J.</span>, Huang, Y. (2025). Between Filters and Feeds: Investigating Douyin and WeChat's Influence on Chinese Adolescent Body Image. <em>arXiv preprint arXiv:2507.17755.</em>
            <a href="https://doi.org/10.48550/arXiv.2507.17755" class="publication-link" target="_blank">https://doi.org/10.48550/arXiv.2507.17755</a>
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

<h2>Professional Training</h2>
<div class="conference-grid">
    <div class="conference-card">Summer Institute in Computational Social Science—Singapore 2024</div>
</div>
