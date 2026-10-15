#!/usr/bin/env python3
"""Generate the two static language pages from content.json. Python stdlib only."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'content.json').read_text())
URL = DATA['site_url'].rstrip('/') + '/'

TEXT = {
 'zh': {
  'name': '朱淇铭', 'other_name': 'Qiming Zhu', 'title': '朱淇铭 · Qiming Zhu',
  'nav': ['关于', '研究', '教育'], 'skip': '跳到主要内容',
  'intro': '我是<a href="https://www.cuhk.edu.cn/" target="_blank" rel="noopener noreferrer">香港中文大学（深圳）</a>人工智能学院的人工智能研究型硕士生，导师为<a href="https://wabyking.github.io/" target="_blank" rel="noopener noreferrer">王本友</a>教授。',
  'focus': '我致力于推进<strong>个性化智能体（Personalized Agents）</strong>，让 working agents 和 mobile agents 在工作与日常生活中，成为理解个人、持续协作的伙伴。',
  'motivation': '<p><strong>更懂你。</strong>我研究长期记忆（memory），并探索 RSI，希望 Agent 能从交互历史与反馈中积累经验，更好地理解个人偏好和需求，持续改进协作方式。</p><p><strong>更能处理和管理任务。</strong>通过 OS-native 支持，我探索如何让 Agent 在需求与环境变化时，持续跟踪目标、协调跨时间与跨应用的任务；多轮交互评测则帮助我检验这些能力是否真正服务于用户。</p>',
  'vision': '期待和你一起探索、一起构建，逐步走向我们想象中的 <strong>JARVIS</strong>。',
  'research': '研究工作', 'research_en': 'Selected research',
  'research_note': '以记忆、任务管理与交互评测，探索个性化智能体。',
  'education': '教育背景', 'education_en': 'Education',
  'edu': [('2025.09 — 至今', '香港中文大学（深圳）', '人工智能研究型硕士 · 人工智能学院', '导师：王本友教授'), ('2020.09 — 2024.07', '西安交通大学', '数学与应用数学 · 理学学士', '')],
  'project': '项目主页', 'paper': '论文', 'code': '代码', 'demo': '在线演示', 'dataset': '数据集',
  'private': '代码暂未公开', 'figure': '查看完整研究配图', 'close': '关闭图片',
  'image_hint': '点击图片放大', 'portrait': '朱淇铭在海边看日落',
  'contact': '欢迎交流个性化智能体相关研究与实践。',
  'footer': '基于', 'template': '学术主页模板', 'updated': '更新于 2026 年 10 月',
  'description': '朱淇铭，香港中文大学（深圳）人工智能研究型硕士生。致力于推进个性化智能体，探索 memory、RSI、OS-native 与多轮交互评测。',
 },
 'en': {
  'name': 'Qiming Zhu', 'other_name': '朱淇铭', 'title': 'Qiming Zhu · 朱淇铭',
  'nav': ['About', 'Research', 'Education'], 'skip': 'Skip to main content',
  'intro': 'I am a research master’s student in Artificial Intelligence at <a href="https://www.cuhk.edu.cn/en" target="_blank" rel="noopener noreferrer">The Chinese University of Hong Kong, Shenzhen</a>, advised by <a href="https://wabyking.github.io/" target="_blank" rel="noopener noreferrer">Prof. Benyou Wang</a>.',
  'focus': 'I aim to advance <strong>Personalized Agents</strong>: working agents and mobile agents that understand individuals and collaborate with them over time, across work and everyday life.',
  'motivation': '<p><strong>Understanding you better.</strong> I study long-term memory and explore RSI, with the goal of helping agents learn from interaction history and feedback, understand personal preferences and needs, and improve how they collaborate.</p><p><strong>Handling and managing tasks better.</strong> Through OS-native support, I explore agents that track goals and coordinate tasks over time and across applications as user needs and environments evolve. Multi-turn interaction evaluation helps me examine whether these capabilities truly serve the user.</p>',
  'vision': 'Let’s explore and build together, taking steps toward the <strong>JARVIS</strong> we envision.',
  'research': 'Selected research', 'research_en': 'Research',
  'research_note': 'Exploring personalized agents through memory, task management, and interaction evaluation.',
  'education': 'Education', 'education_en': 'Background',
  'edu': [('Sep 2025 — Present', 'The Chinese University of Hong Kong, Shenzhen', 'Research master’s in Artificial Intelligence · School of AI', 'Advisor: Prof. Benyou Wang'), ('Sep 2020 — Jul 2024', 'Xi’an Jiaotong University', 'B.Sc. in Mathematics and Applied Mathematics', '')],
  'project': 'Project', 'paper': 'Paper', 'code': 'Code', 'demo': 'Live demo', 'dataset': 'Dataset',
  'private': 'Code not yet public', 'figure': 'View full research figure', 'close': 'Close image',
  'image_hint': 'Click to enlarge', 'portrait': 'Qiming Zhu watching the sunset by the sea',
  'contact': 'Happy to connect about personalized agents, in research and practice.',
  'footer': 'Adapted from', 'template': 'academic homepage template', 'updated': 'Updated October 2026',
  'description': 'Qiming Zhu is an AI research master’s student at CUHK-Shenzhen, advancing personalized agents through memory, RSI, OS-native support, and multi-turn interaction evaluation.',
 }
}

def external(url, label, cls=''):
    return f'<a class="{cls}" href="{e(url, quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>'

for lang, t in TEXT.items():
    prefix = '' if lang == 'zh' else '../'
    page_url = URL + ('' if lang == 'zh' else 'en/')
    opposite = 'en/' if lang == 'zh' else '../'
    cards = []
    for p in DATA['publications']:
        author_names = [f'<strong>{e(a)}</strong>' if a == 'Qiming Zhu' else e(a) for a in p['authors']]
        authors = ', '.join(author_names)
        links = []
        for key in ['homepage', 'paper', 'code', 'demo', 'dataset']:
            if p.get(key):
                if key == 'code' and p.get('code_visibility') == 'private':
                    links.append(f'<span class="link-unavailable">{t["private"]}</span>')
                else:
                    labels = {'homepage': 'project'}
                    links.append(external(p[key], t[labels.get(key, key)], 'resource-link'))
        title_url = p.get('paper') or p['homepage']
        img = prefix + p['image']
        cards.append(f'''
        <article class="publication" id="{e(p['id'])}">
          <a class="research-figure" href="{e(img)}" data-lightbox aria-label="{t['figure']}: {e(p['short_title'])}">
            <img src="{e(img)}" alt="{e(p['image_alt'][lang])}" loading="lazy" decoding="async" width="{p['image_width']}" height="{p['image_height']}">
            <span class="figure-hint">{t['image_hint']} ↗</span>
          </a>
          <div class="publication-copy">
            <div class="paper-meta"><span>{e(p['venue'])}</span><span>{e(p['role'][lang])}</span></div>
            <h3>{external(title_url, e(p['title']))}</h3>
            <p class="authors">{authors}</p>
            <p class="summary">{e(p['summary'][lang])}</p>
            <div class="resource-links">{''.join(links)}</div>
          </div>
        </article>''')
    education_rows = []
    for date, school, degree, advisor in t['edu']:
        advisor_html = '<p class="advisor">' + e(advisor) + '</p>' if advisor else ''
        education_rows.append(f'<li><time>{e(date)}</time><div><h3>{e(school)}</h3><p>{e(degree)}</p>{advisor_html}</div></li>')
    education = ''.join(education_rows)
    nav = ''.join(f'<a href="#{section}">{label}</a>' for section, label in zip(['about', 'research', 'education'], t['nav']))
    jsonld = json.dumps({'@context': 'https://schema.org', '@type': 'Person', 'name': 'Qiming Zhu', 'alternateName': '朱淇铭', 'url': URL, 'image': URL+'images/me.jpg', 'affiliation': {'@type': 'CollegeOrUniversity', 'name': 'The Chinese University of Hong Kong, Shenzhen'}, 'sameAs': ['https://github.com/Qiming-Zhu', 'https://scholar.google.com/citations?user=vwQ1_0AAAAAJ']}, ensure_ascii=False)
    html = f'''<!doctype html>
<html lang="{'zh-CN' if lang == 'zh' else 'en'}" data-language="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>{t['title']} | {'个人主页' if lang == 'zh' else 'Personal website'}</title>
  <meta name="description" content="{e(t['description'])}">
  <meta name="author" content="Qiming Zhu">
  <link rel="canonical" href="{e(page_url)}">
  <link rel="alternate" hreflang="zh-CN" href="{e(URL)}">
  <link rel="alternate" hreflang="en" href="{e(URL+'en/')}">
  <link rel="alternate" hreflang="x-default" href="{e(URL)}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{t['title']}">
  <meta property="og:description" content="{e(t['description'])}">
  <meta property="og:url" content="{e(page_url)}">
  <meta property="og:image" content="{e(URL+'images/me.jpg')}">
  <meta property="og:locale" content="{'zh_CN' if lang == 'zh' else 'en_US'}">
  <meta name="twitter:card" content="summary">
  <link rel="stylesheet" href="{prefix}stylesheet.css">
  <script type="application/ld+json">{jsonld}</script>
  <script>
  try {{
    const explicit = new URL(location.href).searchParams.get('lang');
    const saved = localStorage.getItem('qiming-language');
    if (explicit === 'zh' || explicit === 'en') localStorage.setItem('qiming-language', explicit);
    else if ('{lang}' === 'en') localStorage.setItem('qiming-language', 'en');
    else if (saved === 'en') location.replace('en/?lang=en' + location.hash);
  }} catch (_) {{}}
  </script>
  <script src="{prefix}site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">{t['skip']}</a>
  <header class="site-header"><div class="header-inner">
    <nav aria-label="{'主导航' if lang == 'zh' else 'Main navigation'}">{nav}</nav>
    <div class="language-switch" aria-label="{'语言选择' if lang == 'zh' else 'Language'}">
      <a href="{'' if lang == 'zh' else '../'}?lang=zh" lang="zh-CN" data-language-link="zh" {'aria-current="page"' if lang == 'zh' else ''}>中文</a>
      <span aria-hidden="true">/</span>
      <a href="{'en/' if lang == 'zh' else ''}?lang=en" lang="en" data-language-link="en" {'aria-current="page"' if lang == 'en' else ''}>EN</a>
    </div>
  </div></header>
  <main id="main" class="page">
    <section id="about" class="about-section" aria-labelledby="name">
      <div class="bio">
        <p class="eyebrow">PERSONALIZED AGENTS</p>
        <h1 id="name">{t['name']}<span class="other-name">{t['other_name']}</span></h1>
        <p>{t['intro']}</p><p>{t['focus']}</p>
        <div class="motivation">{t['motivation']}</div>
        <p class="vision">{t['vision']}</p>
        <div class="contact-links">
          <a href="mailto:225085006@link.cuhk.edu.cn">Email <span aria-hidden="true">↗</span></a>
          {external('https://scholar.google.com/citations?user=vwQ1_0AAAAAJ', 'Google Scholar <span aria-hidden="true">↗</span>')}
          {external('https://github.com/Qiming-Zhu', 'GitHub <span aria-hidden="true">↗</span>')}
        </div>
      </div>
      <figure class="portrait"><img src="{prefix}images/me.jpg" width="1212" height="808" alt="{t['portrait']}" fetchpriority="high"><figcaption>Qiming Zhu · 朱淇铭</figcaption></figure>
    </section>
    <section id="research" class="research-section" aria-labelledby="research-title">
      <div class="section-heading"><h2 id="research-title">{t['research']}</h2><span>{t['research_en']}</span></div>
      <p class="section-note">{t['research_note']}</p>
      <div class="publications">{''.join(cards)}</div>
    </section>
    <section id="education" class="education-section" aria-labelledby="education-title">
      <div class="section-heading"><h2 id="education-title">{t['education']}</h2><span>{t['education_en']}</span></div>
      <ol class="education-list">{education}</ol>
    </section>
    <footer class="site-footer">
      <p class="footer-contact">{t['contact']} <a href="mailto:225085006@link.cuhk.edu.cn">Email ↗</a></p>
      <div><span>© 2026 Qiming Zhu</span><span>{t['updated']}</span></div>
      <p class="template-credit">{t['footer']} {external('https://github.com/w-r-s/academic-homepage-template', t['template'])}</p>
    </footer>
  </main>
  <dialog id="image-viewer" aria-label="{t['figure']}"><button class="viewer-close" type="button" aria-label="{t['close']}">×</button><img alt=""><p></p></dialog>
</body></html>
'''
    output = ROOT / ('index.html' if lang == 'zh' else 'en/index.html')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html)
print('Built index.html and en/index.html')
