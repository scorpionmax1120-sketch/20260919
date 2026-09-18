// 前端呼叫後端的那座橋
const API = "http://127.0.0.1:8000";

f.onsubmit = async (e) => {
  e.preventDefault();                       // 不要讓表單重整頁面
  msg.textContent = "登入中…";

  const res = await fetch(API + "/api/login", {
    method: "POST",                                          // HTTP 方法
    headers: { "Content-Type": "application/json" },         // 標頭：我送的是 JSON
    body: JSON.stringify({                                   // Body：真正的資料
      username: f.username.value,
      password: f.password.value
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
