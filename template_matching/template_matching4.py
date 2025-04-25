#!/usr/bin/env python3

# ライブラリのインポート
import cv2


# 対象の画像を読み込む
image = cv2.imread("images/target4.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# テンプレートの画像を読み込む
template = cv2.imread("images/template4.jpg")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h, w = template_gray.shape

## テンプレートマッチングを実行
# 特徴マップを算出
res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF)

# 特徴マップから特徴量が最大の位置を抽出
max_feature_value = 0
for r_h in range(res.shape[0]):
    for r_w in range(res.shape[1]):
        if res[r_h][r_w] > max_feature_value:
            max_feature_value = res[r_h][r_w]
            max_loc = (r_w, r_h)
print(max_feature_value)
print(max_loc)


# 検出位置にバウンディングボックスを描画
bottom_right = (max_loc[0] + w, max_loc[1] + h)
cv2.rectangle(image , max_loc, bottom_right, 255, 20)

# 検出結果を可視化
image = cv2.resize(image, (int(image.shape[1] / 2), int(image.shape[0] / 2)))
template = cv2.resize(template, (int(template.shape[1] / 2), int(template.shape[0] / 2)))
cv2.imshow("target", image)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
