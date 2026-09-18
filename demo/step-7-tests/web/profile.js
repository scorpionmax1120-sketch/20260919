const API = location.port === "5500" ? "http://127.0.0.1:8000" : "";

// 一律用 document.getElementById，不要依賴「id 自動變成全域變數」。
// 原因：window.name 是瀏覽器內建的字串屬性，<dd id="name"> 蓋不過它，
// 寫 name.textContent = ... 不會報錯也不會生效，
// 畫面會一直停在「載入中…」而且 Console 什麼都不顯示。
const $ = (id) => document.getElementById(id);

(async () => {
  const token = localStorage.getItem("token");
  if (!token) { location.href = "index.html"; return; }   // 沒票就出去

  const res = await fetch(API + "/api/me", {
    headers: { "Authorization": "Bearer " + token }       // 出示通行證
  });

  if (res.status === 401) { location.href = "index.html"; return; }

  const me = await res.json();
  $("username").textContent = me.username;
  $("name").textContent = me.name;
  $("dept").textContent = me.dept;
})();

$("logout").onclick = () => {
  localStorage.removeItem("token");
  location.href = "index.html";
};
