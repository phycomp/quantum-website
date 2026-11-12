# physim 概念圖

以下以 Mermaid 表示 physim 平台的架構、資料流、領域分佈與渲染管線。

## 1. 系統架構（分層）

```mermaid
flowchart TB
    subgraph UI["上層：UI / CLI / 外部"]
        ST[Streamlit 薄外殼]
        PN[panel 獨立入口]
        CLI[CLI: list/search/info/render/animate/panel/cache]
        EXT[外部程式]
    end

    subgraph Service["服務層（唯讀）"]
        SVC[physim.service]
        CTR[physim.contracts (pydantic)]
    end

    subgraph Core["核心層（無 UI 依賴）"]
        PARAM[ParamSpec / ParamSet / Preset]
        SCENE[Scene2D / Scene3D]
        MODEL[BaseModel 協定]
        REG[Registry]
        CACHE[Render Cache]
    end

    subgraph Domains["領域層（19 domains / 48 models）"]
        Q[quantum, bands, circuit]
        M[mechanics, chaos, stability, rigid]
        O[optics, em, thermo, fluid, waves]
        A[astro, celestial, statistical, solid_state, relativity, quantum_optics, canvas]
    end

    subgraph Render["渲染層"]
        MPL[matplotlib 2D/3D fallback]
        PV[pyvista 3D 離屏]
        QK[Qiskit Bloch / 電路]
        SVG[SVG 2D]
        PLAYER[HTML/GIF 播放器]
    end

    UI --> SVC
    SVC --> CTR
    SVC --> Core
    Core --> Domains
    Domains --> SCENE
    SCENE --> Render
    Render --> PLAYER
```

## 2. 資料流（單幀）

```mermaid
flowchart LR
    A[ParamSpec/ParamSet] --> B[BaseModel.frame index]
    B --> C[numerics.py 純數值]
    C --> D[Scene2D / Scene3D]
    D --> E[render_frame renderer]
    E --> F[PNG / SVG]
    F --> G[HTML/GIF/panel/Streamlit]
```

## 3. 電路域渲染管線

```mermaid
flowchart LR
    CM[circuit model] --> PS[program / statevector]
    PS --> NS[native_scene qiskit]
    NS --> QB[Qiskit plot_bloch_multivector + 電路圖]
    NS --> PV2[pyvista Bloch 球]
    QB --> PNG[PNG]
    PV2 --> PNG
```

## 4. 領域分布

```mermaid
pie title 模型數量 by domain 群組
    "Quantum/Bands/Circuit" : 15
    "Mechanics/Chaos/Stability/Rigid" : 13
    "Optics/EM/Thermo/Fluid/Waves" : 8
    "Astro/Celestial/Statistical/SolidState/Relativity/QOptics/Canvas" : 12
```

## 5. UI 深連結優先序

```mermaid
flowchart LR
    URL[URL query] -->|最高| STATE[session state]
    STATE -->|次之| PRESET[preset]
    PRESET -->|再次之| DEF[預設值]
    DEF --> PARAM[param override]
```

## 6. 測試與驗收對應

```mermaid
flowchart TB
    T[pytest 329 passed] --> C[核心/服務]
    T --> R[渲染 2D/3D/SVG]
    T --> Q[電路域 21 閘]
    T --> U[UI/CLI 煙霧]
    T --> P[效能硬門檻]
    C --> AC[驗收通過]
    R --> AC
    Q --> AC
    U --> AC
    P --> AC
```