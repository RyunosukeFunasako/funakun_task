work_space/multiple_plots
===
1分子動画の軌跡描画ソフトの言語移行(MATLAB &rarr; Python)

## Description
MATLABで書かれていた1分子動画の軌跡描画ソフトをPythonで書き直した.<br>
ファイル構成は以下のようになっている.

+ data
    + video1
        + edited
            + edited_video.mp4
            + original_video_00.mp4(original_videoを4分割した際の左上)
            + original_video_01.mp4(original_videoを4分割した際の左下)
            + original_video_10.mp4(original_videoを4分割した際の右上)
            + original_video_11.mp4(original_videoを4分割した際の右下)
        + Original_mov2.mp4
        + Tracks2
            + datファイル
+ video_split.py
+ original_images
    + 作成された画像
+ original_images_00
    + 作成された画像(original_imageを4分割した際の左上)
+ original_images_01
    + 作成された画像(original_imageを4分割した際の左下)
+ original_images_10
    + 作成された画像(original_imageを4分割した際の右上)
+ original_images_11
    + 作成された画像(original_imageを4分割した際の右下)
+ frame_count.py
+ expansion.py
+ xyposition_getter.py
+ figure_draw.py
+ figure_images
    + 作成された画像
+ trajectory_draw.py
+ trajectory_images
    + 作成された画像
+ video_write.py
+ main.py
+ requirements.txt
+ README.md

## Requirement
* Python 3.9.6
* opencv-python(cv2)
* pandas
* numpy

## Usage
このリポジトリをcloneし, 作成せされたmultiple_plotsディレクトリ上で`python3 main.py`のようにして`main.py`を実行する必要がある. <br>

また, `main.py`にて<br>
+ プロットする分子の数
+ プロットする図形のタイプ(circle, square)
+ 図形の色(white, light_blue, pink, purple, blue, yellow, yellow_green, red, orange)
+ プロットする軌跡のタイプ(disappear, keep)
+ 軌跡の色(図形の色と同様)

を選択することができる. <br>

拡大画像または動画を作成したい場合は`python3 expansion.py`のようにして`expansion.py`を実行する必要がある.
