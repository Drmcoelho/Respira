/* Respira · canonical module loader
   Transitional layer: canonical /modules/*.html URLs load the legacy module files
   without breaking relative links inside the legacy documents.
*/
(function(){
  const script = document.currentScript;
  const src = script?.dataset?.src;
  const label = script?.dataset?.label || src || 'módulo';
  if(!src){
    document.body.innerHTML = '<main style="max-width:680px;margin:10vh auto;font-family:system-ui;padding:24px"><h1>Fonte não definida</h1><p>O wrapper canônico não recebeu data-src.</p></main>';
    return;
  }

  const legacyUrl = '../' + src;
  fetch(legacyUrl, {cache:'no-store'})
    .then(r => {
      if(!r.ok) throw new Error('HTTP ' + r.status + ' ao carregar ' + legacyUrl);
      return r.text();
    })
    .then(html => {
      // Mantém os links internos antigos apontando para a raiz do GitHub Pages.
      // Sem isso, index.html e arquivos auxiliares seriam resolvidos dentro de /modules/.
      if(/<head[^>]*>/i.test(html)){
        html = html.replace(/<head([^>]*)>/i, '<head$1>\n<base href="../">\n<meta name="x-respira-canonical-wrapper" content="' + location.pathname + '">');
      }
      document.open();
      document.write(html);
      document.close();
    })
    .catch(err => {
      document.body.innerHTML = '<main style="max-width:720px;margin:10vh auto;font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;color:#16383B;background:#F4EFE4;padding:28px;border:1px solid #D7CCB8;border-radius:16px">' +
        '<h1 style="margin-top:0">Falha ao carregar ' + label + '</h1>' +
        '<p>O arquivo canônico existe, mas não conseguiu carregar a versão legada.</p>' +
        '<p><a style="color:#A24B2C;font-weight:700" href="' + legacyUrl + '">Abrir versão legada diretamente</a></p>' +
        '<pre style="white-space:pre-wrap;background:#EBE3D3;padding:12px;border-radius:10px">' + String(err).replace(/[&<>]/g, s => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[s])) + '</pre>' +
      '</main>';
    });
})();
