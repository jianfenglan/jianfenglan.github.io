---
title: ""
permalink: /blog/
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

/* Blog / News List */
.news-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.05rem;
    margin: 1.2rem 0 2.5rem;
}

.news-card {
    display: grid;
    grid-template-columns: minmax(260px, 0.9fr) minmax(360px, 1.4fr);
    align-items: stretch;
    min-height: 235px;
    border: 1px solid var(--line);
    border-radius: 16px;
    background: #fff;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);
    overflow: hidden;
    cursor: pointer;
    transition: border-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
}

.news-card:hover {
    border-color: #d8dee8;
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.06);
    transform: translateY(-1px);
}

.news-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1.35rem 1.45rem;
    min-width: 0;
    background: #fff;
}

.news-content h3 {
    margin: 0 0 0.45rem;
    color: #202327;
    font-size: 1.08em;
    font-weight: 560;
    line-height: 1.42;
}

.news-meta {
    display: block;
    color: var(--muted);
    font-size: 0.9em;
    line-height: 1.5;
}

.news-link-hint {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    gap: 0.25rem;
    margin-top: 1rem;
    color: #69717d;
    font-size: 0.88em;
    line-height: 1.5;
    transition: color 0.18s ease;
}

.news-link-hint::after {
    content: "↗";
    font-size: 0.86em;
}

.news-card:hover .news-link-hint {
    color: var(--blue);
}

.news-image {
    position: relative;
    min-height: 235px;
    background: #fff;
    overflow: hidden;
}

.news-image img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.news-card:hover .news-image img {
    transform: scale(1.018);
}

/* Modal */
.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    inset: 0;
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(7px);
    justify-content: center;
    align-items: center;
    padding: 2rem;
}

.modal-overlay.show {
    display: flex;
}

.modal-content {
    position: relative;
    width: min(760px, 100%);
    max-height: calc(100vh - 8rem);
    margin-top: 3rem;
    padding: 2rem;
    border: 1px solid var(--line);
    border-radius: 18px;
    background: #fff;
    box-shadow: 0 18px 48px rgba(15, 23, 42, 0.14);
    overflow-y: auto;
    word-wrap: break-word;
    transform: translateY(8px) scale(0.98);
    opacity: 0;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.modal-overlay.show .modal-content {
    transform: translateY(0) scale(1);
    opacity: 1;
}

.close-button {
    position: absolute;
    top: 1rem;
    right: 1.1rem;
    color: #8a929d;
    font-size: 1.45rem;
    line-height: 1;
    cursor: pointer;
    transition: color 0.18s ease;
}

.close-button:hover {
    color: var(--blue);
}

#modal-title {
    margin: 0 2rem 0.45rem 0;
    color: #202327;
    font-size: 1.08em;
    font-weight: 560;
    line-height: 1.45;
}

#modal-meta {
    margin-bottom: 1.25rem;
    color: var(--muted);
    font-size: 0.9em;
    font-weight: 400;
    line-height: 1.5;
}

#modal-body p {
    margin: 0 0 1rem;
    color: #363b42;
    font-size: 0.96em;
    line-height: 1.75;
    font-weight: 400;
    text-align: left;
}

#modal-body p:last-of-type {
    margin-bottom: 0;
}

#modal-body img {
    max-width: 100%;
    height: auto;
    margin-top: 1rem;
    border-radius: 14px;
}

/* Mobile */
@media (max-width: 768px) {
    .page__inner-wrap {
        max-width: 100% !important;
    }

    body {
        font-size: 0.94em;
    }

    .news-list {
        gap: 1rem;
        margin-top: 1rem;
    }

    .news-card {
        grid-template-columns: 1fr;
        min-height: 0;
        border-radius: 14px;
    }

    .news-image {
        order: -1;
        min-height: 210px;
        height: 210px;
    }

    .news-content {
        padding: 1.1rem 1.15rem 1.2rem;
    }

    .news-content h3 {
        font-size: 1.02em;
    }

    .modal-overlay {
        align-items: flex-start;
        padding: 1rem;
    }

    .modal-content {
        max-height: calc(100vh - 5rem);
        margin-top: 3.5rem;
        padding: 1.45rem;
        border-radius: 16px;
    }
}
</style>

