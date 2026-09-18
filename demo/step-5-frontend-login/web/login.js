// 前端呼叫後端的那座橋
// 本機開發：前端在 5500、後端在 8000，要指定後端位址
// 部署後：前端和 API 由同一個服務供應，用相對路徑即可（空字串）
const API = location.port === "5500" ? "http://127.0.0.1:8000" : "";

// 用 document.getElementById 明確取得元素。
// 不要直接把 id 當變數用 —— 有些 id（例如 name）會撞到瀏覽器內建的
// window 屬性，寫進去不會報錯，畫面卻永遠不動，這種錯最難查。
const $ = (id) => document.getElementById(id);
const form = $("f"), msg = $("msg");

form.onsubmit = async (e) => {
  e.preventDefault();                       // 不要讓表單重整頁面
  msg.textContent = "登入中…";

  const res = await fetch(API + "/api/login", {
    method: "POST",                                          // HTTP 方法
    headers: { "Content-Type": "application/json" },         // 標頭：我送的是 JSON
    body: JSON.stringify({                                   // Body：真正的資料
      username: form.username.value,
      password: form.password.value
    })
  });

  if (!res.ok) {                            // 401 會走到這裡
    msg.textContent = "登入失敗，請檢查帳號密碼";
    return;
  }

  const data = await res.json();
  localStorage.setItem("token", data.token);   // 收好通行證
  msg.textContent = "登入成功！token 已存起來（下一步做個人資料頁）";
};
