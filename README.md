<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Muhammad Zain Ul Islam — GitHub Profile</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #050d1a;
    --surface: #0a1628;
    --surface2: #0e1e35;
    --border: rgba(0, 180, 255, 0.15);
    --accent: #00b4ff;
    --accent2: #7b5cf0;
    --text: #e2eaf5;
    --muted: #7a8fa8;
    --green: #00e5a0;
    --mono: 'JetBrains Mono', monospace;
    --sans: 'Syne', sans-serif;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── STARS ── */
  .stars {
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background:
      radial-gradient(1px 1px at 10% 15%, rgba(255,255,255,.7) 0%, transparent 100%),
      radial-gradient(1px 1px at 25% 40%, rgba(255,255,255,.5) 0%, transparent 100%),
      radial-gradient(1px 1px at 45% 10%, rgba(255,255,255,.8) 0%, transparent 100%),
      radial-gradient(1px 1px at 60% 60%, rgba(255,255,255,.4) 0%, transparent 100%),
      radial-gradient(1px 1px at 75% 25%, rgba(255,255,255,.6) 0%, transparent 100%),
      radial-gradient(1px 1px at 88% 80%, rgba(255,255,255,.5) 0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 33% 75%, rgba(255,255,255,.6) 0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 55% 88%, rgba(255,255,255,.7) 0%, transparent 100%),
      radial-gradient(1px 1px at 90% 5%, rgba(255,255,255,.9) 0%, transparent 100%),
      radial-gradient(2px 2px at 5% 55%, rgba(0,180,255,.4) 0%, transparent 100%),
      radial-gradient(2px 2px at 70% 45%, rgba(123,92,240,.4) 0%, transparent 100%);
  }

  .wrap { position: relative; z-index: 1; max-width: 860px; margin: 0 auto; padding: 0 24px 80px; }

  /* ── HERO ── */
  .hero {
    text-align: center;
    padding: 80px 0 60px;
    position: relative;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: 0; left: 50%; transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(0,180,255,.12) 0%, transparent 70%);
    pointer-events: none;
  }

  .hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    font-family: var(--mono); font-size: 13px; color: var(--accent);
    border: 1px solid var(--border);
    background: rgba(0,180,255,.05);
    padding: 6px 16px; border-radius: 100px;
    margin-bottom: 28px;
    animation: fadeUp .6s ease both;
  }
  .hero-badge::before { content: '</>'; opacity: .6; }

  .hero h1 {
    font-size: clamp(2.4rem, 5vw, 3.6rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -.02em;
    background: linear-gradient(135deg, #e2eaf5 0%, #00b4ff 50%, #7b5cf0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeUp .6s .1s ease both;
  }

  .typing-wrap {
    margin: 24px auto 0;
    display: inline-flex; align-items: center; gap: 10px;
    background: rgba(0,180,255,.06);
    border: 1px solid var(--border);
    padding: 10px 24px; border-radius: 8px;
    font-family: var(--mono); font-size: 16px; color: var(--text);
    animation: fadeUp .6s .2s ease both;
    min-width: 320px; justify-content: center;
  }
  .typing-wrap::before { content: '>_'; color: var(--accent); font-weight: 700; }
  .typing-text { display: inline-block; border-right: 2px solid var(--accent); animation: blink 1s step-end infinite; }

  @keyframes blink { 0%,100%{border-color:var(--accent)} 50%{border-color:transparent} }

  .hero-meta {
    margin-top: 28px;
    display: flex; align-items: center; justify-content: center;
    flex-wrap: wrap; gap: 8px 24px;
    font-size: 14px; color: var(--muted);
    animation: fadeUp .6s .3s ease both;
  }
  .hero-meta span { display: flex; align-items: center; gap: 6px; }
  .hero-meta svg { width: 15px; height: 15px; flex-shrink: 0; }

  .hero-links {
    margin-top: 28px;
    display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;
    animation: fadeUp .6s .4s ease both;
  }
  .hero-links a {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 10px 24px; border-radius: 8px;
    font-size: 14px; font-weight: 700; text-decoration: none;
    transition: transform .2s, box-shadow .2s;
  }
  .hero-links a:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,.4); }
  .btn-linkedin { background: #0a66c2; color: #fff; }
  .btn-github { background: var(--surface2); color: var(--text); border: 1px solid var(--border); }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 48px 0;
  }

  /* ── SECTION ── */
  .section-title {
    display: flex; align-items: center; gap: 12px;
    font-size: 18px; font-weight: 700;
    margin-bottom: 24px; color: var(--text);
  }
  .section-title .icon {
    font-size: 20px;
  }
  .section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
    margin-left: 8px;
  }

  /* ── ABOUT ── */
  .about-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px 32px;
  }
  .about-lead {
    font-size: 16px; line-height: 1.6;
    margin-bottom: 20px;
  }
  .about-lead strong { color: var(--accent); font-weight: 700; }
  .about-list { list-style: none; display: flex; flex-direction: column; gap: 10px; }
  .about-list li {
    display: flex; align-items: center; gap: 12px;
    font-size: 14px; color: var(--muted);
    font-family: var(--mono);
  }
  .about-list li::before {
    content: '▸';
    color: var(--accent);
    font-size: 12px;
    flex-shrink: 0;
  }
  .about-list li span { color: var(--text); }
  .about-footer {
    margin-top: 20px; padding-top: 20px;
    border-top: 1px solid var(--border);
    font-size: 14px; color: var(--muted);
    font-style: italic;
  }

  /* ── TECH STACK ── */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
  }
  .tech-group {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 20px;
  }
  .tech-group-label {
    font-family: var(--mono); font-size: 11px;
    color: var(--accent); letter-spacing: .1em;
    text-transform: uppercase; margin-bottom: 14px;
    font-weight: 700;
  }
  .tech-pills { display: flex; flex-wrap: wrap; gap: 8px; }
  .pill {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(0,180,255,.08);
    border: 1px solid rgba(0,180,255,.2);
    color: var(--text); font-size: 12px;
    padding: 4px 12px; border-radius: 6px;
    font-family: var(--mono);
    transition: background .2s, border-color .2s;
  }
  .pill:hover { background: rgba(0,180,255,.15); border-color: rgba(0,180,255,.4); }
  .pill.purple {
    background: rgba(123,92,240,.08);
    border-color: rgba(123,92,240,.25);
  }
  .pill.purple:hover { background: rgba(123,92,240,.18); }
  .pill.green {
    background: rgba(0,229,160,.08);
    border-color: rgba(0,229,160,.25);
  }

  /* ── EXPERIENCE ── */
  .exp-list { display: flex; flex-direction: column; gap: 20px; }
  .exp-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 0 12px 12px 0;
    padding: 22px 28px;
    position: relative;
    transition: border-left-color .2s;
  }
  .exp-card.purple-border { border-left-color: var(--accent2); }
  .exp-card:hover { border-left-color: var(--green); }
  .exp-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }
  .exp-title { font-size: 16px; font-weight: 700; color: var(--text); }
  .exp-company { font-size: 14px; color: var(--accent); font-family: var(--mono); margin-top: 2px; }
  .exp-period {
    font-family: var(--mono); font-size: 11px; color: var(--muted);
    background: var(--surface2); padding: 4px 10px; border-radius: 6px;
    border: 1px solid var(--border); white-space: nowrap;
  }
  .exp-bullets { list-style: none; display: flex; flex-direction: column; gap: 8px; }
  .exp-bullets li {
    font-size: 13px; color: var(--muted);
    display: flex; align-items: flex-start; gap: 10px; line-height: 1.5;
  }
  .exp-bullets li::before { content: '→'; color: var(--accent); flex-shrink: 0; margin-top: 1px; font-size: 12px; }

  /* ── PROJECTS ── */
  .proj-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }
  .proj-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    text-decoration: none;
    color: inherit;
    display: flex; flex-direction: column; gap: 10px;
    transition: transform .2s, border-color .2s, box-shadow .2s;
    position: relative; overflow: hidden;
  }
  .proj-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    opacity: 0; transition: opacity .2s;
  }
  .proj-card:hover { transform: translateY(-3px); border-color: rgba(0,180,255,.35); box-shadow: 0 12px 32px rgba(0,0,0,.3); }
  .proj-card:hover::before { opacity: 1; }
  .proj-icon { font-size: 22px; }
  .proj-name { font-size: 15px; font-weight: 700; color: var(--text); }
  .proj-desc { font-size: 13px; color: var(--muted); line-height: 1.5; flex: 1; }
  .proj-link {
    font-family: var(--mono); font-size: 11px;
    color: var(--accent); letter-spacing: .03em;
    display: flex; align-items: center; gap: 4px;
  }
  .proj-link::after { content: '↗'; font-size: 12px; }

  /* ── STATS ── */
  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  .stats-grid-bottom {
    margin-top: 16px;
  }
  .stats-card {
    border-radius: 12px; overflow: hidden;
    border: 1px solid var(--border);
    background: var(--surface);
    min-height: 120px;
    display: flex; align-items: center; justify-content: center;
  }
  .stats-card img {
    width: 100%; display: block;
    border-radius: 12px;
  }
  .stats-card-full {
    grid-column: 1 / -1;
  }

  /* ── FOOTER ── */
  .footer {
    text-align: center;
    padding: 40px 0 0;
    color: var(--muted);
    font-size: 13px;
    font-family: var(--mono);
    border-top: 1px solid var(--border);
  }
  .footer .wave { font-size: 22px; display: block; margin-bottom: 8px; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 600px) {
    .stats-grid { grid-template-columns: 1fr; }
    .hero { padding: 48px 0 40px; }
  }
