---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
    /* --- 新增的卡片样式 --- */
    .about-card {
        background: white; /* 卡片背景色 */
        border: 1px solid #e9e9e9; /* 边框颜色 */
        border-radius: 12px; /* 圆角大小 */
        padding: 2.5rem; /* 内边距，让文字和边框有呼吸感 */
        box-shadow: 0 2px 8px rgba(0,0,0,0.06); /* 阴影效果 */
        transition: transform 0.2s ease, box-shadow 0.2s ease; /* 悬浮动画过渡 */
        line-height: 1.7; /* 调整行高，阅读更舒适 */
    }

    /* 鼠标悬浮在卡片上时的“上浮”效果 */
    .about-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    /* --- 新增样式结束 --- */


    /* 为主要内容区域设置 Flexbox 布局来实现垂直居中 */
    .page__content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 8vh; /* 顶部留白 */
        padding-bottom: 4vh; /* 底部留白 */
        min-height: auto; /* 移除强制的最小高度 */
    }

    /* 为本页面的正文段落设置两端对齐 */
    .page__content p {
        text-align: justify;
    }
    
    /* 为主要标题上方增加间距 */
    .page__content h2 {
        margin-top: 2.5rem;
    }

    /* --- 这是为你最终定制的链接样式 --- */
    /* 链接的默认样式 */
    .page__content a {
      color: #333333; /* 默认使用深灰色 */
      font-weight: 400; /* 保持常规粗细 */
      text-decoration: none; /* 移除所有默认下划线 */
      border-bottom: none; /* 移除所有边框 */
      transition: color 0.2s ease-in-out; /* 只让颜色变化有过渡效果 */
    }

    /* 鼠标悬浮在链接上时的样式 */
    .page__content a:hover {
      color: #002FA7; /* 鼠标悬浮时变为克莱因蓝 */
      background-image: none; /* 在悬浮时，移除背景图片，即移除点状虚线 */
      text-decoration: none; /* 再次强调不要任何下划线 */
    }

</style>

<div class="about-card">

Hi, this is Jeff.

I'm a Ph.D. candidate (in the combined Master-Ph.D. program) at the School of Media and Communication, Shanghai Jiao Tong University, and a member of the [**Center for Future Media & Human-Machine Communication**](https://cfmhmc.github.io/), led by [**Prof. Yi Mou**](https://cfmhmc.github.io/yimou.github.io/). 

My research focuses on human-AI interaction's impact on emerging media users' perception of intimacy and digital immortality. 

Before joining SJTU, I received my B.A. in Journalism from the School of Journalism, Chongqing University.

</div>
