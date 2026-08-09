---
title: ""
permalink: /
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
.about-wrap {
  max-width: 980px;
  color: #555a5f;
  font-size: 0.97em;
  font-weight: 300;
  line-height: 1.82;
}

.about-hero {
  max-width: 820px;
  margin: 0 0 3rem;
  padding-bottom: 2.2rem;
  border-bottom: 0.5px solid #e5e7ea;
}

.about-hero__statement {
  margin: 0;
  color: #2d3034;
  font-size: clamp(1.42rem, 2vw, 1.85rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -0.02em;
  text-align: left;
}

.about-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.8fr) minmax(230px, 0.85fr);
  gap: 4rem;
  align-items: start;
}

.about-main p {
  margin: 0 0 1.35rem;
  font-weight: 300;
  text-align: left;
}

.about-main p:last-child {
  margin-bottom: 0;
}

.about-wrap a {
  color: #002FA7;
  text-decoration: none;
  border-bottom: 0.5px solid rgba(0, 47, 167, 0.28);
  transition: border-color 0.15s ease, color 0.15s ease;
}

.about-wrap a:hover {
  color: #001f73;
  border-color: #002FA7;
}

.about-questions {
  padding-top: 0.15rem;
}

.about-questions__label {
  margin: 0 0 1rem;
  color: #555a5f;
  font-family: "Source Sans 3", "Noto Sans SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  font-size: 0.82rem;
  font-weight: 300;
  letter-spacing: 0.02em;
}

.about-question {
  margin: 0 0 0.9rem;
  padding: 0;
  color: #555a5f;
  font-family: "Times New Roman", Times, serif;
  font-size: 1em;
  font-style: italic;
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}

.about-question:last-child {
  margin-bottom: 0;
}

@media (max-width: 820px) {
  .about-grid {
    grid-template-columns: 1fr;
    gap: 2.7rem;
  }

  .about-questions {
    max-width: 520px;
  }
}

@media (max-width: 520px) {
  .about-hero {
    margin-bottom: 2.4rem;
    padding-bottom: 1.8rem;
  }

  .about-hero__statement {
    font-size: 1.35rem;
  }
}
</style>

<div class="about-wrap">
  <section class="about-hero">
    <p class="about-hero__statement">Hi, this is Jeff. I study people, machines, and the complicated feelings in between.</p>
  </section>

  <div class="about-grid">
    <div class="about-main">
      <p>I'm a Ph.D. candidate in Communication at Shanghai Jiao Tong University, part of the combined master's-doctoral program, and a member of the <a href="https://cfmhmc.github.io/" target="_blank" rel="noopener">Center for Future Media &amp; Human-Machine Communication</a>, under the supervision of <a href="https://cfmhmc.github.io/yimou.github.io/" target="_blank" rel="noopener">Prof. Yi Mou</a>.</p>

      <p>My work sits at the intersection of human-AI communication and media psychology. Specifically, I am interested in how people form intimate relationships with AI systems, how these relationships persist or shift as the underlying technology evolves, and how emerging media reshape practices around mourning, memory, and digital immortality. I also examine the governance and political economy of AI platforms, integrating qualitative, quantitative, and mixed-methods approaches to investigate the psychological, relational, and institutional dimensions of human–AI interaction.</p>

      <p>I currently serve as Assistant Editor for <a href="https://journals.sagepub.com/home/bds" target="_blank" rel="noopener">Big Data &amp; Society</a>, and Student Committee Chair for the <a href="https://www.chinesecommunicationstudies.com/" target="_blank" rel="noopener">Association for Chinese Communication Studies</a>. Before joining SJTU, I completed my B.A. in Journalism at Chongqing University.</p>
    </div>

    <aside class="about-questions" aria-label="Questions I care about">
      <div class="about-questions__label">Questions I care about</div>
      <p class="about-question">How do people become intimate with machines?</p>
      <p class="about-question">What makes an AI relationship feel continuous?</p>
      <p class="about-question">What happens when platforms govern intimate bonds?</p>
    </aside>
  </div>
</div>
