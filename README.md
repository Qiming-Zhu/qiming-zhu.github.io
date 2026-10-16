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

- `content.json`：论文、作者、公开状态、链接和中英文简介；`contribution` 为卡片加粗的贡献概括。
- `build.py`：中英文个人介绍、教育信息和页面模板。
- `images/me.jpg`：用户提供的照片；页面仅通过 CSS 控制展示范围，原图保留。
- `images/research/`：卡片与放大视图均使用原始研究配图，不重新绘制或替换。
- `stylesheet.css`：样式和手机布局。
- `site.js`：语言选择、配图放大。

修改数据或模板后运行 `python3 build.py`，提交两个生成的页面。Pages 使用 `main` 分支的根目录；`.nojekyll` 保证按静态文件部署。

现已采用两个仓库的布局：`Qiming-Zhu/Qiming-Zhu` 用于 GitHub 个人资料页，`Qiming-Zhu/qiming-zhu.github.io` 用于独立网站。网站根地址为 `https://qiming-zhu.github.io/`，英文版位于 `/en/`。

## GitHub 个人资料页

在 `Qiming-Zhu/Qiming-Zhu` 公开仓库根目录放入 `profile/README.md` 的内容，即可显示在 GitHub 账号主页。该同名仓库与网站仓库用途不同。

## 内容范围

当前只展示个人介绍、研究和教育背景。没有实习、工作经历、电话、GPA 或完整简历。OS-native Agents 尚无 arXiv，页面只展示公开项目主页与演示；其代码仓库目前未公开，页面不生成不可访问的代码链接。

配图和模板来源见 [UPSTREAM.md](UPSTREAM.md)。

## 私有访问统计

中英文页面共用一个 [GoatCounter](https://www.goatcounter.com/) 账号，已配置为 `qiming-zhu`。更换账号时，将 `content.json` 中的 `analytics.goatcounter_code` 填为后台地址的子域名（例如后台为 `https://example.goatcounter.com`，则只填 `example`），再运行 `python3 build.py` 并发布。留空表示不加载统计脚本。

后台必须保持以下设置：

- **Dashboard viewable by → Only logged in users**，不创建共享链接、不添加其他用户。
- **Allow adding visitor counts on your website** 不勾选，避免通过公开计数接口读取访问量。
- **Sites that can embed GoatCounter** 留空。

网站不展示计数器或后台入口。网页源码中的统计地址是公开的收集入口，不能用于读取私有报表；密码、验证码和 API key 不应放入本项目。统计从接入后开始，来源网站可能因浏览器不发送 Referrer 而显示未知。

发布后须用不带登录 Cookie 的请求确认：后台跳转登录页，`/counter/TOTAL.json` 返回 403，`/api/v0/stats/total` 返回 401；再登录后台确认真实页面访问能够入账。
