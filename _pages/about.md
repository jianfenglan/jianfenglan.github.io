---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
    /* --- 卡片样式（已更新） --- */
    .about-card {
        background: white;
        border: 1px solid #e9e9e9;
        border-radius: 12px;
        padding: 2.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        line-height: 1.7;
        margin-bottom: 1.5rem; /* 新增：为卡片之间创建垂直间距 */
    }

    /* 最后一个卡片不需要底部间距 */
    .about-card:last-child {
        margin-bottom: 0;
    }

    .about-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    /* --- 样式结束 --- */


    /* 为主要内容区域设置 Flexbox 布局来实现垂直居中 */
    .page__content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 8vh;
        padding-bottom: 4vh;
        min-height: auto;
    }

    /* 为本页面的正文段落设置两端对齐 */
    .page__content p {
        text-align: justify;
    }
    
    .page__content h2 {
        margin-top: 2.5rem;
    }

    /* 链接样式 */
    .page__content a {
      color: #333333;
      font-weight: 400;
      text-decoration: none;
      border-bottom: none;
      transition: color 0.2s ease-in-out;
    }

    .page__content a:hover {
      color: #002FA7;
      background-image: none;
      text-decoration: none;
    }

</style>

<div class="about-card" markdown="1">
Hi, this is Jeff.
</div>

<div class="about-card" markdown="1">
I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [**Center for Future Media & Human-Machine Communication**](https://cfmhmc.github.io/), led by [**Prof. Yi Mou**](https://cfmhmc.github.io/yimou.github.io/).
</div>

<div class="about-card" markdown="1">
My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality. Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.
</div>
