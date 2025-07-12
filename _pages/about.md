---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
    /* 1. 主要内容区域：创造一个大的垂直留白区域 */
    .page__content {
        display: flex;
        flex-direction: column;
        justify-content: center; /* 让内容块在垂直方向上居中 */
        min-height: 70vh;      /* 确保内容区域至少有视窗高度的70%，为居中留出足够空间 */
        padding: 4vh 0;
    }

    /* 2. 开场白样式：突出 "Hi, this is Jeff." */
    .lead-greeting {
        font-size: 1.8rem;     /* 更大的字号 */
        font-weight: 300;      /* 更细的字体，显得更优雅 */
        color: #555;           /* 柔和的深灰色 */
        text-align: center;    /* 居中显示 */
        margin-bottom: 3rem;   /* 和下方的正文拉开足够的距离 */
    }

    /* 3. 正文容器：实现最佳阅读行宽和呼吸感 */
    .bio-text-container {
        max-width: 68ch;       /* 核心：将最大宽度限制在约68个字符，这是最理想的阅读行宽 */
        margin-left: auto;     /* 配合上一条，实现水平居中 */
        margin-right: auto;    /* 配合上一条，实现水平居中 */
        line-height: 1.8;      /* 增加行高，创造段落的“呼吸感” */
    }

    /* 4. 正文段落：两端对齐并增加段间距 */
    .bio-text-container p {
        text-align: justify;
        margin-bottom: 1.5em; /* 增加段落之间的距离 */
    }
    .bio-text-container p:last-child {
        margin-bottom: 0;
    }

    /* 5. 链接样式：在简洁基础上增加精致的交互细节 */
    .bio-text-container a {
      color: #333333;
      text-decoration: none;
      /* 默认状态下是一条非常浅的虚线，几乎不可见，但暗示了可点击 */
      border-bottom: 1px dotted rgba(0, 0, 0, 0.2);
      padding-bottom: 2px;
      transition: all 0.2s ease-in-out;
    }

    /* 鼠标悬浮时，颜色变蓝，下划线变实线并更明显 */
    .bio-text-container a:hover {
      color: #002FA7;
      border-bottom-color: #002FA7;
    }

</style>

<p class="lead-greeting">Hi, this is Jeff.</p>

<div class="bio-text-container" markdown="1">

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [**Center for Future Media & Human-Machine Communication**](https://cfmhmc.github.io/), led by [**Prof. Yi Mou**](https://cfmhmc.github.io/yimou.github.io/). 

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality. 

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>
