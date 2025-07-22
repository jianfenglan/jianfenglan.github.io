---
title: ""
permalink: /researches/
author_profile: true
---

<style>
.page__inner-wrap {
    max-width: 1600px !important;
}

.publication-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    counter-reset: pub-counter;
    margin-top: 1rem;
}

.publication-card {
    display: flex;
    align-items: flex-start;
    gap: 1em;
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    /* transition and cursor removed to make it static */
    line-height: 1.6;
    flex-wrap: wrap;
}

/*
.publication-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}
*/

.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 200;
    font-size: 1.1em;
    color: #333;
    min-width: 2em;
    text-align: right;
}

.publication-content {
    flex: 1;
    min-width: 0;
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
}

.my-name {
    color: #002FA7;
    font-weight: 200;
}

.conference-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
}

.conference-card {
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 8px;
    padding: 0.4rem 0.9rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    font-weight: 300;
    font-size: 0.95em;
    line-height: 1.5;
}


/* --- Hiding the modal pop-up styles as they are no longer used --- */
/*
.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    inset: 0;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(6px);
    justify-content: center;
    padding: 6rem 1rem;
}

.modal-content {
    background: #fff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    max-width: 600px;
    width: 90%;
    transform: scale(0.9);
    transition: transform 0.3s ease;
    position: relative;
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
    max-height: calc(100vh - 12rem);
    overflow-y: auto;
    margin: auto 0;
}

.modal-content h2 {
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
    color: #333;
}
*/

h2 {
    font-weight: 200;
}

@media (max-width: 768px) {
    .modal-overlay {
        padding: 7rem 1rem;
    }
    .modal-content {
        max-height: calc(100vh - 14rem);
    }
}
</style>

<h2>Journal Articles</h2>
<div class="publication-list">
    <div class="publication-card" data-detail="...details hidden...">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2025). 从“机事”到“机心”：与智能技术的深度意义交互及当代青年的数字生命观形成. <em>新闻与传播研究, 32</em>(6), 17-29.
        </div>
    </div>
    <div class="publication-card" data-detail="...details hidden...">
        <div class="publication-content">
            <span class="my-name">Lan, J.</span>, Huang, Y. (2025). Performing Intimacy: Curating the Self-presentation in Human–AI Relationships. <em>Emerging Media, 3</em>(2), 305-317.
        </div>
    </div>
    <div class="publication-card" data-detail="...details hidden...">
        <div class="publication-content">
            Mou, Y.*, <span class="my-name">Lan, J.</span>*, & Huang, Y. (2023). Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach. <em>New Media & Society, 27</em>(5), 2684-2702. (*co-first author)
        </div>
    </div>
    <div class="publication-card" data-detail="...details hidden...">
        <div class="publication-content">
            牟怡, <span class="my-name">蓝剑锋</span>. (2023). 机器写作中的性别刻板印象: 基于实验研究的实然探讨. <em>中国网络传播研究, 1</em>(1), 236-266.
        </div>
    </div>
</div>

<h2>Preprints</h2>
<div class="publication-list">
    <div class="publication-card" data-detail="...details hidden...">
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