<div class="news-list">

<div class="news-card" onclick="openModal(this)" data-title="ICA 2026" data-meta="June 6, 2026 | Cape Town" data-content="<p>Caught up with old friends, met new ones, presented research, learned a lot, and probably drank more wine than I should admit.<br><br>Also managed to see penguins, seals, baboons, and a few breathtaking landscapes along the way. Leaving with new ideas, new connections, and a renewed appreciation for this community.<br><br>Until next year.</p>">
    <div class="news-content">
        <h3>ICA 2026</h3>
        <span class="news-meta">June 6, 2026 | Cape Town</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2026.png' | relative_url }}" alt="ICA 2026">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="NCA 2025" data-meta="November 22, 2025 | Denver" data-content="<p>This is my first year serving as the Student Affairs Committee Chair for ACCS at NCA. I joined the business meeting remotely and was delighted to be part of the group photo.<br><br>I feel deeply honored and grateful to have received such tremendous support from both the internal and external communities. I look forward to connecting with you all in the future.</p>">
    <div class="news-content">
        <h3>NCA 2025</h3>
        <span class="news-meta">November 22, 2025 | Denver</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA25.JPG' | relative_url }}" alt="NCA 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="PCST-Tokyo Symposium 2025" data-meta="November 11, 2025 | Tokyo" data-content="<p>My journey brought me to Tokyo, Japan, for my first time attending the PCST Conference. Together with my collaborator Kelsie, our latest research explores issues of inequality and vulnerability in communication, with a particular focus on East Asian contexts. We were excited to share our ongoing work at this meeting—our first venture into the field of science communication. The organizer provided an excellent environment for thoughtful exchange, with everyone fully engaged in each presentation. <br><br>The Institute of Science Tokyo is such a fascinating place, and I truly hope to return to Japan for more conferences in the future.</p>">
    <div class="news-content">
        <h3>PCST-Tokyo Symposium 2025</h3>
        <span class="news-meta">November 11, 2025 | Tokyo</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/PCST.jpg' | relative_url }}" alt="PCST-Tokyo Symposium 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="HKBU Graduate Conference 2025" data-meta="August 12, 2025 | Hong Kong" data-content="<p>I am sincerely grateful to the School of Communication at Hong Kong Baptist University for organizing the conference themed “Advancing Responsible AI Communication” and for fully funding my trip to Hong Kong. This marks my third visit to the city, but my first time at HKBU. <br><br>I was delighted to share my latest research on human–AI intimacy at the conference and truly appreciated the insightful feedback and inspiring conversations I received.</p>">
    <div class="news-content">
        <h3>HKBU Graduate Conference 2025</h3>
        <span class="news-meta">August 12, 2025 | Hong Kong</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/HKBU25.JPG' | relative_url }}" alt="HKBU Graduate Conference 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="AEJMC 2025" data-meta="August 8, 2025 | San Francisco" data-content="<p>I’m deeply honored to receive the Top Student Paper Award from the AEJMC History Division this year. My co-author, Kelsie, deserves immense credit—she contributed greatly, and this recognition truly belongs to her. <br><br>Although I couldn’t attend the conference in person, I’m grateful to my friend Nesh for bringing this precious gift back to Shanghai.</p>">
    <div class="news-content">
        <h3>AEJMC 2025</h3>
        <span class="news-meta">August 8, 2025 | San Francisco</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/AEJMC25.png' | relative_url }}" alt="AEJMC 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="IAMCR 2025" data-meta="July 15, 2025 | Singapore" data-content="<p>While my physical form was tragically unable to grace the halls of IAMCR 2025 this year, my fantastic colleague and co-author, Jingyi Li, represented us beautifully.<br><br>Maybe next year I'll figure out how to teleport.</p>">
    <div class="news-content">
        <h3>IAMCR 2025</h3>
        <span class="news-meta">July 15, 2025 | Singapore</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/IAMCR2025.jpg' | relative_url }}" alt="IAMCR 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2025" data-meta="June 15, 2025 | Denver" data-content="<p>I was truly disappointed to have missed this year's ICA conference in Denver. Fortunately, my dear friend and colleague, Kelsie, was there to present our latest work. I wanted to share this wonderful photo of her and express my immense gratitude for her support.</p><p>Over time, I've come to realize that the value of academic conferences extends far beyond presenting research. I couldn't agree more with Kelsie that having a few deep conversations with friends you only meet annually is far more meaningful than adding fifty new contacts to your phone.</p>">
    <div class="news-content">
        <h3>ICA 2025</h3>
        <span class="news-meta">June 15, 2025 | Denver</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2025.jpg' | relative_url }}" alt="ICA 2025">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="NCA 2024" data-meta="November 22, 2024 | New Orleans" data-content="<p>My journey at NCA 2024 is off to a magical start.</p><p>I extend my heartfelt gratitude to Dr. Patrick and Dr. Dongjing for inviting me to the Tenth Annual U.S.-China Communication Scholars Summit and giving me the opportunity to present my latest research.</p><p>This year, I’m honored to serve as the Student Committee Chair for ACCS and the Graduate Student Representative for the CATF division at NCA. I welcome your suggestions and invite you to reach out for more information.</p>">
    <div class="news-content">
        <h3>NCA 2024</h3>
        <span class="news-meta">November 22, 2024 | New Orleans</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/NCA.png' | relative_url }}" alt="NCA 2024">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2024" data-meta="June 23, 2024 | Gold Coast" data-content="<p>I thoroughly enjoyed my time in Australia.</p><p>My colleagues Kelsie, Christina, and Zhi and I co-authored two papers on AIGC regulation, emerging media usage, and adolescent body image issues in China.</p><p>Academic research not only provided a sense of achievement but also fostered valuable friendships.</p>">
    <div class="news-content">
        <h3>ICA 2024</h3>
        <span class="news-meta">June 23, 2024 | Gold Coast</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2024.png' | relative_url }}" alt="ICA 2024">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="SICSS-Singapore 2024" data-meta="June 7, 2024 | Singapore" data-content="<p>This summer, I'm deeply honored to attend SICSS-Singapore at beautiful National University of Singapore. Five days' talks and discussions were beyond insightful and full of joy. Special thanks to Rongxin and Jinyuan for their host.</p><p>Also, thanks to the speakers' generous sharing about their research, it was so inspiring. I highly recommend signing up for the upcoming SICSS-Singapore event—you won’t regret it.</p>">
    <div class="news-content">
        <h3>SICSS-Singapore 2024</h3>
        <span class="news-meta">June 7, 2024 | Singapore</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/SICSS01.JPG' | relative_url }}" alt="SICSS-Singapore 2024">
    </div>
