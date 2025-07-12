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
        padding-top: 3rem;
        padding-bottom: 10vh;
    }

    /* 2. 统一的文本容器：为所有文本设定样式 */
    .bio-container {
        max-width: 68ch;      /* 理想的阅读宽度 */
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;      /* 正文统一使用细体 */
        line-height: 1.8;
    }

    /* 3. 段落样式 */
    .bio-container p {
        text-align: justify;
        margin-bottom: 1.5em; /* 段落之间的间距 */
    }
    .bio-container p:last-child {
        margin-bottom: 0;
    }

    /* 4. 链接样式：通过字重来区分 */
    .bio-container a {
      color: #333333;
      text-decoration: none;
      font-weight: 400;        /* 关键：链接使用常规字重，比细体正文更突出 */
      border-bottom: none;
      transition: color 0.2s ease-in-out;
    }

    .bio-container a:hover {
      color: #002FA7;
      text-decoration: none; 
    }

</style>

<div class="bio-container" markdown="1">
Hi, this is Jeff.

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [Center for Future Media & Human-Machine Communication](https://cfmhmc.github.io/), led by [Prof. Yi Mou](https://cfmhmc.github.io/yimou.github.io/).

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality.

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>
