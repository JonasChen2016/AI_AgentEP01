# 專案工作藍圖：用 Agent 來學習 Agent (AI Agent EP01)

本專案旨在透過與 Google Antigravity / Gemini 等先進 AI Agent 進行協作，深度探索與學習 Agentic Workflow 的設計、客製化（Skills/Rules）、多 Agent 協作，以及工具整合（MCP）。

---

## 🎯 專案核心目標
1. **實戰學習**：不只學習理論，而是透過實際動手實作（Learning by Doing）來掌握 AI Agent 的核心技術。
2. **客製化實踐**：學習如何透過設定檔、自訂 Skills 與 Rules 來形塑專案專屬的 Agent。
3. **工具擴充**：掌握 MCP（Model Context Protocol）或自訂工具的串接，擴展 Agent 的能力邊界。
4. **知識沉澱**：將學習歷程、架構設計與實作步驟系統化地記錄下來。

---

## 🗺️ 專案工作階段 (Roadmap)

### 📌 階段一：基礎探索與環境建置
- [x] 初始化專案工作區
- [x] 建立基礎專案工作藍圖（`agents.md`）
- [ ] 探索 Antigravity IDE 的運作機制與基本指令
- [ ] 了解 Workspace 的目錄結構與自訂根目錄

### 📌 階段二：Agent 客製化 (Skills & Rules)
- [ ] 在 `.agents/` 目錄下建立客製化 Rules (`AGENTS.md`)
- [ ] 定義專案專屬的開發規範與角色風格
- [ ] 建立第一個自訂 Skill（包含 `SKILL.md` 與 helper scripts）
- [ ] 測試並驗證 Agent 是否能正確讀取並應用自訂的技能

### 📌 階段三：工具與 MCP 整合 (Tool Use & MCP)
- [ ] 學習 Model Context Protocol (MCP) 的運作原理
- [ ] 開發一個簡單的自訂 MCP Server
- [ ] 將 MCP Server 載入 Agent，使其能調用特定的本地或外部 API
- [ ] 實作一個需要多步驟決策（Routing）與工具調用的情境

### 📌 階段四：多 Agent 協作 (Multi-Agent & Teamwork)
- [ ] 學習 `define_subagent` 與 `invoke_subagent` 的設計模式
- [ ] 設計一個「主 Agent（Planner） + 子 Agent（Researcher/Executor）」的協作案例
- [ ] 模擬團隊協作（Teamwork）解決一個較複雜的綜合任務

### 📌 階段五：專案驗證與總結
- [ ] 撰寫完整的驗證計畫與成果展示（Walkthrough）
- [ ] 將學習心得與最佳實踐整理成學習筆記
- [ ] 分享與發表（如影片腳本、Blog 文章或 GitHub 倉庫）

---

## 🛠️ 工作區與設定參考
*   **專案根目錄**: `c:/Users/tingn/Desktop/AI Agent/三師爸/Antigravity/2026AI_agent/AI_AgentEP01_用 Agent 來學習 Agent`
*   **客製化設定目錄**: `.agents/` (未來可在此目錄下擴充 `AGENTS.md` 及 `skills/` 子目錄)

---

## 📝 隨手記與異動紀錄
*   **2026-07-02**: 初始化專案，建立 [agents.md](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/agents.md) 工作藍圖。
