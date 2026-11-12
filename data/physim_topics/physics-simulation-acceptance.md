# 物理模擬軟體驗收規格（physim）

**專案**：`/home/sam/物理模擬`  
**版本**：physim 1.0（README/測試基準）  
**驗收日期**：2026-11-12  
**測試基準**：`pytest` 329 passed（本機 Python 3.14）

---

## 1. 範圍與目標

本規格定義 **physim 物理模擬平台** 的驗收條件，涵蓋：
- 核心數值模型（48 個模型、19 個領域）
- 服務層與契約（`physim.service`、`physim.contracts`）
- 渲染管线（2D matplotlib、3D pyvista、Qiskit Bloch/電路）
- CLI、Streamlit、panel 三大入口
- 快取、深連結、匯出
- 效能硬門檻

**不在驗收範圍**：舊 Streamlit 互動編輯器（保留原位、未遷移）、非物理頁面。

---

## 2. 使用者場景

### US-1：研究者探索模型
- 使用者在 CLI/UI 搜尋模型，調整參數，產生單幀 PNG 與動畫。
- 驗收：`physim.cli list/search/info/render/animate` 全可用；render 輸出 PNG。

### US-2：比較兩組參數
- 同模型兩組參數並排摘要與圖，不做同軸疊圖。
- 驗收：UI compare 模式可切換；CLI 不需支援比較（UI only）。

### US-3：量子電路實驗
- 選擇 2/3-qubit 閘、設定種子，得到 statevector、Bloch 球、shots 直方圖。
- 驗收：21 個閘么正性、Bell/GHZ 機率、隱形傳態 fidelity=1.0。

### US-4：Streamlit 非主執行緒 3D
- 在 Streamlit worker 中渲染 3D 不 segfault。
- 驗收：worker 隔離測試通過。

---

## 3. 功能性需求（FR）

| ID | 需求 | 驗證方式 |
|---|---|---|
| FR-01 | 核心層不 import Streamlit/panel/pyvista；可用 CLI/pytest 直接執行 | import 檢查 + 測試 |
| FR-02 | 48 個模型全部註冊並可 `service.list_models()` 列出 | `test_service` |
| FR-03 | 參數 schema 驗證（ParamSpec/ParamSet）與 digest 穩定性 | `test_params` |
| FR-04 | Scene2D/Scene3D 型別正確、動畫幀數契約（2D 120、3D 60、電路依閘數） | `test_scene` |
| FR-05 | 2D 渲染 matplotlib Agg → PNG；SVG 必支援 | `test_render_2d` |
| FR-06 | 3D 渲染 pyvista 離屏 → PNG；失敗可退回 matplotlib 3D；strict 模式報錯 | `test_render_3d` |
| FR-07 | Qiskit 電路域：Statevector/Operator 精確結果；Aer shots 4096 | `test_circuit_*` |
| FR-08 | 電路動畫幀數契約 `12 + 36×n + 12` | `test_circuit_animation` |
| FR-09 | big-endian 顯示標籤與索引往返 | `test_endian` |
| FR-10 | 快取 key 包含模型+參數 digest+幀+dpi+後端；命中 <0.3s | `test_cache` |
| FR-11 | 深連結 URL→session→預設；param > preset > default | `test_deeplink` |
| FR-12 | 匯出：HTML 播放器、GIF、SVG、CSV/JSON、參數 JSON | `test_export` |
| FR-13 | 服務層唯讀；pydantic 契約序列化 | `test_service`, `test_contracts` |
| FR-14 | Qiskit renderer 雙路（pyvista Bloch + Qiskit 官方） | `test_renderer` |
| FR-15 | Streamlit/panel 外殼煙霧測試（領域切換、搜尋、preset、深連結） | `test_streamlit_app`, `test_panel_app` |

---

## 4. 非功能性需求（NFR）

| ID | 需求 | 門檻 |
|---|---|---|
| NFR-01 | CLI 冷啟動 `list` | < 5 s（實測 ~0.98 s） |
| NFR-02 | 2D 單幀冷渲染 | ~0.14–0.16 s |
| NFR-03 | 3D 單幀冷渲染（CLI 主執行緒） | < 2 s（實測 ~0.86 s） |
| NFR-04 | 3D 首次渲染（Streamlit worker） | < 2 s（實測 ~1.5 s） |
| NFR-05 | Qiskit Bloch 單幀冷/熱渲染 | ~2.2 s / 1.6 s |
| NFR-06 | 快取命中 | < 0.3 s（實測 ~0.0002–0.0004 s） |
| NFR-07 | statevector/unitary 數值誤差 | ≤ 1e-10 |
| NFR-08 | Aer 4096 shots 總變差（固定種子） | ≤ 0.05 |
| NFR-09 | 隱形傳態 Bob fidelity | 1.000000 |
| NFR-10 | 超密編碼 00/01/10/11 | 全部精確解碼 |
| NFR-11 | 21 個閘么正性 | 全部通過 |
| NFR-12 | 測試總數 | ≥ 329 passed |

---

## 5. 驗收準則（Acceptance Criteria）

### AC-1 核心與服務
- [ ] `pytest` 全數通過（≥329）
- [ ] `physim.service` 唯讀邊界無寫入副作用
- [ ] 契約序列化 round-trip 一致

### AC-2 渲染
- [ ] 2D PNG 可產生且非空
- [ ] 3D PNG 在無 Xvfb 環境可透過 EGL/OSMesa 產生
- [ ] `PHYSIM_STRICT_3D=1` 時 pyvista 失敗會報錯而非靜默退回
- [ ] SVG 2D 必支援

### AC-3 電路域
- [ ] 21 個閘么正性全部通過
- [ ] Bell/GHZ 機率與熵解析值一致
- [ ] 隱形傳態 fidelity = 1.000000
- [ ] 超密編碼四訊息精確解碼
- [ ] Aer 4096 shots 總變差 ≤ 0.05

### AC-4 UI/CLI
- [ ] CLI `list/search/info/presets/render/animate/panel/cache` 全可用
- [ ] Streamlit/panel 煙霧測試通過
- [ ] 深連結 param > preset > default 生效

### AC-5 效能
- [ ] 所有 NFR 門檻達成（見第 4 節）

---

## 6. 測試對應

| 測試模組 | 覆蓋需求 |
|---|---|
| `test_params` | FR-03 |
| `test_scene` | FR-04 |
| `test_render_2d` / `test_render_3d` | FR-05, FR-06 |
| `test_circuit_*` | FR-07, FR-08, FR-09 |
| `test_cache` | FR-10 |
| `test_deeplink` | FR-11 |
| `test_export` | FR-12 |
| `test_service` / `test_contracts` | FR-13, FR-14 |
| `test_streamlit_app` / `test_panel_app` | FR-15 |
| `test_performance` | NFR-01~06 |

---

## 7. 已知限制與未遷移項目

- 舊 Streamlit 互動編輯器（pymunk/pygame/vpython/pybullet）未遷移，保留原位。
- 非物理頁面（瀏覽、物理交流、概念整合）不遷移。
- ML/torch 留待 optional extra。
- 流體/PDE、天文大規模、相對論 Schwarzschild 軌道等為可新增主題。

---

## 8. 驗收結論

- **測試狀態**：329 passed（本機 Python 3.14）
- **效能**：所有硬門檻達成（詳 README 測試與驗收節）
- **結論**：physim 平台核心、渲染、電路域、UI/CLI、快取與匯出均通過驗收；未遷移項目已記錄於第 7 節，不影響核心驗收。

---

## 9. 概念圖

見 `docs/acceptance/concept-diagrams.md`。