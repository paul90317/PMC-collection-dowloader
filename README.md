# PMC Collection Dowloader
## 我的筆記
* [以 Event Loop 實現非同步爬蟲](https://hackmd.io/@paul90317/event_loop)  
說明 `async`, `await` 與 asyncio 的 event loop 的差別，以及為什麼在 **python** 中只用 `async`, `await` 無法達到非同步的原因。
* [Discord 筆記](https://hackmd.io/@paul90317/dscord_bot)  
如何使用 `commands` 和模板。
## 環境變數
```env
TOKEN=<token>
```
* [建立新的 token](https://discord.com/developers/applications)
## 技術點
### 非同步爬蟲
[./crawl.py](./crawl.py)
非同步爬蟲函式。
### Event Loop
[./get_code.py](./get_code.py)
用 **event loop** 執行多個非同步方法。
### Regular Expression
[./parser.py](./parser.py)
用來辨識連結是否為短連結或重導向，是的話要用爬蟲自動重導向。
### Discord Bot Py
[./app.py](./app.py) 機器人本體。
## Discord Bot 使用說明
[PMC Collection Downloader](https://www.planetminecraft.com/mod/collection-downloader-discord-bot-5470111/)