# 网站维护约定

个人站：Jekyll + academicpages 主题，GitHub Pages legacy 构建，域名 jefflan.blue。

## 铁律

1. **永不直接改 main、永不直接 push main。**
2. 任何改动都走分支：`dsh/<简短描述>`。
3. 推送分支后，必须给用户可确认的证据（云端构建产物截图），等用户明确说「合并 / 推到 main」再合并。
4. 合并后确认 Pages 构建成功，再把线上链接给用户。
5. 每次改动说明改了哪个文件、为什么。

## 预览流程

- push 到 `dsh/**` 自动触发 `.github/workflows/preview.yml`，产出 artifact `preview-site`。
- 本地取回：`gh run download <run-id> -n preview-site -D /tmp/preview`
- 起服务：`python3 -m http.server` 于产物目录，Chrome headless 截图（1440x900 桌面 + 390x844 移动）。

## 仓库现状（2026-10）

- 约 222MB，`.git` 占 224MB（29 个历史分支 `archive/*`、`work/*`），谨慎 `git gc` 与历史重写。
- 无 `_posts` 目录。内容在各页面：`research.md`、`plog.md`、`elsewhere.md`、`_pages/about.md`；全局配置在 `_config.yml`；导航在 `_data/navigation.yml`。
- `images/news/NCA25.JPG` 曾与 `NCA25.jpg` 大小写冲突（macOS 只能存一个），已删除未被引用的 `.jpg`。macOS 上勿盲用 `git add -A`。