</div>

<div class="news-card" onclick="openModal(this)" data-title="ICA 2023" data-meta="May 25, 2023 | Toronto" data-content="<p>This marks my first time attending ICA.</p><p>Eager to engage in discourse, gain insight, and pursue academic inquiry, I was fortunate to receive ample assistance and support.</p><p>This academic journey stands as a pivotal experience, ushering in a new chapter.</p>">
    <div class="news-content">
        <h3>ICA 2023</h3>
        <span class="news-meta">May 25, 2023 | Toronto</span>
        <span class="news-link-hint">Read note</span>
    </div>
    <div class="news-image">
        <img src="{{ '/images/news/ICA2302.jpg' | relative_url }}" alt="ICA 2023">
    </div>
</div>

</div>

<div id="news-modal" class="modal-overlay">
    <div class="modal-content">
        <span class="close-button" onclick="closeModal()">×</span>
        <h3 id="modal-title"></h3>
        <div class="meta" id="modal-meta"></div>
        <div id="modal-body"></div>
    </div>
</div>

<script>
function openModal(card) {
    const title = card.getAttribute('data-title');
    const meta = card.getAttribute('data-meta');
    const content = card.getAttribute('data-content');

    document.getElementById('modal-title').innerText = title;
    document.getElementById('modal-meta').innerText = meta;
    document.getElementById('modal-body').innerHTML = content;

    const modal = document.getElementById('news-modal');
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('news-modal');
    modal.classList.remove('show');
    document.body.style.overflow = '';
}

document.getElementById('news-modal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

document.querySelector('.modal-content').addEventListener('click', function(e) {
    e.stopPropagation();
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});
</script>
