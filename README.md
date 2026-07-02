# 用 Agent 來學習 Agent (AI Agent EP01)

本專案是一個透過 AI Agent（如 Google Antigravity / Gemini 等）來自動化建構學習知識庫的實作專案。

透過這個儲存庫中的指令檔與自訂技能設定，您可以教導任何 AI Agent 自動抓取 [三師爸 YouTube 頻道](https://www.youtube.com/@sensebar) 中與 AI Agent、Claude AI、Codex、Antigravity、Opencode 相關的影片，下載字幕並清理語音轉文字的重疊贅字，轉換為乾淨的 Markdown 逐字稿檔案以利後續學習與查詢（如貼入 NotebookLM）。

---

## 📂 專案目錄結構

- `.agents/`：Agent 的客製化設定目錄。
  - `AGENTS.md`：本專案開發時套用給 Agent 的行為規則與工作藍圖。
  - `skills/build_knowledge/`：自訂技能目錄。
    - `SKILL.md`：說明如何觸發並運作此技能。
    - `scripts/build_knowledge.py`：全自動執行「獲取影片清單 -> 關鍵字篩選 -> 下載字幕 -> 字幕降噪整理 -> 輸出 Markdown」的一鍵式腳本。
- `subtitles/`：存放全自動產生的影片字幕 Markdown 檔案。
- `agents.md`：本專案的專案工作藍圖。
- `sensebar_urls.txt`：篩選後的影片 YouTube 網址列表（每行一個，可直接貼入 NotebookLM）。
- `sensebar_videos.md`：Markdown 格式的影片清單連結。

---

## 🚀 快速開始

### 1. 安裝環境需求
本專案的腳本需要 Python 3、`yt-dlp` 及 `FFmpeg`。
如果您使用的是 Windows 系統，可直接透過 PowerShell 執行以下指令進行安裝：
```powershell
winget install yt-dlp
winget install yt-dlp.FFmpeg
```
*註：如果安裝後顯示找不到指令，請重新啟動終端機或 IDE 以載入環境變數 PATH，或者使用 `$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")` 來重新載入環境變數。*

### 2. 執行建構腳本
執行以下指令，一鍵獲取最新影片並重建/更新字幕知識庫：
```bash
python .agents/skills/build_knowledge/scripts/build_knowledge.py
```
執行完畢後，即可在 `subtitles/` 資料夾中看到更新的逐字稿檔案，並更新 `sensebar_urls.txt` 中的網址。

---

## 🤖 給 AI Agent 的執行指南 (For AI Agents)

本專案已在 `.agents/skills/build_knowledge/SKILL.md` 定義了 `build_knowledge` 自訂技能（Skill）。

當您（AI Agent）載入此專案時：
1. 請先閱讀 [.agents/skills/build_knowledge/SKILL.md](file:///.agents/skills/build_knowledge/SKILL.md) 了解此技能的工作流程與規範。
2. 執行 [.agents/skills/build_knowledge/scripts/build_knowledge.py](file:///.agents/skills/build_knowledge/scripts/build_knowledge.py) 腳本來一鍵重建此專案的知識內容。
3. 腳本會智慧尋找您系統中的 `yt-dlp` 與 `ffmpeg`（包括 WinGet 本地 portable 安裝），且自動清理 auto-caption 產生的重疊贅字。
