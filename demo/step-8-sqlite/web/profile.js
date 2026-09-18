const API = "http://127.0.0.1:8000";

(async () => {
  const token = localStorage.getItem("token");
  if (!token) { location.href = "index.html"; return; }   // 沒票就出去

  const res = await fetch(API + "/api/me", {
    headers: { "Authorization": "Bearer " + token }       // 出示通行證
  });

  if (res.status === 401) { location.href = "index.html"; return; }

  const me = await res.json();
  username.textContent = me.username;
  name.textContent = me.name;
  dept.textContent = me.dept;
})();

logout.onclick = () => {
  localStorage.removeItem("token");
  location.href = "index.html";
};
