import easyocr
import pyautogui
import time

still_follow = ['公众平台安全助手', '微信公众平台', '微信转账助手']
reader = easyocr.Reader(['ch_sim','en'])

for i in range(40):
    image = pyautogui.screenshot('name.png', region=(760, 841, 211, 27))
    name = reader.readtext('name.png', detail = 0)[0]
    if name in still_follow:
        print('保留公众号【' + name + '】')
        pyautogui.click(x = 760, y = 841)
        pyautogui.press('down')                # 跳过该公众号
    else:
        pyautogui.rightClick(x = 760, y = 841) # 右键选择公众号
        pyautogui.click(x = 820, y = 893)      # 左键点击不再关注
        pyautogui.click(x = 1067, y = 607)     # 左键确认不再关注
        print('取关公众号【' + name + '】')
        time.sleep(4)                          # 等待 4 秒