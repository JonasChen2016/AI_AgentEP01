---
name: build_knowledge
description: Scrape, filter, download, clean, and convert YouTube video subtitles to markdown files to construct a local knowledge base.
---

# Build Knowledge Base Skill

This skill allows the Agent to fetch all videos from a specified YouTube channel (e.g., 三師爸 `@sensebar`), filter them by relevant keywords (like `Claude`, `Codex`, `Antigravity`, `Opencode`, `Agent`), download their subtitles, clean up any VTT timestamps and duplicate stuttering lines, and save the transcripts as individual markdown files inside the `subtitles/` folder.

## Prerequisites

1. **Python 3**: The script is written in Python.
2. **yt-dlp**: Required for downloading metadata and subtitles. If it's not installed in your global PATH, the script will automatically attempt to locate it in the default local WinGet packages folder (`%LOCALAPPDATA%\Microsoft\WinGet\Packages\`).
3. **FFmpeg**: Required by yt-dlp to handle subtitles formatting and conversions.

## Execution

To run the pipeline and construct or refresh the knowledge base, run the following command in the workspace root:

```bash
python .agents/skills/build_knowledge/scripts/build_knowledge.py
```

## How It Works Under the Hood

1. **Executable Discovery**: Resolves the path of `yt-dlp` and `ffmpeg` globally or inside the local WinGet portable directories.
2. **Metadata Fetching**: Pulls the titles and URLs of the first 300 videos from the channel playlist.
3. **Keywords Filtering**: Filters the list of videos to match topics of interest.
4. **Lists Generation**: Writes matching URLs to `sensebar_videos.md` and `sensebar_urls.txt` in the root folder.
5. **Subtitles Acquisition**: Loops through all matches and runs `yt-dlp` to get Traditional Chinese (`zh-Hant`), auto-translated, or English subtitles in WebVTT/SRT.
6. **Transcript Cleaning**: Parses VTT text, removes headers, HTML markup, time markers, duplicate consecutive lines, and cumulative auto-generated overlapping stutters.
7. **Document Assembly**: Outputs clean markdown transcripts inside `subtitles/` folder.
