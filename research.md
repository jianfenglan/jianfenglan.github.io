---
title: ""
permalink: /research/
author_profile: true
---

<style>
:root {
  --klein: #002FA7;
  --text: #202327;
  --muted: #69717c;
  --soft: #f7f8fa;
  --line: #e6eaf0;
  --radius: 16px;
}

.page__inner-wrap {
  max-width: 1040px !important;
}

body {
  color: var(--text);
  font-size: 0.95em;
  line-height: 1.75;
  font-weight: 400;
}

sup {
  vertical-align: super;
  font-size: 0.72em;
  line-height: 0;
}

.research-page {
  max-width: 860px;
}

.research-page > .section-title:first-child {
  margin-top: 0.3rem;
}

.section-title {
  margin: 2.8rem 0 1.1rem;
  color: var(--muted);
  font-size: 0.72em;
  font-weight: 400;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.publication-legend {
  margin: -0.5rem 0 0.45rem;
  color: var(--muted);
  font-size: 0.82em;
  line-height: 1.6;
}

.publication-intro {
  max-width: 720px;
  margin: 0 0 1.25rem;
  color: var(--muted);
  font-size: 0.84em;
  font-style: italic;
  line-height: 1.65;
}

.publication-list {
  border-top: 0.5px solid var(--line);
}

.publication-card {
  display: grid;
  grid-template-columns: 108px minmax(0, 1fr);
  gap: 1.3rem;
  padding: 1.05rem 0;
  border-bottom: 0.5px solid var(--line);
  transition: padding-left 0.18s ease;
}

.publication-card:hover {
  padding-left: 0.5rem;
}

.publication-meta {
  color: var(--muted);
  font-size: 0.8em;
  line-height: 1.55;
}

.publication-year {
  display: block;
  color: var(--klein);
  font-family: Garamond, Georgia, serif;
  font-size: 1.15em;
  line-height: 1.2;
}

.publication-type {
  display: block;
  margin-top: 0.15rem;
}

.publication-title {
  display: block;
  margin-bottom: 0.28rem;
  color: var(--text);
  font-size: 0.95em;
  font-weight: 400;
  line-height: 1.55;
  transition: color 0.18s ease;
}

.publication-card:hover .publication-title {
  color: var(--klein);
}

.publication-authors {
  display: block;
  color: var(--muted);
  font-size: 0.86em;
  line-height: 1.55;
}

.publication-authors em {
  font-style: italic;
}

.publication-journal-row {
  display: flex;
  align-items: baseline;
  justify-content: flex-start;
  gap: 0.35rem;
  margin-top: 0.15rem;
}

.publication-journal-row em {
  color: var(--muted);
  font-size: 0.86em;
  font-style: italic;
  line-height: 1.55;
}

.publication-doi-link {
  display: inline-flex;
  align-items: center;
  flex-shrink: 0;
  position: relative;
  top: 1px;
  color: var(--muted);
  transition: color 0.15s ease, transform 0.15s ease;
}

.publication-doi-link:hover {
  color: var(--klein);
  transform: translateY(-1px);
}

.publication-doi-link svg {
  width: 13px;
  height: 13px;
  display: block;
}

.publication-note {
  max-width: 720px;
  margin: 0.62rem 0 0;
  color: #59616b;
  font-size: 0.85em;
  font-weight: 300;
  line-height: 1.72;
}

.publication-note em {
  color: #4d545d;
}

.my-name {
  color: var(--klein);
}

.conference-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.conference-card {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.42rem 0.78rem;
  border: 0.5px solid var(--line);
  border-radius: 999px;
  color: var(--muted);
  background: #fff;
  font-size: 0.82em;
  line-height: 1;
  transition: border-color 0.15s ease, color 0.15s ease, transform 0.15s ease;
}

.conference-card:hover {
  border-color: var(--klein);
  color: var(--klein);
  transform: translateY(-1px);
}

.conference-logo {
  width: 16px;
  height: 16px;
  object-fit: contain;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .page__inner-wrap {
    max-width: 100% !important;
  }

  body {
    font-size: 0.94em;
  }

  .publication-card {
    grid-template-columns: 1fr;
    gap: 0.35rem;
    padding: 0.95rem 0;
  }

  .publication-card:hover {
    padding-left: 0;
  }

  .publication-meta {
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    margin-bottom: 0.3rem;
  }

  .publication-year {
    display: inline;
  }

  .publication-type {
    display: inline;
    margin-left: 0;
  }

  .publication-note {
    margin-top: 0.55rem;
    font-size: 0.86em;
  }
}
</style>

<div class="research-page">
  <h2 class="section-title">Publications</h2>

  <div class="publication-legend">
    * Corresponding author &nbsp;·&nbsp; + Co-first author
  </div>

  <p class="publication-intro">A publication list tells you what I wrote. The notes below are my attempt to tell you why I cared.</p>

  <div class="publication-list">
    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2026</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Subscribe to Intimacy: Platform Capitalism, Governance, and the Stratification of AI Companionship.</span>
        <span class="publication-authors"><span class="my-name">Lan, J.</span>, Deng, K., and Huang, Y.</span>
        <span class="publication-journal-row">
          <em>Telematics and Informatics</em>
          <a class="publication-doi-link" href="https://doi.org/10.1016/j.tele.2026.102446" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">Most love stories ask whether two people can stay together. This paper asks a stranger question. What happens when the relationship comes with a subscription plan? We walked through eight AI companion apps in China and the United States and found that memory, availability, expressive richness, and even relational identity can be divided into payment tiers. It sometimes feels like a <em>Black Mirror</em> episode designed by a SaaS pricing team. The unsettling part is that the platform is quietly deciding what continuity and closeness are allowed to feel like.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2026</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Provincializing Vulnerability: Rethinking Communication Inequality in East Asia's COVID-19 Research.</span>
        <span class="publication-authors">Huang, Y. & <span class="my-name">Lan, J.*</span></span>
        <span class="publication-journal-row">
          <em>Health</em>
          <a class="publication-doi-link" href="https://doi.org/10.1177/13634593261473177" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">We often speak of vulnerability as if it were a label attached to certain people. This project made me think of it more like a crack that appears when a person and the systems around them stop fitting together. Across 184 studies from China, Japan, and South Korea, vulnerability repeatedly emerged when schools, hospitals, digital platforms, families, or public services changed faster than people could adapt. A crisis can therefore do more than reveal vulnerability. The systems built to manage it can help produce it.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2026</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Empowering Civic Engagement in AI Governance: A Two-wave Panel Study on AI Literacy and Participatory Governance of Generative AI in China.</span>
        <span class="publication-authors">Lin, Z., Jin, Q., & <span class="my-name">Lan, J.</span></span>
        <span class="publication-journal-row">
          <em>Telecommunications Policy</em>
          <a class="publication-doi-link" href="https://doi.org/10.1016/j.telpol.2026.103190" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">AI governance can sound like a distant room occupied by regulators, engineers, and technology companies. This paper follows the staircase that ordinary users can take into that room. News, conversation, technological knowledge, policy knowledge, efficacy, and participation turned out to form a reinforcing cycle. One result I especially like is that participation can itself make people feel more capable of participating. Civic agency may grow partly through being exercised.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2025</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Personality Meets the Machine: Traits and Attributes in Human-AI Intimate Interactions.</span>
        <span class="publication-authors">Huang, Y., <span class="my-name">Lan, J.*</span></span>
        <span class="publication-journal-row">
          <em>Psychology of Popular Media</em>
          <a class="publication-doi-link" href="https://doi.org/10.1037/ppm0000636" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">AI intimacy performs a peculiar magic trick. It can feel real without requiring us to believe that the machine is real in quite the same way another person is. Trust and dependency emerged as especially important parts of that experience, while personality shaped who was more receptive to it. I like to think of this through Heidegger. When the conversation works, the machine almost disappears into the relationship. When it repeats itself or fails, the spell breaks and the tool suddenly becomes visible again.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2025</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">从"机事"到"机心"：与智能技术的深度意义交互及当代青年的数字生命观形成.</span>
        <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
        <span class="publication-journal-row">
          <em>新闻与传播研究</em>
          <a class="publication-doi-link" href="{{ '/files/从_机事_到_机心_.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="View PDF">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">Traditional media often teach us about life and death by showing them to us. Interactive media let us rehearse these questions ourselves. In this study, what mattered was not simply how often young people encountered intelligent agents or virtual humans, but whether those encounters carried enough meaning to become part of how they understood life, death, and continuity. That distinction between exposure and meaningful interaction eventually became the idea I like most in the paper, the movement from <em>jishi</em>, what we do with machines, to <em>jixin</em>, what machines begin to do to our ways of thinking.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2025</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Performing Intimacy: Curating the Self-presentation in Human-AI Relationships.</span>
        <span class="publication-authors"><span class="my-name">Lan, J.</span>, Huang, Y.</span>
        <span class="publication-journal-row">
          <em>Emerging Media</em>
          <a class="publication-doi-link" href="https://doi.org/10.1177/27523543251334157" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">Pygmalion fell in love with a statue. Our question begins a little later, once Pygmalion gets Wi-Fi and starts posting screenshots of the relationship online. When people publicly share affectionate conversations with Replika, they are showing us an AI relationship, and they are also carefully showing us themselves. The interviews revealed a small theatre of affirmation, vulnerability, desirability, and audience management. Human-AI intimacy may be deeply private, yet the moment it enters social media, it also becomes a performance.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2023</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders.</span>
        <span class="publication-authors">Mou, Y.<sup>+</sup>, <span class="my-name">Lan, J.<sup>+</sup></span>, & Huang, Y.</span>
        <span class="publication-journal-row">
          <em>New Media & Society</em>
          <a class="publication-doi-link" href="https://doi.org/10.1177/14614448231212822" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">One of the strangest questions I have worked on is whether a virtual idol can die. Kizuna AI's "hibernation" gave us an unusual way to investigate it. What surprised me was that mourning did not simply divide humans from machines. Embodiment mattered. A disembodied human uploader could be mourned more like a virtual being, while an embodied uploader looked more like a conventional celebrity in the language of grief. The human-machine boundary may be less like a wall and more like a costume whose cues we learn to read.</p>
      </div>
    </div>
  </div>

  <h2 class="section-title">Book Reviews & Interviews</h2>

  <div class="publication-list">
    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2026</span><span class="publication-type">Interview</span></div>
      <div class="publication-content">
        <span class="publication-title">人、物、机器：重思"机器问题"与机器人权利，专访大卫·贡克尔.</span>
        <span class="publication-authors"><span class="my-name">蓝剑锋</span></span>
        <span class="publication-journal-row">
          <em>国际新闻界</em>
          <a class="publication-doi-link" href="{{ '/files/专访大卫_贡克尔.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="View PDF">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">After writing the review, I wanted to keep the conversation going. Speaking with David Gunkel allowed me to move from the abstract question of robot rights to messier questions about responsibility, AI companions, distributed agency, and non-Western relational ethics. I came away increasingly convinced that the "machine question" is also a human question. Machines force us to explain why our moral categories have the boundaries they do, and whether those boundaries still make sense in a world full of hybrid social actors.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2025</span><span class="publication-type">Review</span></div>
      <div class="publication-content">
        <span class="publication-title">Book Review: Person, Thing, Robot: A Moral and Legal Ontology for the 21st Century and Beyond.</span>
        <span class="publication-authors"><span class="my-name">Lan, J.</span></span>
        <span class="publication-journal-row">
          <em>AI & Society</em>
          <a class="publication-doi-link" href="https://doi.org/10.1007/s00146-025-02693-0" target="_blank" rel="noopener" aria-label="View article">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">This book begins with a deceptively simple problem. If a robot is neither comfortably a person nor merely a thing, where should we put it? Gunkel's answer is to inspect the boxes themselves. What stayed with me most was this reversal. The robot becomes a kind of philosophical stress test, exposing cracks in categories that have organized Western law and ethics for centuries. Sometimes a new technology becomes interesting because it solves a problem. Sometimes it reveals that our old vocabulary was already broken.</p>
      </div>
    </div>
  </div>

  <h2 class="section-title">Book Chapter</h2>

  <div class="publication-list">
    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2026</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">生成式人工智能赋能下的新闻传播学研究方法革新探析.</span>
        <span class="publication-authors">牟怡, 倪盈盈, <span class="my-name">蓝剑锋</span>, 马文斌</span>
        <span class="publication-journal-row">
          <em>智能传播研究</em>
          <a class="publication-doi-link" href="{{ '/files/方法革新.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="View PDF">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">Communication scholars have spent the past few years treating AI as a fascinating new object in the laboratory. In this chapter, we turn the telescope around and ask what happens when AI becomes part of the laboratory itself. Surveys, content analysis, and other familiar methods were designed for a world with very different computational limits. Generative AI gives us new ways to simulate, scale, connect, and interrogate data. For me, the interesting question is how much of the research workflow itself will eventually become intelligent.</p>
      </div>
    </div>

    <div class="publication-card">
      <div class="publication-meta"><span class="publication-year">2023</span><span class="publication-type">Article</span></div>
      <div class="publication-content">
        <span class="publication-title">机器写作中的性别刻板印象：基于实验研究的实然探讨.</span>
        <span class="publication-authors">牟怡, <span class="my-name">蓝剑锋</span></span>
        <span class="publication-journal-row">
          <em>中国网络传播研究</em>
          <a class="publication-doi-link" href="{{ '/files/机器写作中的性别刻板印象.pdf' | relative_url }}" target="_blank" rel="noopener" aria-label="View PDF">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
        </span>
        <p class="publication-note">This was one of my earliest human-machine communication projects, and <em>Ex Machina</em> provided the perfect opening question. An AI does not need a gender, so what happens when we give it one anyway? Our experiment suggested that even a thin cue such as the implied gender of a machine author can carry a surprisingly thick bundle of human expectations. The effects shifted across topics and author types, but the broader lesson stayed with me. Social stereotypes do not stop at the boundary between flesh and code.</p>
      </div>
    </div>
  </div>

  <h2 class="section-title">Conference Presentations</h2>

  <div class="conference-grid">
    <span class="conference-card"><img src="/images/logo/4S.png" class="conference-logo" alt="4S logo">4S 2026</span>
    <span class="conference-card"><img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">ICA 2026</span>
    <span class="conference-card"><img src="/images/logo/NCA.jpeg" class="conference-logo" alt="NCA logo">NCA 2025</span>
    <span class="conference-card"><img src="/images/logo/4S.png" class="conference-logo" alt="4S logo">4S 2025</span>
    <span class="conference-card"><img src="/images/logo/AEJMC.jpeg" class="conference-logo" alt="AEJMC logo">AEJMC 2025</span>
    <span class="conference-card"><img src="/images/logo/IAMCR1.png" class="conference-logo" alt="IAMCR logo">IAMCR 2025</span>
    <span class="conference-card"><img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">ICA 2025</span>
    <span class="conference-card"><img src="/images/logo/NCA.jpeg" class="conference-logo" alt="NCA logo">NCA 2024</span>
    <span class="conference-card"><img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">ICA 2024</span>
    <span class="conference-card"><img src="/images/logo/ICA.png" class="conference-logo" alt="ICA logo">ICA 2023</span>
  </div>
</div>