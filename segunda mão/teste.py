import re
p='template.html'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:80])
    t=t.replace(old,new)
def rx(pat,new,flags=re.S):
    global t
    t,n=re.subn(pat,lambda m:new,t,flags=flags)
    assert n==1,(n,pat[:80])

# ---------------- CSS ----------------
rep("padding:36px 36px 140px;","padding:30px 32px 96px;")
rep(".wave{position:absolute;left:0;right:0;bottom:0;height:96px;",".wave{position:absolute;left:0;right:0;bottom:0;height:72px;")
rep(".wave-cap{position:absolute;left:36px;bottom:80px;",".wave-cap{position:absolute;left:32px;bottom:80px;") if ".wave-cap{position:absolute;left:36px;bottom:80px;" in t else rep(".wave-cap{position:absolute;left:36px;bottom:104px;",".wave-cap{position:absolute;left:32px;bottom:80px;")
rep(".hero{padding:26px 22px 110px}",".hero{padding:26px 22px 96px}")
rep(".in .tag{grid-row:span 2;",".in .tag{grid-row:span 3;")
rep(".f select{",".f[hidden],.fnote[hidden]{display:none}\n.i{cursor:help;color:var(--muted);font-size:12px;margin-left:3px}\n.hd{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}\n.hd .pill{margin-top:4px}\n.tabs{display:flex;gap:4px;margin:12px 0 12px;border-bottom:1px solid var(--line);overflow-x:auto}\n.tab{border:0;background:none;padding:8px 12px;cursor:pointer;color:var(--ink2);font-weight:600;border-bottom:2px solid transparent;margin-bottom:-1px;white-space:nowrap}\n.tab[aria-selected=true]{color:var(--ink);border-color:var(--accent)}\n.met{margin:0;padding-left:18px;color:var(--ink2);font-size:14px;max-width:96ch}\n.met li{margin:7px 0}.met b{color:var(--ink)}\n.in details summary{cursor:pointer;font-size:13px;color:var(--ink2);width:max-content;max-width:100%}\n.in details p{margin:6px 0 0}\n.empty details{margin-top:8px}.empty summary{cursor:pointer;color:var(--ink2)}.empty details p{margin:6px 0 0;font-size:13.5px}\n.f select{")

# ---------------- HTML ----------------
rep('<span>EcoSom SUS <span style="font-weight:400;color:var(--ink2)">· Projeto Integrado FMU Tech Inovação 2026.2</span></span>','<span>EcoSom SUS <span style="font-weight:400;color:var(--ink2)">· FMU Tech Inovação 2026.2</span></span>')

hero='''  <header class="hero" id="topo">
    <div class="hero-grid">
      <div>
        <h1 class="serif">EcoSom SUS</h1>
        <p class="sub">Índice de Desertos de Descanso Acústico e Proteção Neurovascular Urbana</p>
        <p class="objetivo serif">Transformar dados públicos de ruído em prevenção: proteger o coração e o sono e tornar a cidade mais acessível a quem tem hipersensibilidade auditiva.</p>
        <div class="chips"><span class="chip">ODS 3 · Meta 3.9</span><span class="chip">PWA · GeoSampa, DataSUS, CNES</span></div>
      </div>
      <div class="trilha">
        <h2>Uma camada de ruído, três entregas</h2>
        <div class="faixa"><i style="background:#3987e5"></i><b>Longo prazo</b><p>Sono fragmentado e cortisol alto elevam o risco de hipertensão, infarto e AVC.</p><span class="ent">Módulo 1: Score de Risco Acústico e Plano de Blindagem Noturna</span></div>
        <div class="faixa"><i style="background:#eb6834"></i><b>Curto prazo</b><p>O excesso de ruído pode causar sobrecarga sensorial em pessoas com TEA.</p><span class="ent">Módulo 2: rotas de menor ruído e refúgios de descompressão</span></div>
        <div class="faixa"><i style="background:#1baf7a"></i><b>Visão pública</b><p>Cruza o ruído com as internações do DataSUS.</p><span class="ent">Painel analítico para gestores e associações de bairro</span></div>
      </div>
    </div>
  </header>
'''