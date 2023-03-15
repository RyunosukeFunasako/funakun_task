---

今やること

1フレームごとに細かく分子の編集オプションをつけて動画を編集できるようにする

↓

フロントエンド実装かなー

---

実装メモ

edit\_options = {
    'does\_draw\_figure': 'true',
    'figure\_shape': 'square',
    'figure\_color': 'red',
    'does\_draw\_trajectory': 'true',
    'trajectory\_color': 'red'
}

molecule\_edit\_options\_in\_frame = {
    '1(molecule\_id)': edit\_options(),
}

frame\_edit\_options = {
    '1(frame\_id)': molecule\_edit\_options\_in\_frame(),
}

frame\_id -->\* molecule\_id -->\* options

---

その他のメモ

len(\[\[ f x y \]\]) == frame\_num
f = frame

---
