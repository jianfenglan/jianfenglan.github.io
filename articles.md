---
title: ""
permalink: /articles/
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
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    line-height: 1.6;
    cursor: pointer;
    flex-wrap: wrap;
}

.publication-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}

.publication-card::before {
    counter-increment: pub-counter;
    content: counter(pub-counter) ".";
    font-weight: 600;
    font-size: 1.1em;
    color: #888;
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
    font-weight: 700;
}

.modal-overlay {
    display: none;
    position: fixed;
    z-index: 999;
    inset: 0;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(6px);
    justify-content: center;
    /* align-items: center; -- 此处移除，用padding代替 */
    /* --- 新增的代码从这里开始 --- */
    padding: 6rem 1rem; /* 为弹窗容器增加上下6rem、左右1rem的内边距，确保不被遮挡 */
    /* --- 新增的代码到这里结束 --- */
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
    max-height: 90vh; 
    overflow-y: auto;
    /* --- 新增的代码 --- */
    margin: auto 0; /* 在垂直方向上自动外边距，实现居中效果 */
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
    color: #666;
}
</style>

<h2>🗞️ Journal Articles</h2>
<div class="publication-list">
  <div class="publication-card" data-detail="<h2>Performing Intimacy: Curating the Self-presentation in Human–AI Relationships</h2><br>Ever wondered what happens when private chats with an AI go public? 🤔 <br><br> We examined how users of the chatbot Replika perform their 「intimate」 relationships on social media. Turns out, it's a fascinating mix of seeking genuine validation and carefully crafting an idealized self-image. <br><br> We found that sharing these moments isn't just about the human-AI bond, but also about managing our own emotions and social standing. It's a performance for an audience. <br><br> Key questions: <br> 👏🏻 When we post about our AI companions, are we looking for connection or just applause? <br> 🤖 Does sharing these intimate moments online reinforce our self-worth, or does it feed our inner narcissist? <br><br> Here's a model of the motivations and outcomes we discovered: <br> <img src='{{ '/images/EMM_F1.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top: 1rem; margin-bottom: 1rem;'> <br>Is our AI partner just a character in the story we write about ourselves online? ✨ <br><br>Read at 👉🏻: https://journals.sagepub.com/doi/10.1177/27523543251334157">
    <div class="publication-content">
      <span class="my-name">Lan, J.</span>, Huang, Y. (2025). Performing Intimacy: Curating the Self-presentation in Human–AI Relationships. <em>Emerging Media</em>, Online first.
    </div>
  </div>
  <div class="publication-card" data-detail="<h2>Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach</h2><br>When a virtual idol 「hibernate」, do we say 「Goodbye」 forever, or just 「Good night」 for now? 👋😴 <br><br> We adopted data-mining to compare how young audiences react to the 「death」 of virtual uploader (VUP), human uploader (HUP), and real-world celebrity. The results are surprising! 🤯 <br><br> Mourning for VUPs is very different from for human celebrities. More interestingly, we found that human uploaders who don't show their faces are mourned more like VUPs, while those who do are mourned like real people. <br><br> This leads to some big questions about our digital lives: <br> 🤔 Are we starting to treat humans more like machines based on how 「real」 they appear online? <br> 🤖 As virtual beings become more human, are humans online becoming less so? <br><br> Our theoretical hypothesis for this is: <br> <img src='{{ '/images/VUP.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top: 1rem; margin-bottom: 1rem;'> <br> It's a fascinating look at how technology is changing our concepts of life, death, and even humanity itself. <br><br>Read at 👉🏻: https://journals.sagepub.com/doi/abs/10.1177/14614448231212822">
    <div class="publication-content">
      Mou, Y.*, <span class="my-name">Lan, J.</span>*, & Huang, Y. (2023). Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach. <em>New Media & Society, 27(5),</em> 2684-2702. (*co-first author)
    </div>
  </div>
  <div class="publication-card" data-detail="<h2>Gender Stereotypes in Perceiving Machine-Written Content: Empirical Evidence Based on an Experimental Study</h2><br>Does it matter if an AI writer is a 「he,」 a 「she,」 or an 「it」? <br><br> This time, we dive into the world of machine-written news to see if we apply real-world gender stereotypes to our silicon authors. Based on the Computers Are Social Actors (CASA) paradigm, we conducted an experiment to see if an article's perceived quality and its author's expertise change when the AI is given a male, female, or neutral name. <br><br> The results show our biases are clear: we judge machine-written content differently based on the gender we associate with it! This reveals the subtle ways our social prejudices extend into the realm of human-machine communication. <br><br> <img src='{{ '/images/Gender.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top: 1rem; margin-bottom: 1rem;'> <br>This paper is in Chinese.">
    <div class="publication-content">
            Mou, Y.[牟怡], <span class="my-name">Lan, J.[蓝剑锋]</span>. (2023). Gender Stereotypes in Perceiving Machine-Written Content: Empirical Evidence Based on an Experimental Study [机器写作中的性别刻板印象: 基于实验研究的实然探讨]. <em>Chinese Journal of Computer-Mediated Communication [中国网络传播研究]</em>, (1)1:236-266.
    </div>
  </div>
