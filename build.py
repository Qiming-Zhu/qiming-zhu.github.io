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
  'intro': '我是<a href="https://www.cuhk.edu.cn/" target="_blank" rel="noopener noreferrer">香港中文大学（深圳）</a>人工智能学院的研究型硕士生，导师为<a href="https://wabyking.github.io/" target="_blank" rel="noopener noreferrer">王本友</a>教授。',
  'focus': '我的研究方向是<strong>个性化智能体（Personalized Agents）</strong>。我希望构建能够在长期交互中理解用户、持续管理任务，并从经验与反馈中改进的智能伙伴，服务于工作与日常生活。',
  'current_work': '目前，我主要关注<strong>长期记忆与持续任务管理</strong>：通过 <a href="#tiermem">TierMem</a>，探索智能体如何高效利用历史交互，同时保留重要细节；通过 <a href="#os-native">OS-native Agents</a>，研究智能体持续协调跨应用任务所需的操作系统支持。我也参与多轮语音交互评测 <a href="#mtalk">MTalk-Bench</a>，研究如何可靠地衡量模型的交互能力。',
  'vision': '希望有一天，这些研究能帮助我们一起构建真正可以长期共事的 <strong>JARVIS</strong>。',
  'research': '研究工作', 'research_en': 'Selected research',
  'education': '教育背景', 'education_en': 'Education',
  'edu': [('2025.09 — 至今', '香港中文大学（深圳）', '人工智能研究型硕士 · 人工智能学院', '导师：王本友教授'), ('2020.09 — 2024.07', '西安交通大学', '数学与应用数学 · 理学学士', '')],
  'project': '项目主页', 'paper': '论文', 'code': '代码', 'demo': '在线演示', 'dataset': '数据集',
  'figure': '查看完整研究配图', 'close': '关闭图片',
  'image_hint': '查看完整框架图', 'portrait': '朱淇铭在海边看日落',
  'contact': '欢迎交流个性化智能体、长期记忆与人机协作相关的研究和实践。',
  'footer': '基于', 'template': '学术主页模板', 'updated': '更新于 2026 年 10 月',
  'description': '朱淇铭，香港中文大学（深圳）研究型硕士生。研究个性化智能体，关注长期记忆、持续任务管理与多轮交互评测，探索能够长期理解用户的智能伙伴。',
 },
 'en': {
  'name': 'Qiming Zhu', 'other_name': '朱淇铭', 'title': 'Qiming Zhu · 朱淇铭',
  'nav': ['About', 'Research', 'Education'], 'skip': 'Skip to main content',
  'intro': 'I am a master’s student in the School of Artificial Intelligence at <a href="https://www.cuhk.edu.cn/en" target="_blank" rel="noopener noreferrer">The Chinese University of Hong Kong, Shenzhen</a>, advised by <a href="https://wabyking.github.io/" target="_blank" rel="noopener noreferrer">Prof. Benyou Wang</a>.',
  'focus': 'My research focuses on <strong>personalized AI agents</strong>. I aim to build agents that understand their users over time, reliably manage ongoing tasks, and learn from experience and feedback, in work and everyday life.',
  'current_work': 'My current work focuses on <strong>long-term memory and ongoing task management</strong>. In <a href="#tiermem">TierMem</a>, I study how agents can use interaction history efficiently while retaining important details. In <a href="#os-native">OS-native Agents</a>, I explore the operating system support needed for agents to manage ongoing tasks across applications. I also work on reliable evaluation of multi-turn spoken interaction through <a href="#mtalk">MTalk-Bench</a>.',
  'vision': 'I hope these efforts bring us closer to building a <strong>JARVIS</strong> we can work with over the long term.',
  'research': 'Selected research', 'research_en': '',
  'education': 'Education', 'education_en': '',
  'edu': [('Sep 2025 — Present', 'The Chinese University of Hong Kong, Shenzhen', 'Research master’s in Artificial Intelligence · School of AI', 'Advisor: Prof. Benyou Wang'), ('Sep 2020 — Jul 2024', 'Xi’an Jiaotong University', 'B.Sc. in Mathematics and Applied Mathematics', '')],
  'project': 'Project', 'paper': 'Paper', 'code': 'Code', 'demo': 'Live demo', 'dataset': 'Dataset',
  'figure': 'View full research figure', 'close': 'Close image',
  'image_hint': 'View full framework', 'portrait': 'Qiming Zhu watching the sunset by the sea',
  'contact': 'I welcome conversations and collaborations on personalized agents, agent memory, and human–AI interaction.',
  'footer': 'Adapted from', 'template': 'academic homepage template', 'updated': 'Updated October 2026',
  'description': 'Qiming Zhu is a master’s student at CUHK-Shenzhen researching personalized AI agents, with a focus on long-term memory, ongoing task management, and multi-turn interaction evaluation.',
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
                    continue
                else:
                    labels = {'homepage': 'project'}
                    links.append(external(p[key], t[labels.get(key, key)], 'resource-link'))
        title_url = p.get('paper') or p['homepage']
        img = prefix + p['image']
        thumbnail = prefix + p.get('thumbnail', p['image'])
        cards.append(f'''
        <article class="publication" id="{e(p['id'])}">
          <a class="research-figure" href="{e(img)}" data-lightbox data-figure-caption="{e(p['image_alt'][lang], quote=True)}" aria-label="{t['figure']}: {e(p['short_title'])}">
            <img src="{e(thumbnail)}" alt="{e(p['thumbnail_alt'][lang])}" loading="lazy" decoding="async" width="448" height="300">
            <span class="figure-hint">{t['image_hint']} ↗</span>
          </a>
          <div class="publication-copy">
            <div class="paper-meta"><span>{e(p['status'][lang])}</span></div>
            <h3>{external(title_url, e(p['title']))}</h3>
            <p class="authors">{authors}</p>
            <p class="summary"><strong>{e(p['contribution'][lang])}</strong> {e(p['summary'][lang])}</p>
            <div class="resource-links">{''.join(links)}</div>
          </div>
        </article>''')
    education_rows = []
    for date, school, degree, advisor in t['edu']:
        advisor_html = '<p class="advisor">' + e(advisor) + '</p>' if advisor else ''
        education_rows.append(f'<li><time>{e(date)}</time><div><h3>{e(school)}</h3><p>{e(degree)}</p>{advisor_html}</div></li>')
    education = ''.join(education_rows)
    research_subtitle = f'<span>{e(t["research_en"])}</span>' if t['research_en'] else ''
    education_subtitle = f'<span>{e(t["education_en"])}</span>' if t['education_en'] else ''
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
        <p class="current-work">{t['current_work']}</p>
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
      <div class="section-heading"><h2 id="research-title">{t['research']}</h2>{research_subtitle}</div>
      <div class="publications">{''.join(cards)}</div>
    </section>
    <section id="education" class="education-section" aria-labelledby="education-title">
      <div class="section-heading"><h2 id="education-title">{t['education']}</h2>{education_subtitle}</div>
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
