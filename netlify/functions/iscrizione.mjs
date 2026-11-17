/* Iscrizione alla newsletter dal test del granchietto.
   Aggiunge il contatto alla lista Brevo. La chiave non sta nel codice:
   in Netlify → Site configuration → Environment variables vanno impostate
     BREVO_API_KEY  = la chiave API di Brevo
     BREVO_LIST_ID  = il numero della lista (es. 3)
   Se mancano, la funzione non fa nulla: resta comunque la copia in Netlify → Forms. */
export default async (req) => {
  if (req.method !== 'POST') return new Response('', { status: 405 });
  let d = {};
  try { d = await req.json(); } catch (e) { return new Response('', { status: 400 }); }
  const email = String(d.email || '').trim().toLowerCase();
  const nome = String(d.nome || '').trim().slice(0, 40);
  if (d['bot-field'] || d.consenso !== 'si' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 120) {
    return new Response('', { status: 400 });
  }
  const key = process.env.BREVO_API_KEY, lista = Number(process.env.BREVO_LIST_ID);
  if (!key || !lista) return new Response('', { status: 503 });

  const invia = (attributi) => fetch('https://api.brevo.com/v3/contacts', {
    method: 'POST',
    headers: { 'api-key': key, 'content-type': 'application/json', accept: 'application/json' },
    body: JSON.stringify({ email, listIds: [lista], updateEnabled: true, ...(attributi ? { attributes: attributi } : {}) })
  });
  let r = await invia(nome ? { FIRSTNAME: nome } : null);
  if (r.status === 400 && nome) r = await invia(null);   // se l'attributo del nome ha un altro nome nell'account
  return new Response('', { status: r.ok || r.status === 204 ? 200 : 502 });
};