</div>

<h2>🗣️ Conference Papers</h2>
<div class="publication-list">
  <div class="publication-card" data-detail="Work in progress ✍🏻">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Huang, Y. (2025). Subscribing to Intimacy: Hyperreal Love and the Commodification of Affordances in Chinese AI Romance Apps. <em>JSF-PCST Tokyo 2025</em>, Tokyo, Japan. </div></div>
  <div class="publication-card" data-detail="Work in progress ✍🏻">
    <div class="publication-content">Huang, Y., <span class="my-name">Lan, J.</span> (2025). Rethinking Vulnerability and Communication Inequality in East Asia: A Scoping Review of COVID-19 Science Communication Practices.  <em>JSF-PCST Tokyo 2025</em>, Tokyo, Japan. </div></div>
  <div class="publication-card" data-detail="">
    <div class="publication-content">Huang, Y., <span class="my-name">Lan, J.</span> (2025). Media Metaphors and Social Meaning of ‘Internet’ in Taiwan (1995-2023). <em>AEJMC 2025</em>, San Francisco, U.S. <br>🥈 Second Runner Up Student Paper Award</div></div>
  <div class="publication-card" data-detail="Work in progress ✍🏻">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Huang, Y. (2025). Reconfiguring Sociality: Human-AI Intimacy, Narcissistic Dynamics, and Replika. <em>Society for Social Studies of Science (4S) 2025</em>, Seattle, U.S.</div></div>
  <div class="publication-card" data-detail="Work in progress ✍🏻">
    <div class="publication-content">Mou, Y., Li, J., <span class="my-name">Lan, J.</span> (2025). A Cross-Cultural Diachronic Examination of Audiences’ Attitudes Toward Digital Immortality in Science Fiction. <em>IAMCR 2025</em>, Singapore.</div></div>
  <div class="publication-card" data-detail="Under Review 🙏🏻">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Huang Y. (2025). Love the Way You Are: Examine the Attribute of Human-AI Intimate Relationships. <em>75th ICA Annual Conference</em>, Denver, U.S.</div></div>
  <div class="publication-card" data-detail="Under Review 🙏🏻">
    <div class="publication-content">Mou, Y., <span class="my-name">Lan, J.</span>, Lu, J., Wang, J. (2024). Emerging Media Use and Acceptance of Digital Immortality: A Cluster Analysis among Chinese Young Generations. <em>NCA 2024</em>, New Orleans, U.S.</div></div>
  <div class="publication-card" data-detail="Under Review 🙏🏻">
    <div class="publication-content">Jin, Q., <span class="my-name">Lan, J.</span>, Lin, Z. (2024). Share My Face: Understanding Privacy Paradox and Third-person Effect of Artificial Intelligence Generated Content (AIGC) Applications. <em>74th ICA Annual Conference</em>, Gold Coast, Australia.</div></div>
  <div class="publication-card" data-detail="">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Huang Y., Mou Y. (2024). Examining the Impact of Social Media Use on Chinese Male Adolescent’s Body Image: A Cross-platform Perspective. <em>74th ICA Annual Conference</em>, Gold Coast, Australia.</div></div>
  <div class="publication-card" data-detail="<h2>Performing Intimacy: Curating the Self-presentation in Human–AI Relationships</h2><br>Ever wondered what happens when private chats with an AI go public? 🤔 <br><br>We examined how users of the chatbot Replika perform their 「intimate」 relationships on social media. Turns out, it's a fascinating mix of seeking genuine validation and carefully crafting an idealized self-image. <br><br> We found that sharing these moments isn't just about the human-AI bond, but also about managing our own emotions and social standing. It's a performance for an audience. <br><br> Key questions: <br> 👏🏻 When we post about our AI companions, are we looking for connection or just applause? <br> 🤖 Does sharing these intimate moments online reinforce our self-worth, or does it feed our inner narcissist? <br><br> Here's a model of the motivations and outcomes we discovered: <br> <img src='{{ '/images/EMM_F1.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top: 1rem; margin-bottom: 1rem;'> <br>Is our AI partner just a character in the story we write about ourselves online? ✨ <br><br>Read at 👉🏻: https://journals.sagepub.com/doi/10.1177/27523543251334157">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Huang, Y. (2023). Performing Intimacy: Curating the Self- presentation in Human–AI Relationships. <em>the First Hongyi Forum</em>, Chongqing, China.<br>🥉 Third Place Award</div></div>
  <div class="publication-card" data-detail="<h2>Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach</h2><br>When a virtual idol 「hibernate」, do we say 「Goodbye」 forever, or just 「Good night」 for now? 👋😴 <br><br> We adopted data-mining to compare how young audiences react to the 「death」 of virtual uploader (VUP), human uploader (HUP), and real-world celebrity. The results are surprising! 🤯 <br><br> Mourning for VUPs is very different from for human celebrities. More interestingly, we found that human uploaders who don't show their faces are mourned more like VUPs, while those who do are mourned like real people. <br><br> This leads to some big questions about our digital lives: <br> 🤔 Are we starting to treat humans more like machines based on how 「real」 they appear online? <br> 🤖 As virtual beings become more human, are humans online becoming less so? <br><br> Our theoretical hypothesis for this is: <br> <img src='{{ '/images/VUP.png' | relative_url }}' style='width:100%; border-radius: 8px; margin-top: 1rem; margin-bottom: 1rem;'> <br> It's a fascinating look at how technology is changing our concepts of life, death, and even humanity itself. <br><br>Read at 👉🏻: https://journals.sagepub.com/doi/abs/10.1177/14614448231212822">
    <div class="publication-content"><span class="my-name">Lan, J.</span>, Mou, Y., Huang, Y. (2023). Good Night versus Goodbye? Comparing the Mourning Remarks of Virtual and Human Uploaders through A Data-mining Approach. <em>73rd ICA Annual Conference</em>, Toronto, Canada.</div></div>
</div>

<div id="popup-modal" class="modal-overlay">
  <div class="modal-content">
    <span class="close-button">&times;</span>
    <div id="modal-text">Loading...</div>
  </div>
</div>

<script>
  const modal = document.getElementById('popup-modal');
  const modalText = document.getElementById('modal-text');
  const closeBtn = document.querySelector('.close-button');

  document.querySelectorAll('.publication-card').forEach(card => {
    card.addEventListener('click', () => {
      const detail = card.getAttribute('data-detail') || 'No details available.';
      modalText.innerHTML = detail;
      modal.classList.add('show');
      modal.style.display = 'flex';
    });
  });

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('show');
    setTimeout(() => { modal.style.display = 'none'; }, 200);
  });

  modal.addEventListener('click', e => {
    if (e.target === modal) {
      modal.classList.remove('show');
      setTimeout(() => { modal.style.display = 'none'; }, 200);
    }
  });
</script>
