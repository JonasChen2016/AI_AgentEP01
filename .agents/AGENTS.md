# 專案開發規範：用 Agent 來學習 Agent (AI Agent EP01)

本專案供 AI Agent 協作開發與學習。當您作為 AI Agent 進入此工作區時，請遵循以下規範與工作藍圖：

---

## 🎯 專案核心目標
1. 深入探索與實踐 AI Agent 的各種核心技術與 workflow 設計。
2. 學習自訂 Skills、自訂 Rules 並落實成設定檔與程式。
3. 串接與實踐 MCP（Model Context Protocol）或第三方自訂工具。
4. 整理、重構與分析 YouTube 影片字幕，沉澱成結構化知識庫。

---

## 🛠️ 開發與寫作規範 (Rules for Agents)

- **自動化優先**：對於重複性的工作（如資料抓取、檔案重命名、格式整理），請優先編寫 Python 腳本並以程式方式執行，避免繁雜的人工代寫。
- **編碼與路徑**：Windows 系統下執行終端指令時，請留意編碼輸出（優先捕獲 Raw Bytes 後再嘗試 `utf-8` 或 `cp950` 解碼）。在任何檔案寫入時使用 `utf-8` 格式。路徑必須使用絕對路徑或基於 workspace 的相對路徑，並保持 Windows/Unix 相容。
- **檔案連結**：在您的回覆中提及專案檔案、代碼符號（如類別、函數）或生成報告時，必須使用標準 GFM 格式建立 `file://` 的可點擊連結（例如 `[README.md](file:///path/to/README.md)`），以便於使用者和別的 Agent 在編輯器中點擊跳轉。
- **自訂技能調用**：若需要建構或更新本專案的影片與字幕資料庫，請優先調用 [build_knowledge](file:///c:/Users/tingn/Desktop/AI%20Agent/%E4%B8%89%E5%B8%AB%E7%88%B8/Antigravity/2026AI_agent/AI_AgentEP01_%E7%94%A8%20Agent%20%E4%BE%86%E5%AD%B8%E7%BF%92%20Agent/.agents/skills/build_knowledge/SKILL.md) 技能，或是直接執行 `python .agents/skills/build_knowledge/scripts/build_knowledge.py`。
