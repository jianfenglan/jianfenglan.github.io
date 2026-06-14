---
title: ""
permalink: /research/
author_profile: true
---

<style>
.page__inner-wrap {
    max-width: 1120px !important;
}

body {
    font-size: 0.95em;
    line-height: 1.75;
    font-weight: 400;
    color: #2f3337;
}

:root {
    --blue: #002FA7;
    --text: #2f3337;
    --muted: #6f7680;
    --line: #e7ebf2;
}

h2 {
    margin-top: 3.2rem;
    margin-bottom: 1.1rem;
    padding-bottom: 0.65rem;
    border-bottom: 1px solid var(--line);
    color: #222;
    font-size: 1rem;
    font-weight: 560;
    letter-spacing: 0.035em;
    text-transform: uppercase;
}

sup {
    vertical-align: super;
    font-size: 0.72em;
    line-height: 0;
}

.my-name {
    color: var(--blue);
    font-weight: 560;
}

/* Publications */
.publication-legend,
.publication-link {
    color: var(--muted);
    font-size: 0.9em;
}

.publication-legend {
    margin-top: -0.45rem;
    margin-bottom: 1.2rem;
    line-height: 1.55;
}

.publication-list {
    display: grid;
    gap: 0.85rem;
    counter-reset: pub-counter;
}

.publication-card {
    display: grid;
    grid-template-columns: 2.35rem minmax(0, 1fr);
    column-gap: 1rem;
    align-items: flex-start;
    position: relative;
    padding: 1.05rem 1.15rem;
    border: 1px solid var(--line);
    border-radius: 14px;
    background: #fff;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);
    transition: border-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
}

.publication-card:hover {
    border-color: #d8dee8;
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.06);
    transform: translateY(-1px);
}

.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter, decimal-leading-zero);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.15rem;
    height: 2.15rem;
    border: 1px solid #dfe3eb;
    border-radius: 999px;
    background: #fff;
    color: var(--blue);
    font-size: 0.72em;
    font-weight: 560;
    letter-spacing: 0.04em;
}

.publication-content {
    min-width: 0;
}

.publication-title,
.publication-authors,
.publication-venue {
    display: block;
}

.publication-title {
    margin-bottom: 0.32rem;
    color: #202327;
    font-size: 1.01em;
    font-weight: 560;
    line-height: 1.48;
}

.publication-authors,
.publication-venue {
    color: #525a64;
    font-size: 0.95em;
    line-height: 1.55;
}

.publication-venue em {
    color: #30343a;
    font-style: italic;
}

