// 入口のページだけを控えておく（GitHubが落ちていても、前に開いた入口で開けるように）
// いつもはネットの新しい入口を使い、取れないとき・エラーのときだけ控えを使う
const C='kg-entry-v1';
self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
  const req=e.request;if(req.method!=='GET')return;
  const u=new URL(req.url);if(u.origin!==location.origin)return;
  const page=req.mode==='navigate'||/\/(index\.html)?$/.test(u.pathname);
  if(!page)return;
  e.respondWith(fetch(req,{cache:'no-store'}).then(r=>{
    if(r.ok){const c=r.clone();caches.open(C).then(x=>x.put('entry',c));return r;}
    return caches.open(C).then(x=>x.match('entry')).then(m=>m||r);
  }).catch(()=>caches.open(C).then(x=>x.match('entry')).then(m=>m||Response.error())));
});
