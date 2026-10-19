import { chromium } from 'playwright';

const BASE = 'http://127.0.0.1:8080';
const pages = [
  ['home', '/'],
  ['research', '/research/'],
  ['plog', '/plog/'],
  ['elsewhere', '/elsewhere/'],
];
const viewports = [
  ['desktop', { width: 1440, height: 1000 }],
  ['mobile', { width: 390, height: 844 }],
];

const browser = await chromium.launch();
for (const [name, path] of pages) {
  for (const [tag, vp] of viewports) {
    const page = await browser.newPage({ viewport: vp, deviceScaleFactor: 1 });
    await page.goto(BASE + path, { waitUntil: 'networkidle' });
    // 让懒加载图片有机会进入可视区
    await page.evaluate(async () => {
      await new Promise((resolve) => {
        let y = 0;
        const step = () => {
          y += window.innerHeight;
          window.scrollTo(0, y);
          if (y < document.body.scrollHeight) setTimeout(step, 120);
          else { window.scrollTo(0, 0); setTimeout(resolve, 400); }
        };
        step();
      });
    });
    const height = await page.evaluate(() => Math.max(document.body.scrollHeight, document.documentElement.scrollHeight));
    const tall = height > 6000;
    await page.screenshot({
      path: `shots/${name}-${tag}.${tall ? 'jpg' : 'png'}`,
      fullPage: true,
      ...(tall ? { type: 'jpeg', quality: 85 } : {}),
    });
    console.log(`${name}-${tag} ok  ${vp.width}x${height}${tall ? ' (jpeg)' : ''}`);
    await page.close();
  }
}
await browser.close();
