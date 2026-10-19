# 网站维护约定

个人站：Jekyll + academicpages 主题，GitHub Pages legacy 构建，域名 jefflan.blue。

## 铁律

1. **永不直接改 main、永不直接 push main。**
2. 任何改动都走分支：`dsh/<简短描述>`。
3. 推送分支后，必须给用户可确认的证据（云端构建产物截图），等用户明确说「合并 / 推到 main」再合并。
4. 合并后确认 Pages 构建成功，再把线上链接给用户。
5. 每次改动说明改了哪个文件、为什么。

## 预览流程

- push 到 `dsh/**` 自动触发 `.github/workflows/preview.yml`。
- workflow 在 runner 内用 Jekyll（GitHub Pages 同款镜像）构建，起 `http.server`，用 Playwright 对 `/`、`/research/`、`/plog/`、`/elsewhere/` 各截桌面 1440 宽与移动 390 宽两张全页图，上传为 artifact `preview-shots`。
- 本地取回：`gh run download <run-id> -n preview-shots -D /tmp/shots`
- 只回传 PNG/JPEG 截图（几 MB），不回传整站产物（100MB+，会超时）。

## 环境现状

- 本机无 Homebrew、无 Docker，系统 Ruby 2.6 装不了 `github-pages` gem，**不能本地构建 Jekyll**；预览一律走 CI。
- 本机截图可用：`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless=new`。

## 仓库现状（2026-10）

- 约 222MB，`.git` 占 224MB（29 个历史分支 `archive/*`、`work/*`），谨慎 `git gc` 与历史重写。
- 无 `_posts` 目录。内容在各页面：`research.md`、`plog.md`、`elsewhere.md`、`_pages/about.md`；全局配置在 `_config.yml`；导航在 `_data/navigation.yml`。
- `images/news/NCA25.JPG` 曾与 `NCA25.jpg` 大小写冲突（macOS 只能存一个），已删除未被引用的 `.jpg`。macOS 上勿盲用 `git add -A`。
