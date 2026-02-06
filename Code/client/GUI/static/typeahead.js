/* Lightweight tokenized autocomplete / typeahead
   - Transforms comma-separated inputs into token UIs
   - Sources suggestions from window.appMetadata arrays
   - Keeps original input.value as comma-separated values for form submission
*/
(function(){
  // Inject minimal styles
  const css = `
  .token-input-container{border:1px solid #ddd;padding:6px;display:flex;flex-wrap:wrap;gap:6px;border-radius:4px}
  .token-input-container .token{background:#eef;padding:4px 8px;border-radius:12px;display:inline-flex;align-items:center;gap:6px}
  .token-input-container .token .remove{cursor:pointer;font-weight:bold;margin-left:6px}
  .token-input-container input.token-typed{border:none;outline:none;min-width:120px;flex:1}
  .typeahead-suggestions{position:absolute;background:#fff;border:1px solid #ccc;z-index:1500;max-height:180px;overflow:auto;border-radius:4px;box-shadow:0 4px 12px rgba(0,0,0,0.08)}
  .typeahead-suggestions .item{padding:6px 10px;cursor:pointer}
  .typeahead-suggestions .item:hover{background:#f4f4f4}
  `;
  const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);

  function createTokenUI(original){
    const id = original.id || ('tok-' + Math.random().toString(36).slice(2,8));
    const wrapper = document.createElement('div');
    wrapper.className = 'token-input-container';
    wrapper.style.position = 'relative';

    const tokenList = document.createElement('div'); tokenList.className = 'token-list';
    const input = document.createElement('input'); input.type = 'text'; input.className = 'token-typed';
    input.placeholder = original.placeholder || '';
    wrapper.appendChild(tokenList);
    wrapper.appendChild(input);

    // suggestion box
    const sug = document.createElement('div'); sug.className = 'typeahead-suggestions hidden'; sug.style.display='none';
    wrapper.appendChild(sug);

    // insert wrapper after original and hide original
    original.style.display = 'none';
    original.parentNode.insertBefore(wrapper, original.nextSibling);

    let tokens = [];

    function syncOriginal(){ original.value = tokens.join(', '); }

    function renderTokens(){ tokenList.innerHTML=''; tokens.forEach((t, idx)=>{
      const tk = document.createElement('span'); tk.className='token'; tk.textContent = t;
      const rem = document.createElement('span'); rem.className='remove'; rem.textContent='×'; rem.title='Remove';
      rem.addEventListener('click', ()=>{ tokens.splice(idx,1); renderTokens(); syncOriginal(); });
      tk.appendChild(rem); tokenList.appendChild(tk);
    });
    }

    // initialize from original value
    if(original.value && original.value.trim()){ tokens = original.value.split(',').map(s=>s.trim()).filter(Boolean); renderTokens(); syncOriginal(); }

    // suggestion helpers
    function openSuggestions(items){
      sug.innerHTML=''; if(!items || items.length===0){ sug.style.display='none'; return; }
      items.forEach(it=>{ const d = document.createElement('div'); d.className='item'; d.textContent = it; d.addEventListener('click', ()=>{ addToken(it); hideSuggestions(); input.focus(); }); sug.appendChild(d); });
      sug.style.display='block';
    }
    function hideSuggestions(){ sug.style.display='none'; }

    function addToken(value){ value = String(value).trim(); if(!value) return; if(tokens.includes(value)) return; tokens.push(value); renderTokens(); syncOriginal(); }

    // keyboard handling: comma/enter add token, backspace remove last when empty
    input.addEventListener('keydown', (ev)=>{
      if(ev.key === 'Enter' || ev.key === ','){ ev.preventDefault(); const v = input.value.trim().replace(/,$/,''); if(v) addToken(v); input.value=''; hideSuggestions(); }
      else if(ev.key === 'Backspace' && input.value === ''){ if(tokens.length){ tokens.pop(); renderTokens(); syncOriginal(); } }
      else if(ev.key === 'Escape'){ hideSuggestions(); }
    });

    input.addEventListener('input', (ev)=>{
      const q = input.value.trim().toLowerCase(); if(!q){ hideSuggestions(); return; }
      const source = wrapper._source || [];
      const filtered = source.filter(s => s.toLowerCase().includes(q) && !tokens.includes(s)).slice(0,50);
      if(filtered.length) openSuggestions(filtered); else hideSuggestions();
    });

    // clicking outside hides suggestions
    document.addEventListener('click', (ev)=>{ if(!wrapper.contains(ev.target)) hideSuggestions(); });

    // expose helper
    wrapper.addToken = addToken;
    wrapper.getTokens = () => tokens.slice();
    wrapper.setSource = (arr) => { wrapper._source = Array.isArray(arr)? arr.slice() : []; };

    return wrapper;
  }

  // Map input ids to metadata keys
  const MAPPINGS = {
    'linkTags': 'genres',
    'docGenres': 'genres',
    'docAuthors': 'authors',
    'audioGenres': 'genres',
    'audioAuthors': 'authors',
    'audioPerformers': 'performers',
    'audioInstruments': 'instruments',
    'videoGenres': 'genres',
    'videoAuthors': 'authors',
    'videoPerformers': 'performers',
    'videoInstruments': 'instruments'
  };

  function initAll(){
    Object.keys(MAPPINGS).forEach(id => {
      const el = document.getElementById(id);
      if(!el) return;
      // don't re-init
      if(el.__tokenized) return; el.__tokenized = true;
      const w = createTokenUI(el);
      // attach source when metadata available
      const key = MAPPINGS[id];
      function attachSource(){
        if(key === 'all' || id === 'search'){
          // combine all metadata arrays for search suggestions
          const meta = [];
          const wm = window.appMetadata || {};
          (wm.genres||[]).forEach(x=>meta.push(String(x)));
          (wm.authors||[]).forEach(x=>meta.push(String(x)));
          (wm.performers||[]).forEach(x=>meta.push(String(x)));
          (wm.instruments||[]).forEach(x=>meta.push(String(x)));
          (wm.media_titles||[]).forEach(x=>meta.push(String(x)));
          // unique
          const uniq = Array.from(new Set(meta));
          w.setSource(uniq);
        } else {
          const meta = window.appMetadata && window.appMetadata[key] ? window.appMetadata[key] : [];
          w.setSource(meta.map(x=>String(x)));
        }
      }
      attachSource();
      // if metadata updates later, keep binding: observe global changes by polling
      let tries = 0;
      const poll = setInterval(()=>{
        if(window.appMetadata && window.appMetadata[key] && window.appMetadata[key].length >= 0){ attachSource(); clearInterval(poll); }
        if(++tries > 50) clearInterval(poll);
      }, 120);
    });
  }

  // If metadata present now, init; otherwise wait until window.appMetadata is available
  if(window.appMetadata && typeof window.appMetadata === 'object'){
    document.addEventListener('DOMContentLoaded', initAll);
    if(document.readyState === 'interactive' || document.readyState === 'complete') initAll();
  } else {
    // wait for metadata injection or other code to set it
    const maxWait = 4000; let waited = 0;
    const waiter = setInterval(()=>{
      if(window.appMetadata && typeof window.appMetadata === 'object'){
        clearInterval(waiter); document.addEventListener('DOMContentLoaded', initAll); if(document.readyState === 'interactive' || document.readyState === 'complete') initAll();
      }
      waited += 200; if(waited > maxWait) { clearInterval(waiter); document.addEventListener('DOMContentLoaded', initAll); if(document.readyState === 'interactive' || document.readyState === 'complete') initAll(); }
    }, 200);
  }

})();
