# ComfyUI-PromptUtilities
![PromptUtilities Preview](preview.png "PromptUtilities Preview")  
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)用のカスタムノードです。
- プロンプト周りの便利なノードを追加します。

## インストール手順
```
cd <ComfyUIがあるディレクトリ>/custom_nodes
git clone https://github.com/nkchocoai/ComfyUI-PromptUtilities.git
```

## 追加されるノード
### Join String List (実験中)
- 入力として受け取った `argN` を `separator` で結合した文字列を出力します。
- 動作確認が十分にできていないので、バグがあるかもしれません。

![Example Join String List](ex_join.png "Example Join String List")  

### Format String (実験中)
- 入力として受け取った `argN` を `prompt` に埋め込んだ文字列を出力します。
- `prompt` において、 `[N]` は `argN` の値に置き換わります。
- 動作確認が十分にできていないので、バグがあるかもしれません。

![Example Format String](ex_format.png "Example Format String")  

### Load Preset
- 選択したプリセットのプロンプトを出力します。
- プリセットは [presets](presets) ディレクトリ内に配置されたCSVファイルに記載します。

![Example Load Preset](ex_preset.png "Example Load Preset")

### Const String
- 入力した文字列を出力します。

### Const String(multi line)
- 入力した文字列を出力します。
- 複数行で入力できます。