.publication-link {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    margin-top: 0.45rem;
    padding: 0.16rem 0.58rem;
    border: 1px solid #e5eaf2;
    border-radius: 999px;
    background: #fff;
    color: #69717d;
    line-height: 1.5;
    text-decoration: none;
    transition: color 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.publication-link::after {
    content: "↗";
    font-size: 0.86em;
}

.publication-link:hover {
    border-color: #d8dee8;
    background: #fff;
    color: var(--blue);
    text-decoration: none;
}

/* Conference Presentations */
.conference-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.conference-card {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.55rem 0.95rem;
    border: 1px solid var(--line);
    border-radius: 12px;
    background: #fff;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);
    font-size: 0.93em;
    color: #3d444d;
    transition: border-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
}

.conference-card:hover {
    border-color: #d8dee8;
    box-shadow: 0 8px 18px rgba(15, 23, 42, 0.055);
    transform: translateY(-1px);
}

.conference-card span,
.conference-card strong {
    font-weight: 500 !important;
}

.conference-logo {
    width: 28px;
    height: 28px;
    object-fit: contain;
}

/* Mobile */
@media (max-width: 768px) {
    .page__inner-wrap {
        max-width: 100% !important;
    }

    body {
        font-size: 0.94em;
    }

    h2 {
        margin-top: 2.4rem;
    }

    .publication-card {
        grid-template-columns: 1fr;
        gap: 0.62rem;
        padding: 1rem;
        border-radius: 12px;
    }

    .publication-card::before {
        width: auto;
        height: auto;
        justify-content: flex-start;
        border: 0;
        background: transparent;
        color: var(--blue);
        font-size: 0.78em;
    }
}
</style>

<h2>Publications</h2>

<div class="publication-legend">
    * = Corresponding author<br>
    + = Co-first author
</div>

<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Empowering Civic Engagement in AI Governance: A Two-wave Panel Study on AI Literacy and Participatory Governance of Generative AI in China.</span>
            <span class="publication-authors">Lin, Z., Jin, Q., & <span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>Telecommunications Policy</em>, 2026.</span>
            <a href="https://doi.org/10.1016/j.telpol.2026.103190" class="publication-link" target="_blank" rel="noopener">Access</a>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human–AI Intimate Interactions.</span>
            <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.*</span></span>
            <span class="publication-venue"><em>Psychology of Popular Media</em>, 2025.</span>
            <a href="https://doi.org/10.1037/ppm0000636" class="publication-link" target="_blank" rel="noopener">Access</a>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">从“机事”到“机心”：与智能技术的深度意义交互及当代青年的数字生命观形成.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>新闻与传播研究</em>, 2025.</span>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Performing Intimacy: Curating the Self-presentation in Human–AI Relationships.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span>, Huang, Y.</span>
            <span class="publication-venue"><em>Emerging Media</em>, 2025.</span>
            <a href="https://doi.org/10.1177/27523543251334157" class="publication-link" target="_blank" rel="noopener">Access</a>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders.</span>
            <span class="publication-authors">Mou, Y.<sup>+</sup>, <span class="my-name">Lan, J.<sup>+</sup></span>, & Huang, Y.</span>
            <span class="publication-venue"><em>New Media & Society</em>, 2023.</span>
            <a href="https://doi.org/10.1177/14614448231212822" class="publication-link" target="_blank" rel="noopener">Access</a>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">机器写作中的性别刻板印象：基于实验研究的实然探讨.</span>
            <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>中国网络传播研究</em>, 2023.</span>
        </div>
    </div>
</div>

<h2>Book Reviews & Interviews</h2>

<div class="publication-list">
    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">人、物、机器：重思“机器问题”与机器人权利——专访大卫·贡克尔.</span>
            <span class="publication-authors"><span class="my-name">蓝剑锋</span></span>
            <span class="publication-venue"><em>国际新闻界</em>, 2026.</span>
        </div>
    </div>

    <div class="publication-card">
        <div class="publication-content">
            <span class="publication-title">Book Review: Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond.</span>
            <span class="publication-authors"><span class="my-name">Lan, J.</span></span>
            <span class="publication-venue"><em>AI & Society</em>, 2025.</span>
            <a href="https://doi.org/10.1007/s00146-025-02693-0" class="publication-link" target="_blank" rel="noopener">Access</a>
        </div>
    </div>
</div>

<h2>Conference Presentations</h2>

<div class="conference-grid">
    <div class="conference-card">
        <img src="/images/logo/4S.png" class="conference-logo" alt="4S logo">
        <span>4S 2026</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">
        <span>ICA 2026</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/NCA.jpeg" class="conference-logo" alt="NCA logo">
        <span>NCA 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/4S.png" class="conference-logo" alt="4S logo">
        <span>4S 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/AEJMC.jpeg" class="conference-logo" alt="AEJMC logo">
        <span>AEJMC 2025 🏆</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/IAMCR1.png" class="conference-logo" alt="IAMCR logo">
        <span>IAMCR 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">
        <span>ICA 2025</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/NCA.jpeg" class="conference-logo" alt="NCA logo">
        <span>NCA 2024</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">
        <span>ICA 2024</span>
    </div>
    <div class="conference-card">
        <img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">
        <span>ICA 2023</span>
    </div>
</div>
