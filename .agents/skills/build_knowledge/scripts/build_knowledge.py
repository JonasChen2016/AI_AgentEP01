import os
import re
import subprocess
import shutil
import time
import sys

# Default settings
CHANNEL_URL = "https://www.youtube.com/@sensebar/videos"
KEYWORDS = [r"claude", r"codex", r"antigravity", r"opencode", r"open\s*code", r"agent", r"代理"]

def find_executable(name):
    # Check PATH first
    path_exe = shutil.which(name)
    if path_exe:
        return path_exe
        
    # Check WinGet portable package directory on Windows
    if sys.platform == 'win32':
        user_home = os.path.expanduser('~')
        winget_dir = os.path.join(user_home, 'AppData', 'Local', 'Microsoft', 'WinGet', 'Packages')
        if os.path.exists(winget_dir):
            for root, dirs, files in os.walk(winget_dir):
                for file in files:
                    if file.lower() == name.lower() or file.lower() == f"{name.lower()}.exe":
                        return os.path.join(root, file)
    return None

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

def clean_transcript(text):
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        if line.isdigit():
            continue
        # Remove HTML/VTT formatting tags
        line = re.sub(r'<[^>]+>', '', line)
        line = line.strip()
        if not line:
            continue
        
        # De-duplicate consecutive identical lines
        if cleaned_lines and cleaned_lines[-1] == line:
            continue
        cleaned_lines.append(line)
        
    # Deduplicate cumulative auto-generated caption overlaps
    final_lines = []
    for line in cleaned_lines:
        if not final_lines:
            final_lines.append(line)
            continue
        
        prev = final_lines[-1]
        if line.startswith(prev) or prev in line:
            final_lines[-1] = line
        elif prev.startswith(line) or line in prev:
            continue
        else:
            final_lines.append(line)
            
    return "\n\n".join(final_lines)

def run_pipeline():
    workspace_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    subtitles_dir = os.path.join(workspace_dir, "subtitles")
    os.makedirs(subtitles_dir, exist_ok=True)
    
    # 1. Resolve executables
    yt_dlp_path = find_executable("yt-dlp")
    ffmpeg_path = find_executable("ffmpeg")
    
    if not yt_dlp_path:
        print("ERROR: yt-dlp was not found in PATH or WinGet Packages.")
        sys.exit(1)
        
    print(f"Using yt-dlp: {yt_dlp_path}")
    if ffmpeg_path:
        print(f"Using ffmpeg: {ffmpeg_path}")
        
    # 2. Scrape videos titles and urls
    print(f"Fetching channel videos from: {CHANNEL_URL}...")
    fetch_cmd = [yt_dlp_path, "--flat-playlist", "--playlist-end", "300", "--print", "%(title)s | %(url)s", CHANNEL_URL]
    
    try:
        res = subprocess.run(fetch_cmd, capture_output=True, check=True)
        stdout_bytes = res.stdout
        try:
            output = stdout_bytes.decode('utf-8')
        except UnicodeDecodeError:
            output = stdout_bytes.decode('cp950', errors='ignore')
    except Exception as e:
        print(f"ERROR: Failed to fetch videos metadata: {e}")
        sys.exit(1)
        
    lines = output.strip().split('\n')
    print(f"Total videos fetched: {len(lines)}")
    
    # 3. Filter videos by keywords
    matched_videos = []
    for line in lines:
        if '|' not in line:
            continue
        parts = line.split('|')
        if len(parts) < 2:
            continue
        title = parts[0].strip()
        url = parts[-1].strip()
        
        matched = False
        for kw in KEYWORDS:
            if re.search(kw, title, re.IGNORECASE):
                matched = True
                break
        if matched:
            matched_videos.append((title, url))
            
    print(f"Matched videos: {len(matched_videos)}")
    
    # 4. Save list to sensebar_videos.md and sensebar_urls.txt
    md_list_path = os.path.join(workspace_dir, "sensebar_videos.md")
    urls_txt_path = os.path.join(workspace_dir, "sensebar_urls.txt")
    
    md_urls = [f"- {url}" for _, url in matched_videos]
    with open(md_list_path, "w", encoding="utf-8") as f:
        f.write("# 三師爸 YouTube 影片網址清單\n\n" + "\n".join(md_urls) + "\n")
        
    raw_urls = [url for _, url in matched_videos]
    with open(urls_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(raw_urls) + "\n")
        
    print(f"Saved matched URL list to {md_list_path} and {urls_txt_path}")
    
    # 5. Download subtitles and convert to markdown files
    temp_dir = os.path.join(workspace_dir, "temp_subs_download")
    
    success_count = 0
    fail_count = 0
    
    for idx, (title, url) in enumerate(matched_videos, 1):
        print(f"[{idx}/{len(matched_videos)}] Processing: {title} ({url})...")
        safe_title = sanitize_filename(title)
        
        # Clean previous temp folder
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)
        
        sub_cmd = [
            yt_dlp_path, 
            "--skip-download", 
            "--write-subs", 
            "--write-auto-subs", 
            "--sub-langs", "zh-Hant,zh-TW,zh-HK,zh,zh-Hans,en", 
            "--sub-format", "vtt", 
            "-o", os.path.join(temp_dir, "sub.%(ext)s")
        ]
        
        # Add ffmpeg path if found
        if ffmpeg_path:
            sub_cmd.extend(["--ffmpeg-location", os.path.dirname(ffmpeg_path)])
            
        sub_cmd.append(url)
        
        try:
            subprocess.run(sub_cmd, capture_output=True, check=False)
            vtt_files = [f for f in os.listdir(temp_dir) if f.endswith(".vtt") or f.endswith(".srt")]
            
            if vtt_files:
                sub_file = os.path.join(temp_dir, vtt_files[0])
                try:
                    with open(sub_file, "r", encoding="utf-8") as sf:
                        sub_content = sf.read()
                except UnicodeDecodeError:
                    with open(sub_file, "r", encoding="cp950", errors="ignore") as sf:
                        sub_content = sf.read()
                        
                clean_text = clean_transcript(sub_content)
                
                md_path = os.path.join(subtitles_dir, f"{safe_title}.md")
                md_content = f"# {title}\n\n"
                md_content += f"影片網址: {url}\n\n"
                md_content += "## 📝 字幕逐字稿\n\n"
                md_content += clean_text + "\n"
                
                with open(md_path, "w", encoding="utf-8") as mf:
                    mf.write(md_content)
                    
                print(f"SUCCESS: Saved to subtitles/{safe_title}.md")
                success_count += 1
            else:
                print(f"FAILED: No subtitles downloaded for {title}")
                fail_count += 1
        except Exception as e:
            print(f"ERROR: Failed processing {title}: {e}")
            fail_count += 1
            
        time.sleep(1)
        
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        
    print(f"\nAll steps finished!")
    print(f"Successfully processed: {success_count} / {len(matched_videos)}")
    print(f"Failed: {fail_count}")

if __name__ == "__main__":
    run_pipeline()
