---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
    /* 1. 主要内容区域 */
    .page__content {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* 2. 统一的文本容器 */
    .bio-container {
        max-width: 68ch;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.8;
    }

    /* 3. 段落样式 */
    .bio-container p {
        text-align: justify;
        margin-bottom: 1.5em;
    }
    .bio-container p:last-child {
        margin-bottom: 0;
    }

    /* 4. 链接样式 */
    .bio-container a {
      color: #333333;
      text-decoration: none;
      font-weight: 400;
      border-bottom: none;
      transition: color 0.2s ease-in-out;
    }

    .bio-container a:hover {
      color: #002FA7;
      text-decoration: none; 
    }

    /* 5. 修改：机构Logo图片样式 */
    .affiliation-image {
      display: block; /* 将图片设置为块级元素以应用外边距 */
      max-width: 100%; /* 图片最大宽度调整为100%，以铺满容器 */
      height: auto;   /* 高度自动，保持图片比例 */
      margin: 3em auto 0; /* 上方外边距为3em，左右自动以实现居中 */
      pointer-events: none; /* 使图片不可点击，并禁用所有鼠标交互（如悬停效果） */
    }

</style>

<div class="bio-container" markdown="1">

Hi, this is Jeff.

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [**Center for Future Media & Human-Machine Communication**](https://cfmhmc.github.io/), advised by [**Prof. Yi Mou**](https://cfmhmc.github.io/yimou.github.io/).

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality.

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>

<!-- 新增的图片 -->
<img src="/images/affiliation.jpg" alt="Affiliations Logo" class="affiliation-image">
