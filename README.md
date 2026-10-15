# Qiming Zhu · 朱淇铭

中文默认的双语学术主页，基于 [w-r-s/academic-homepage-template](https://github.com/w-r-s/academic-homepage-template) 的布局重新整理。

- [中文网站](https://qiming-zhu.github.io/)
- [English](https://qiming-zhu.github.io/en/)
- [GitHub 个人资料页 README](profile/README.md)

## 本地预览

```sh
python3 build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8765/`。网站只有静态 HTML、CSS、JavaScript，不需要安装前端依赖。

## 更新内容

- `content.json`：论文、作者、链接、配图和中英文简介。
- `build.py`：中英文个人介绍、教育信息和页面模板。
- `images/me.jpg`：用户提供的照片；页面仅通过 CSS 控制展示范围，原图保留。
- `images/research/`：研究配图，点击后可查看原图。
- `stylesheet.css`：样式和手机布局。
- `site.js`：语言选择、配图放大。

修改数据或模板后运行 `python3 build.py`，提交两个生成的页面。Pages 使用 `main` 分支的根目录；`.nojekyll` 保证按静态文件部署。

现已采用两个仓库的布局：`Qiming-Zhu/Qiming-Zhu` 用于 GitHub 个人资料页，`Qiming-Zhu/qiming-zhu.github.io` 用于独立网站。网站根地址为 `https://qiming-zhu.github.io/`，英文版位于 `/en/`。

## GitHub 个人资料页

在 `Qiming-Zhu/Qiming-Zhu` 公开仓库根目录放入 `profile/README.md` 的内容，即可显示在 GitHub 账号主页。该同名仓库与网站仓库用途不同。

## 内容范围

当前只展示个人介绍、研究和教育背景。没有实习、工作经历、电话、GPA 或完整简历。OS-native Agents 尚无 arXiv，页面只展示公开项目主页与演示；其代码仓库目前未公开，页面不生成不可访问的代码链接。

配图和模板来源见 [UPSTREAM.md](UPSTREAM.md)。