</style>
</head>
<body>
<div class="stars"></div>
<div class="wrap">

  <!-- HERO -->
  <section class="hero">
    <div class="hero-badge">Muhammad Zain Ul Islam</div>
    <h1>Software Engineer</h1>
    <div class="typing-wrap">
      <span class="typing-text" id="typer">Java Backend Developer</span>
    </div>

    <div class="hero-meta">
      <span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
        Islamabad, Pakistan
      </span>
      <span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
        zain.rebaso@gmail.com
      </span>
      <span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 11.5 19.79 19.79 0 0 1 1.08 2.84 2 2 0 0 1 3.05 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21 16h1v.92z"/></svg>
        +92 306 0009555
      </span>
    </div>

    <div class="hero-links">
      <a href="https://linkedin.com/in/YOUR_LINKEDIN" class="btn-linkedin" target="_blank">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
        LinkedIn
      </a>
      <a href="https://github.com/MuhammadZainUlIslam" class="btn-github" target="_blank">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
        GitHub
      </a>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ABOUT -->
  <section>
    <div class="section-title"><span class="icon">🧠</span> About Me</div>
    <div class="about-card">
      <p class="about-lead">
        💻 Backend Engineer focused on <strong>scalable distributed systems</strong>
      </p>
      <ul class="about-list">
        <li><span>⚡ High-performance REST APIs</span></li>
        <li><span>🔐 Secure authentication systems</span></li>
        <li><span>📡 Event-driven microservices</span></li>
        <li><span>🧱 Clean, production-ready architectures</span></li>
      </ul>
      <p class="about-footer">I enjoy turning complex backend problems into <em>simple, scalable systems.</em></p>
    </div>
  </section>

  <div class="divider"></div>

  <!-- TECH STACK -->
  <section>
    <div class="section-title"><span class="icon">🛠</span> Tech Stack</div>
    <div class="tech-grid">
      <div class="tech-group">
        <div class="tech-group-label">Backend</div>
        <div class="tech-pills">
          <span class="pill">Java</span>
          <span class="pill">Spring Boot</span>
        </div>
      </div>
      <div class="tech-group">
        <div class="tech-group-label">Architecture</div>
        <div class="tech-pills">
          <span class="pill purple">Microservices</span>
          <span class="pill purple">System Design</span>
        </div>
      </div>
      <div class="tech-group">
        <div class="tech-group-label">Database</div>
        <div class="tech-pills">
          <span class="pill green">MySQL</span>
        </div>
      </div>
      <div class="tech-group">
        <div class="tech-group-label">Tools</div>
        <div class="tech-pills">
          <span class="pill">Git</span>
          <span class="pill">Docker</span>
          <span class="pill">Kafka</span>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- EXPERIENCE -->
  <section>
    <div class="section-title"><span class="icon">💼</span> Experience</div>
    <div class="exp-list">

      <div class="exp-card">
        <div class="exp-header">
          <div>
            <div class="exp-title">🟢 Java Intern</div>
            <div class="exp-company">Evamp &amp; Saanga · Islamabad</div>
          </div>
          <div class="exp-period">Dec 2025 – Present</div>
        </div>
        <ul class="exp-bullets">
          <li>Spring Boot MVC architecture (Controller → Service → Repository)</li>
          <li>MySQL integration + native queries</li>
          <li>REST API development &amp; third-party integrations</li>
          <li>JWT authentication using Spring Security</li>
          <li>Microservices-based design practice</li>
        </ul>
      </div>

      <div class="exp-card purple-border">
        <div class="exp-header">
          <div>
            <div class="exp-title">🔵 Project Lead — Al-Qawi Steels (FYP)</div>
            <div class="exp-company">Foundation University Islamabad</div>
          </div>
          <div class="exp-period">Aug 2023 – Jul 2024</div>
        </div>
        <ul class="exp-bullets">
          <li>Built Intelligent Vehicle Parking System (Flask + OpenCV)</li>
          <li>Real-time CCTV-based vehicle detection system</li>
          <li>REST APIs for monitoring and operations</li>
          <li>System design, UML diagrams, documentation, Figma UI</li>
        </ul>
      </div>

    </div>
  </section>

  <div class="divider"></div>

  <!-- PROJECTS -->
  <section>
    <div class="section-title"><span class="icon">🚀</span> Featured Projects</div>
    <div class="proj-grid">

      <a href="https://github.com/MuhammadZainUlIslam/kafka-springboot-library-events" class="proj-card" target="_blank">
        <div class="proj-icon">📡</div>
        <div class="proj-name">Kafka Event System</div>
        <div class="proj-desc">Event-driven library system using Spring Boot + Kafka</div>
        <div class="proj-link">kafka-springboot-library-events</div>
      </a>

      <a href="https://github.com/MuhammadZainUlIslam/spring-security-jwt-oauth2-aop" class="proj-card" target="_blank">
        <div class="proj-icon">🔐</div>
        <div class="proj-name">Security System</div>
        <div class="proj-desc">Enterprise-level JWT + OAuth2 + AOP authentication & authorization</div>
        <div class="proj-link">spring-security-jwt-oauth2-aop</div>
      </a>

      <a href="https://github.com/MuhammadZainUlIslam/secure-campus-management-system" class="proj-card" target="_blank">
        <div class="proj-icon">🏫</div>
        <div class="proj-name">Campus Management System</div>
        <div class="proj-desc">Secure backend system for campus operations</div>
        <div class="proj-link">secure-campus-management-system</div>
      </a>

    </div>
  </section>

  <div class="divider"></div>

  <!-- GITHUB STATS -->
  <section>
    <div class="section-title"><span class="icon">📊</span> GitHub Analytics</div>
    <div class="stats-grid">
      <div class="stats-card">
        <img
          src="https://github-readme-stats.vercel.app/api?username=MuhammadZainUlIslam&show_icons=true&theme=transparent&bg_color=0a1628&border_color=163050&title_color=00b4ff&icon_color=7b5cf0&text_color=e2eaf5&ring_color=7b5cf0&hide_border=false&count_private=true"
          alt="GitHub Stats"
          onerror="this.parentElement.innerHTML='<div style=\'padding:24px;text-align:center;font-family:monospace;font-size:13px;color:#7a8fa8\'>📊 GitHub Stats<br><span style=\'color:#00b4ff;font-size:11px\'>github-readme-stats.vercel.app</span></div>'"
        />
      </div>
      <div class="stats-card">
        <img
          src="https://github-readme-stats.vercel.app/api/top-langs/?username=MuhammadZainUlIslam&layout=compact&theme=transparent&bg_color=0a1628&border_color=163050&title_color=00b4ff&text_color=e2eaf5&hide_border=false&langs_count=6"
          alt="Top Languages"
          onerror="this.parentElement.innerHTML='<div style=\'padding:24px;text-align:center;font-family:monospace;font-size:13px;color:#7a8fa8\'>💻 Top Languages<br><span style=\'color:#00b4ff;font-size:11px\'>github-readme-stats.vercel.app</span></div>'"
        />
      </div>
    </div>
    <div class="stats-grid stats-grid-bottom">
      <div class="stats-card stats-card-full">
        <img
          src="https://streak-stats.demolab.com?user=MuhammadZainUlIslam&theme=transparent&background=0a1628&border=163050&stroke=163050&ring=00b4ff&fire=00e5a0&currStreakNum=e2eaf5&sideNums=e2eaf5&currStreakLabel=00b4ff&sideLabels=7a8fa8&dates=7a8fa8&hide_border=false"
          alt="GitHub Streak"
          onerror="this.parentElement.innerHTML='<div style=\'padding:24px;text-align:center;font-family:monospace;font-size:13px;color:#7a8fa8\'>🔥 Contribution Streak<br><span style=\'color:#00b4ff;font-size:11px\'>streak-stats.demolab.com</span></div>'"
        />
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <span class="wave">👋</span>
    <span style="font-family: 'JetBrains Mono', monospace;">// Thanks for visiting · Let's build something great together</span>
  </footer>

</div>

<script>
  const roles = [
    'Java Backend Developer',
    'Spring Boot | Microservices',
    'System Design Enthusiast',
    'Backend Architect in Progress',
    'Software Engineer'
  ];
  let ri = 0, ci = 0, deleting = false;
  const el = document.getElementById('typer');

  function type() {
    const word = roles[ri];
    if (!deleting) {
      el.textContent = word.slice(0, ci + 1);
      ci++;
      if (ci === word.length) { deleting = true; setTimeout(type, 1800); return; }
    } else {
      el.textContent = word.slice(0, ci - 1);
      ci--;
      if (ci === 0) { deleting = false; ri = (ri + 1) % roles.length; }
    }
    setTimeout(type, deleting ? 50 : 80);
  }
  type();
</script>
</body>
</html>
