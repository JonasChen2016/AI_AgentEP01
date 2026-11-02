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
- [x] 建立基礎專案工作藍圖（[agents.md](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/agents.md)）
- [x] 探索 Antigravity IDE 的運作機制與基本指令
- [x] 了解 Workspace 的目錄結構與自訂根目錄

### 📌 階段二：Agent 客製化與工具整合 (Skills, Rules & MCP)
- [x] 在 `.agents/` 目錄下建立客製化 Rules（[.agents/AGENTS.md](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/.agents/AGENTS.md)）
- [x] 串接 Obsidian MCP Server (`mcpvault`)，建立第二大腦知識庫 (`G:\我的雲端硬碟\secondbrain`)
- [x] 建立自訂知識庫抓取 Skill (`build_knowledge`)
- [x] 實作台電即時發電數據開放資料抓取與動態 HTML 簡報生成

### 📌 階段三：NoType 專案二次開發與打包 (Google Gemini 語音輸入)
- [x] 複製並整合 NoType 開源專案（`mathruffian-dot/notype`）
- [x] 實現 Google Gemini 多模態語音辨識 (`transcribeWithGemini`) 與 LLM 文字潤飾 (`polishWithGemini`)
- [x] 新增 UI 設定選單，支援 Gemini 最新模型選擇（`gemini-flash-latest`, `gemini-3.6-flash` 等）
- [x] 重構全域快捷鍵解析引擎（[src/shortcut.js](file:///C:/Users/tingn/.gemini/antigravity/brain/6b35bf49-a9d0-4120-b0f1-5c4d8dac4c9f/scratch/notype/src/shortcut.js)），全面支援 `Shift+Z` 等任意自訂組合鍵
- [x] 研發「一步到位單一請求極速引擎」（`transcribeAndPolishWithGemini`），速度提升 200%（約 0.8~1 秒完成）
- [x] 優化鍵盤與剪貼簿自動輸入，實現辨識後自動打入當前游標停放處
- [x] 使用 `electron-builder` 成功編譯打包 Windows 安裝檔（[NoType-Setup-v5.exe](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/NoType-Setup-v5.exe)）與綠色免安裝版（[NoType-Portable-v5.exe](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/NoType-Portable-v5.exe)）

---

## 🛠️ 工作區與設定參考
*   **專案根目錄**: [c:/Users/tingn/Desktop/AI Agent/三師爸/Antigravity/2026AI_agent/AI_AgentEP01_用 Agent 來學習 Agent](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent)
*   **客製化規範與技能**: [.agents/AGENTS.md](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/.agents/AGENTS.md)
*   **NoType 開發原始碼**: [C:\Users\tingn\.gemini\antigravity\brain\6b35bf49-a9d0-4120-b0f1-5c4d8dac4c9f\scratch\notype](file:///C:/Users/tingn/.gemini/antigravity/brain/6b35bf49-a9d0-4120-b0f1-5c4d8dac4c9f/scratch/notype)

---

## 📝 隨手記與異動紀錄
*   **2026-07-31**:
    *   完成 NoType Google Gemini 語音輸入二次開發、快捷鍵重構 (`Shift+Z`)、一步到位極速引擎優化與 Windows `.exe` 打包（[NoType-Portable-v5.exe](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/NoType-Portable-v5.exe)）。
    *   完成 Obsidian MCP (`mcpvault`) 整合與第二大腦目錄結構建置。
    *   完成台電發電資料 Excel 與 HTML 簡報生成。
*   **2026-07-02**: 初始化專案，建立 [agents.md](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/agents.md) 工作藍圖。
