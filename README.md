# kendai-gokaku

家族用の学習アプリ。中身はすべて暗号化してある（合言葉がないと読めない）。

- index.html：入口（合言葉と読み込みの画面）
- app.bin・app_raw.bin：アプリ本体（鍵つき。app.bin は縮めた版）
- materials.bin：アプリを組み立てる材料（鍵つき）。`python3 kg_crypt.py dec <合言葉ファイル> materials.bin materials.tgz` で戻す
- 合言葉はこのリポジトリには置かない
