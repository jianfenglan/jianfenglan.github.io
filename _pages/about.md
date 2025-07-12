---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
    /* 1. 主要内容区域：提供垂直留白 */
    .page__content {
        padding-top: 12vh;
        padding-bottom: 12vh;
    }

    /* 2. 统一的文本容器：确保所有内容完美对齐 */
    .bio-container {
        max-width: 68ch;      /* 理想的阅读宽度 */
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;      /* 统一的细体 */
        line-height: 1.8;
    }

    /* 3. 开场白样式：现在是容器的一部分 */
    .bio-container .lead-greeting {
        font-size: 1.8rem;
        color: #555;
        margin-bottom: 3rem;
        text-align: left;      /* 确保在容器内是左对齐 */
    }

    /* 4. 段落样式 */
    .bio-container p {
        text-align: justify;
        margin-bottom: 1.5em;
    }
    /* 让开场白后面自动生成的空p标签不占位 */
    .bio-container .lead-greeting + p:empty {
        display: none;
    }
    .bio-container p:last-child {
        margin-bottom: 0;
    }

    /* 5. 链接样式：纯粹的颜色变化 */
    .bio-container a {
      color: #333333;
      font-weight: 300;
      text-decoration: none; /* 移除默认下划线 */
      border-bottom: none;     /* 移除所有边框 */
      transition: color 0.2s ease-in-out;
    }

    .bio-container a:hover {
      color: #002FA7;
      text-decoration: none; /* 关键：在悬浮时也强制移除下划线 */
    }

</style>

<div class="bio-container" markdown="1">

<p class="lead-greeting">Hi, this is Jeff.</p>

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [Center for Future Media & Human-Machine Communication](https://cfmhmc.github.io/), led by [Prof. Yi Mou](https://cfmhmc.github.io/yimou.github.io/).

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality.

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>
