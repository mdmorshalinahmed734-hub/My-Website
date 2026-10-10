#python#


from pathlib import Path
import webbrowser

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Digital Growth Hub - Digital Marketing & Business Growth">
<title>Digital Growth Hub</title>
<style>
:root{--bg:#08111f;--panel:#101d30;--text:#f3f7ff;--muted:#a2b2ca;--green:#4ce0b1;--border:#25364e}
*{box-sizing:border-box;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:Arial,sans-serif;line-height:1.65}
a{color:inherit;text-decoration:none}
button{font:inherit;cursor:pointer}
.wrap{width:min(1160px,92%);margin:auto}
header{position:sticky;top:0;background:#08111fee;border-bottom:1px solid var(--border);z-index:10}
.nav{min-height:75px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.brand{font-size:20px;font-weight:bold;color:var(--green)}
nav{display:flex;gap:15px;flex-wrap:wrap}
nav a{font-size:13px;color:var(--muted)}
.btn{display:inline-block;background:var(--green);color:#071521;padding:12px 18px;border-radius:9px;font-weight:bold;border:0;cursor:pointer}
.hero{padding:75px 0;background:radial-gradient(ellipse at 80% 15%,#183a5066,transparent 45%)}
.hero-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:35px;align-items:center}
.eyebrow{color:var(--green);font-size:12px;font-weight:bold;letter-spacing:2px}
h1{font-size:clamp(38px,6vw,65px);line-height:1.1}
h1 span{color:var(--green)}
h2{font-size:32px}
p{color:var(--muted)}
.panel,.card{background:var(--panel);border:1px solid var(--border);border-radius:15px;padding:22px}
.metrics,.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:13px}
.metric{background:#091625;border:1px solid var(--border);padding:15px;border-radius:10px}
.metric strong{display:block;font-size:25px}
.section{padding:65px 0}
.alt{background:#0b1626;border-block:1px solid #17273b}
.cards{grid-template-columns:repeat(3,1fr)}
.card{transition:.2s}
.card:hover{transform:translateY(-4px);border-color:var(--green)}
.icon{font-size:28px}
.tag{font-size:11px;color:var(--green)}
.card a,footer a{color:var(--green)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:30px}
li{padding:6px 0;color:#d5dfed}
.contact{display:grid;gap:12px}
.contact a{display:block;background:var(--panel);border:1px solid var(--border);padding:14px;border-radius:9px;overflow-wrap:anywhere}
input,select,textarea{width:100%;padding:12px;margin:6px 0 15px;background:#091625;color:white;border:1px solid var(--border);border-radius:8px}
label{font-size:14px}
footer{background:#060d17;padding:30px 0;border-top:1px solid var(--border)}
footer .foot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
small{color:var(--muted)}
details{padding:15px 0;border-bottom:1px solid var(--border)}
summary{cursor:pointer;font-weight:bold}
@media(max-width:850px){.hero-grid,.two{grid-template-columns:1fr}.cards{grid-template-columns:repeat(2,1fr)}.nav{flex-wrap:wrap;padding:12px 0}nav{gap:10px}}
@media(max-width:550px){.cards{grid-template-columns:1fr}.hero{padding:40px 0}.section{padding:45px 0}h2{font-size:27px}}
</style>
</head>
<body>
<header><div class="wrap nav">
<a class="brand" href="#home">◆ Digital Growth Hub</a>
<nav>
<a href="#home">Home</a><a href="#services">Services</a>
<a href="#whatsapp">WhatsApp API</a><a href="#instagram">Instagram Ads</a>
<a href="#tiktok">TikTok Ads</a><a href="#growth">Growth Strategy</a>
<a href="#suite">Meta Suite</a><a href="#about">About</a>
<a href="#guide">Page Guide</a><a href="#contact">Contact</a>
</nav>
<a class="btn" href="#contact">Get Started</a>
</div></header>

<main>
<section class="hero" id="home"><div class="wrap hero-grid">
<div><div class="eyebrow">YOUR DIGITAL SUCCESS PARTNER</div>
<h1>Grow Your Business.<br><span>Go Digital.</span></h1>
<p>Smart advertising, WhatsApp automation and digital growth strategies designed to help your business reach more people and build a stronger online presence.</p>
<p><a class="btn" href="#services">Explore Services ↗</a></p>
<p><a href="#contact">Talk to our team →</a></p></div>
<div class="panel"><small>DEMO DASHBOARD</small><h2>Growth Overview</h2>
<div class="metrics">
<div class="metric"><small>Platforms</small><strong>04</strong></div>
<div class="metric"><small>Strategy</small><strong>360°</strong></div>
<div class="metric"><small>Campaigns</small><strong>01</strong></div>
<div class="metric"><small>Support</small><strong>1:1</strong></div>
</div><small>Illustrative preview, not live campaign data.</small>
</div></div></section>

<section class="section" id="services"><div class="wrap">
<div class="eyebrow">WHAT WE DO</div><h2>Digital Services for Business Growth</h2>
<p>Build your online presence, reach the right audience and create a practical marketing plan.</p>
<div class="cards">
<article class="card"><div class="icon">📣</div><span class="tag">META ADS</span><h3>Facebook Ads</h3><p>Campaign planning, audience targeting, creative guidance and optimization.</p><a href="#contact">Discuss campaign →</a></article>
<article class="card" id="instagram"><div class="icon">📸</div><span class="tag">INSTAGRAM</span><h3>Instagram Ads</h3><p>Promote products through Reels, Stories and Feed advertisements.</p><a href="#contact">Promote your brand →</a></article>
<article class="card" id="tiktok"><div class="icon">🎬</div><span class="tag">TIKTOK</span><h3>TikTok Ads</h3><p>Creative planning, advertising setup and audience strategies.</p><a href="#contact">Plan TikTok ads →</a></article>
<article class="card" id="whatsapp"><div class="icon">💬</div><span class="tag">AUTOMATION</span><h3>WhatsApp Business API</h3><p>API setup guidance, approved templates and customer messaging integration.</p><a href="#contact">Discuss API setup →</a></article>
<article class="card" id="suite"><div class="icon">🗂️</div><span class="tag">MANAGEMENT</span><h3>Meta Business Suite</h3><p>Business asset organization, publishing workflows and inbox management.</p><a href="#contact">Manage your business →</a></article>
<article class="card" id="growth"><div class="icon">📈</div><span class="tag">STRATEGY</span><h3>Business Growth Strategy</h3><p>Audience research, content planning, lead generation and measurement.</p><a href="#contact">Build a growth plan →</a></article>
</div></div></section>

<section class="section alt" id="about"><div class="wrap two">
<div><div class="eyebrow">ABOUT US</div><h2>Helping Businesses Grow Digitally</h2>
<p>Digital Growth Hub helps businesses explore digital marketing tools, strengthen their online presence and plan promotional campaigns.</p>
<p>Our service categories include advertising, business messaging and growth strategy.</p><a class="btn" href="#contact">Work With Us</a></div>
<div class="card"><h3>Our Approach</h3><ul>
<li>Understand your business and target audience.</li>
<li>Choose suitable platforms and objectives.</li>
<li>Plan creative content and customer journeys.</li>
<li>Review available metrics and improve campaigns.</li>
<li>Communicate clearly about scope and budget.</li>
</ul></div></div></section>

<section class="section" id="guide"><div class="wrap two">
<div><div class="eyebrow">BEGINNER GUIDE</div><h2>Facebook Business Page Setup</h2>
<p>Establish a professional business presence on Facebook with these basic steps.</p>
<a class="btn" href="https://www.facebook.com/pages/create/" target="_blank" rel="noopener">Create Facebook Page ↗</a></div>
<div class="card"><h3>Setup Checklist</h3><ol>
<li>Create a Page with your business name and category.</li>
<li>Add a logo, cover image and business description.</li>
<li>Review access permissions and security settings.</li>
<li>Publish useful content regularly.</li>
<li>Define your ad budget and campaign objectives.</li>
</ol></div></div></section>

<section class="section alt"><div class="wrap">
<div class="eyebrow">FAQ</div><h2>Frequently Asked Questions</h2>
<details><summary>What services are available?</summary><p>Facebook and Instagram ads, TikTok ads, WhatsApp API guidance, Meta Business Suite and growth planning.</p></details>
<details><summary>Can advertising results be guaranteed?</summary><p>No. Results depend on the offer, budget, audience, creative quality and market conditions.</p></details>
<details><summary>Does this demo have a live backend?</summary><p>No. A real backend, database and messaging integration must be configured separately.</p></details>
</div></section>

<section class="section" id="contact"><div class="wrap two">
<div><div class="eyebrow">GET IN TOUCH</div><h2>Let's Grow Your Business Together</h2>
<p>Contact us to discuss your digital marketing needs.</p>
<div class="contact">
<a href="tel:+88018601808843"><small>Phone / WhatsApp</small><br>018601808843 ↗</a>
<a href="mailto:liyonahmed806@gmail.com"><small>Email</small><br>liyonahmed806@gmail.com ↗</a>
<a href="https://www.facebook.com/profile.php?id=61594996359759&sk=directory_links" target="_blank" rel="noopener"><small>Facebook Page</small><br>Visit Digital Growth Hub ↗</a>
</div></div>
<div class="panel"><h3>Quick Inquiry</h3><p>This form prepares an email draft.</p>
<form id="contactForm">
<label for="name">Your name</label><input id="name" required placeholder="Enter your name">
<label for="service">Service</label><select id="service">
<option>Facebook Ads</option><option>Instagram Ads</option><option>TikTok Ads</option><option>WhatsApp Business API</option><option>Meta Business Suite</option><option>Business Growth Strategy</option>
</select>
<label for="message">Message</label><textarea id="message" rows="4" required placeholder="Tell us about your business"></textarea>
<button class="btn" type="submit">Prepare Email ↗</button>
</form><small>This demo does not save submissions.</small>
</div></div></section>
</main>

<footer><div class="wrap foot">
<div><b>◆ Digital Growth Hub</b><p>Smarter digital marketing. Sustainable growth.</p></div>
<div><b>Explore</b><p><a href="#services">Services</a> · <a href="#about">About</a> · <a href="#guide">Page Guide</a></p></div>
<div><b>Contact</b><p><a href="tel:+88018601808843">018601808843</a></p><p><a href="mailto:liyonahmed806@gmail.com">liyonahmed806@gmail.com</a></p><p><a href="https://www.facebook.com/profile.php?id=61594996359759&sk=directory_links" target="_blank" rel="noopener">Facebook Page ↗</a></p></div>
</div><div class="wrap"><small>© <span id="year"></span> Digital Growth Hub. Demo website.</small></div></footer>

<script>
document.getElementById('year').textContent=new Date().getFullYear();
document.getElementById('contactForm').addEventListener('submit',function(e){
e.preventDefault();
const name=document.getElementById('name').value.trim();
const service=document.getElementById('service').value;
const message=document.getElementById('message').value.trim();
const subject=encodeURIComponent('Digital Growth Hub inquiry: '+service);
const body=encodeURIComponent('Name: '+name+'\nService: '+service+'\n\nMessage:\n'+message);
window.location.href='mailto:liyonahmed806@gmail.com?subject='+subject+'&body='+body;
});
</script>
</body>
</html>
'''

Path("index.html").write_text(html, encoding="utf-8")
webbrowser.open(Path("index.html").resolve().as_uri())