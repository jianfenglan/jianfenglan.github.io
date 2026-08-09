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
  font-size: 0.96em;
  font-weight: 300;
  line-height: 1.82;
}

.about-kicker {
  margin: 0 0 1rem;
  color: #777d83;
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.about-hero {
  max-width: 820px;
  margin: 0 0 3.5rem;
  padding-bottom: 2.6rem;
  border-bottom: 0.5px solid #e5e7ea;
}

.about-hero__statement {
  margin: 0;
  color: #2d3034;
  font-size: clamp(1.45rem, 2.3vw, 2.05rem);
  font-weight: 300;
  line-height: 1.34;
  letter-spacing: -0.028em;
  text-align: left;
}

.about-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.9fr) minmax(210px, 0.8fr);
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

.about-aside {
  display: grid;
  gap: 1.7rem;
}

.about-aside__group {
  padding-top: 0.8rem;
  border-top: 0.5px solid #e5e7ea;
}

.about-aside__label {
  display: block;
  margin-bottom: 0.65rem;
  color: #7a8086;
  font-size: 0.67rem;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.about-aside__value {
  display: block;
  color: #555a5f;
  font-size: 0.88rem;
  font-weight: 300;
  line-height: 1.7;
}

@media (max-width: 820px) {
  .about-hero {
    margin-bottom: 2.5rem;
    padding-bottom: 2rem;
  }

  .about-grid {
    grid-template-columns: 1fr;
    gap: 2.6rem;
  }

  .about-aside {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.5rem 2rem;
  }
}

@media (max-width: 520px) {
  .about-hero__statement {
    font-size: 1.38rem;
  }

  .about-aside {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="about-wrap">
  <section class="about-hero">
    <div class="about-kicker">About</div>
    <p class="about-hero__statement">Hi, this is Jeff. I study people, machines, and the complicated feelings in between.</p>
  </section>

  <div class="about-grid">
    <div class="about-main">
      <p>I'm a Ph.D. candidate in Communication at Shanghai Jiao Tong University, part of the combined master's-doctoral program, and a member of the <a href="https://cfmhmc.github.io/" target="_blank" rel="noopener">Center for Future Media &amp; Human-Machine Communication</a>, under the supervision of <a href="https://cfmhmc.github.io/yimou.github.io/" target="_blank" rel="noopener">Prof. Yi Mou</a>.</p>

      <p>My work sits at the intersection of human-AI communication and media psychology. Specifically, I am interested in how people form intimate relationships with AI systems, how these relationships persist or shift as the underlying technology evolves, and how emerging media reshape practices around mourning, memory, and digital immortality. I also examine the governance and political economy of AI platforms, integrating qualitative, quantitative, and mixed-methods approaches to investigate the psychological, relational, and institutional dimensions of human–AI interaction.</p>

      <p>I currently serve as Assistant Editor for <a href="https://journals.sagepub.com/home/bds" target="_blank" rel="noopener">Big Data &amp; Society</a>, and Student Committee Chair for the <a href="https://www.chinesecommunicationstudies.com/" target="_blank" rel="noopener">Association for Chinese Communication Studies</a>. Before joining SJTU, I completed my B.A. in Journalism at Chongqing University.</p>
    </div>

    <aside class="about-aside" aria-label="Profile highlights">
      <div class="about-aside__group">
        <span class="about-aside__label">Research</span>
        <span class="about-aside__value">Human–AI Communication<br>Media Psychology<br>AI Intimacy</span>
      </div>

      <div class="about-aside__group">
        <span class="about-aside__label">Current</span>
        <span class="about-aside__value">Ph.D. Candidate · SJTU<br>Assistant Editor · Big Data &amp; Society</span>
      </div>

      <div class="about-aside__group">
        <span class="about-aside__label">Methods</span>
        <span class="about-aside__value">Qualitative<br>Quantitative<br>Mixed Methods</span>
      </div>
    </aside>
  </div>
</div>
