"""Step 7 — 登入 API 的自動測試

執行：pytest -v
測試不是為了證明程式對，是為了讓你「敢改」。
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# ── 正常情境 ──────────────────────────────────────────────────

def test_login_success():
    """正確的帳號密碼應該拿到 token"""
    r = client.post("/api/login", json={"username": "jase", "password": "1234"})
    assert r.status_code == 200
    assert "token" in r.json()


def test_login_token_is_random():
    """每次登入應該拿到不同的 token"""
    a = client.post("/api/login", json={"username": "jase", "password": "1234"}).json()
    b = client.post("/api/login", json={"username": "jase", "password": "1234"}).json()
    assert a["token"] != b["token"]


# ── 異常情境 ──────────────────────────────────────────────────

def test_login_wrong_password():
    """密碼錯誤應該被擋下來"""
    r = client.post("/api/login", json={"username": "jase", "password": "xxxx"})
    assert r.status_code == 401


def test_login_user_not_found():
    """帳號不存在也是 401"""
    r = client.post("/api/login", json={"username": "nobody", "password": "1234"})
    assert r.status_code == 401


def test_login_error_message_does_not_leak():
    """錯誤訊息不能洩漏「這個帳號存在」——兩種情況要一模一樣"""
    wrong_pw = client.post("/api/login", json={"username": "jase", "password": "xxxx"})
    no_user = client.post("/api/login", json={"username": "nobody", "password": "xxxx"})
    assert wrong_pw.json() == no_user.json()


def test_login_missing_field():
    """少送 password 欄位，Pydantic 應該回 422"""
    r = client.post("/api/login", json={"username": "jase"})
    assert r.status_code == 422


def test_login_empty_strings():
    """空字串不該登入成功"""
    r = client.post("/api/login", json={"username": "", "password": ""})
    assert r.status_code == 401


def test_login_very_long_string():
    """超長輸入不該讓伺服器爆掉（500）"""
    r = client.post("/api/login", json={"username": "a" * 1000, "password": "b" * 1000})
    assert r.status_code == 401


def test_login_sql_injection_string():
    """SQL 注入字串應該只是一個查不到的帳號，而不是繞過驗證"""
    r = client.post("/api/login", json={"username": "' OR '1'='1", "password": "x"})
    assert r.status_code == 401


# ── 受保護的 API ──────────────────────────────────────────────

def _token():
    return client.post("/api/login", json={"username": "jase", "password": "1234"}).json()["token"]


def test_me_with_valid_token():
    """帶有效 token 應該拿到自己的資料"""
    r = client.get("/api/me", headers={"Authorization": "Bearer " + _token()})
    assert r.status_code == 200
    assert r.json()["name"] == "王小明"


def test_me_without_token():
    """沒帶 token 應該被擋"""
    assert client.get("/api/me").status_code == 401


def test_me_with_bad_token():
    """亂帶 token 應該被擋

    注意這裡用的是 ASCII 字串：HTTP 標頭不能放中文，
    放中文會在送出前就拋出 UnicodeEncodeError，測到的就不是 401 了。
    """
    r = client.get("/api/me", headers={"Authorization": "Bearer not-a-real-token"})
    assert r.status_code == 401


def test_me_never_returns_password():
    """回應裡絕對不能出現密碼"""
    r = client.get("/api/me", headers={"Authorization": "Bearer " + _token()})
    assert "password" not in r.json()
