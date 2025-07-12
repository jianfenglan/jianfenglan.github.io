---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
    /* 1. 主要内容区域：提供一个简洁的垂直布局和上下留白 */
    .page__content {
        padding-top: 12vh;     /* 舒适的顶部留白 */
        padding-bottom: 12vh;
    }

    /* 2. 开场白样式：保持优雅，但恢复左对齐 */
    .lead-greeting {
        font-size: 1.8rem;
        font-weight: 300;      /* 您喜欢的细体 */
        color: #555;
        margin-bottom: 3rem;
        /* --- 以下三行确保它和下方的正文容器宽度一致并居中 --- */
        max-width: 68ch;
        margin-left: auto;
        margin-right: auto;
    }

    /* 3. 正文容器：为所有文本设定统一的细体和布局 */
    .bio-text-container {
        max-width: 68ch;      /* 限制阅读宽度 */
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;      /* 关键：将细体应用到所有段落 */
        line-height: 1.8;      /* 舒适的行高 */
    }

    /* 4. 段落样式 */
    .bio-text-container p {
        text-align: justify;
        margin-bottom: 1.5em;
    }
    .bio-text-container p:last-child {
        margin-bottom: 0;
    }

    /* 5. 链接样式：同样使用细体，并保留点状下划线 */
    .bio-text-container a {
      color: #333333;
      text-decoration: none;
      font-weight: 300;        /* 关键：确保链接也是细体 */
      border-bottom: 1px dotted rgba(0, 0, 0, 0.3);
      padding-bottom: 2px;
      transition: all 0.2s ease-in-out;
    }

    .bio-text-container a:hover {
      color: #002FA7;
      border-bottom-color: #002FA7;
    }

</style>

<p class="lead-greeting">Hi, this is Jeff.</p>

<div class="bio-text-container" markdown="1">

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [Center for Future Media & Human-Machine Communication](https://cfmhmc.github.io/), led by [Prof. Yi Mou](https://cfmhmc.github.io/yimou.github.io/).

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality.

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>
