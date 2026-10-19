"""YouTube 予約アップロードスクリプト

「投稿用テキスト」（タイトルと概要欄を投稿順にまとめたファイル）を読み込み、
同じフォルダにある「タイトル.mp4」を順番に予約投稿でアップロードします。

使い方（まずは確認だけ）:
    python upload_youtube.py --plan "投稿用テキスト_10本.txt" --start "2026-10-21 18:00" --dry-run

本番:
    python upload_youtube.py --plan "投稿用テキスト_10本.txt" --start "2026-10-21 18:00"
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
JST = timezone(timedelta(hours=9))
HERE = Path(__file__).resolve().parent
CLIENT_SECRET = HERE / "client_secret.json"   # Google Cloud からダウンロードしたファイル
TOKEN = HERE / "token.json"                   # 初回ログイン後に自動で作られる
STATE = HERE / "uploaded.json"                # アップロード済みの記録（二重投稿防止）

CATEGORY_EDUCATION = "27"
TAGS = ["Python", "プログラミング", "プログラミング初心者", "Shorts"]


# ---------------- 投稿用テキストの読み込み ----------------
def parse_plan(path):
    """■ N本目 / 【タイトル】 / 【概要欄】 の形式を読み込んで [(title, description)] を返す"""
    text = Path(path).read_text(encoding="utf-8")
    blocks = re.split(r"\n=+\n", text)
    items = []
    for b in blocks:
        m = re.search(r"【タイトル】\n(.+?)\n\n【概要欄】\n(.*)", b.strip(), re.S)
        if m:
            items.append((m.group(1).strip(), m.group(2).strip() + "\n"))
    if not items:
        sys.exit(f"投稿用テキストから動画が1本も見つかりませんでした: {path}")
    return items


def validate(title, desc, video):
    problems = []
    if len(title) > 100: problems.append(f"タイトルが100文字を超えています（{len(title)}文字）")
    if len(desc) > 5000: problems.append(f"概要欄が5000文字を超えています（{len(desc)}文字）")
    for name, s in (("タイトル", title), ("概要欄", desc)):
        if "<" in s or ">" in s: problems.append(f"{name}に山かっこ（< >）が含まれています")
    if not video.exists(): problems.append(f"動画ファイルが見つかりません: {video.name}")
    return problems


def schedule(start, n, interval_hours):
    """日本時間の開始日時から、interval_hours ごとの公開日時を n 個作る"""
    t0 = datetime.strptime(start, "%Y-%m-%d %H:%M").replace(tzinfo=JST)
    return [t0 + timedelta(hours=interval_hours * i) for i in range(n)]


# ---------------- YouTube API ----------------
def get_service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CLIENT_SECRET.exists():
                sys.exit(f"{CLIENT_SECRET.name} がありません。README の「準備」を確認してください。")
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)   # ブラウザが開くので YouTube アカウントで許可する
        TOKEN.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds)


def build_body(title, desc, publish_at):
    return {
        "snippet": {
            "title": title,
            "description": desc,
            "tags": TAGS,
            "categoryId": CATEGORY_EDUCATION,
            "defaultLanguage": "ja",
            "defaultAudioLanguage": "ja",
        },
        "status": {
            "privacyStatus": "private",   # 予約投稿は「非公開＋公開日時」で指定する
            "publishAt": publish_at.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "selfDeclaredMadeForKids": False,
        },
    }


def upload(service, video, body, retries=5):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    media = MediaFileUpload(str(video), mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    req = service.videos().insert(part="snippet,status", body=body, media_body=media)
    response, attempt = None, 0
    while response is None:
        try:
            status, response = req.next_chunk()
            if status: print(f"    {int(status.progress() * 100)}%")
        except HttpError as e:
            if e.resp.status in (500, 502, 503, 504) and attempt < retries:
                attempt += 1
                wait = 2 ** attempt
                print(f"    サーバーエラー {e.resp.status}。{wait}秒後に再試行します…")
                time.sleep(wait)
            else:
                raise
    return response


# ---------------- メイン ----------------
def main(argv=None):
    p = argparse.ArgumentParser(description="投稿用テキストに沿って YouTube に予約アップロードする")
    p.add_argument("--plan", required=True, help="投稿用テキストのファイル")
    p.add_argument("--videos", help="動画フォルダ（省略時は投稿用テキストと同じフォルダ）")
    p.add_argument("--start", required=True, help='1本目の公開日時（日本時間） 例: "2026-10-21 18:00"')
    p.add_argument("--interval-hours", type=float, default=24, help="公開の間隔（時間）。初期値は24＝1日1本")
    p.add_argument("--limit", type=int, help="今回アップロードする最大本数")
    p.add_argument("--dry-run", action="store_true", help="アップロードせず、予定だけ表示する")
    a = p.parse_args(argv)

    items = parse_plan(a.plan)
    vdir = Path(a.videos) if a.videos else Path(a.plan).resolve().parent
    times = schedule(a.start, len(items), a.interval_hours)
    done = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}

    now = datetime.now(JST)
    plan, errors = [], []
    for (title, desc), t in zip(items, times):
        video = vdir / f"{title}.mp4"
        if title in done:   # アップロード済みはチェック不要
            plan.append((title, desc, video, t)); continue
        probs = validate(title, desc, video)
        if t <= now + timedelta(minutes=15):
            probs.append(f"公開日時 {t:%m/%d %H:%M} が近すぎるか過去です（15分以上先にしてください）")
        if probs: errors.append((title, probs))
        plan.append((title, desc, video, t))

    print(f"投稿予定（{len(plan)}本）")
    for i, (title, _, _, t) in enumerate(plan, 1):
        mark = "済" if title in done else "  "
        print(f" {mark} {i:2d}. {t:%m/%d(%a) %H:%M}  {title}")
    if errors:
        print("\n問題が見つかりました:")
        for title, probs in errors:
            for pr in probs: print(f"  ・{title}\n      → {pr}")
        sys.exit(1)
    if a.dry_run:
        print("\n--dry-run のため、アップロードはしていません。")
        return

    service = get_service()
    count = 0
    for title, desc, video, t in plan:
        if title in done:
            continue
        if a.limit and count >= a.limit:
            break
        print(f"\nアップロード中: {title}")
        res = upload(service, video, build_body(title, desc, t))
        vid = res["id"]
        st = res.get("status", {})
        done[title] = {"id": vid, "publishAt": st.get("publishAt"), "uploadedAt": datetime.now(JST).isoformat()}
        STATE.write_text(json.dumps(done, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"    完了 → https://youtube.com/shorts/{vid}  （{t:%m/%d %H:%M} に公開予定）")
        if st.get("privacyStatus") != "private" or not st.get("publishAt"):
            print(f"    ⚠ 予約が設定されていない可能性があります: {st}")
        count += 1
    print(f"\n{count}本をアップロードしました。YouTube Studio の「コンテンツ」で予約状況を確認できます。")


if __name__ == "__main__":
    main()
