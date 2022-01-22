import time

import pyautogui

# 置信度
confidence = 0.62
# 最小尺寸
# pos = (0, 0, 1000, 650)
# 适中尺寸
# pos = (0, 0, 1500, 900)
# 默认尺寸
pos = (0, 0, 1920, 1080)
# 牌局内玩家皮肤区域
player_pos = (850, 460, 250, 250)
# 游戏开始时间
game_start_time = 0


def find_btn_and_click(picture_name):
    btn_position = have_btn_position(picture_name)
    if btn_position is not None:
        pyautogui.click(btn_position)
        time.sleep(2)


def have_btn_position(picture_name, rg=pos):
    btn = pyautogui.locateCenterOnScreen('picture/' + picture_name, region=rg, confidence=confidence)
    return btn


if __name__ == '__main__':
    while True:
        if have_btn_position('quickStart.png'):
            print('房间外等待开始游戏')
            print('快速开始')
            find_btn_and_click('quickStart.png')
            time.sleep(3)
        if have_btn_position('addAIPlayer.png'):
            # 在房间等待开始游戏
            print('房间内等待开始游戏')
            if have_btn_position('gameEndResult.png'):
                print('尝试关闭结算页面')
                find_btn_and_click('gameEndResult.png')
            # 添加机器人
            print('一键添加机器人')
            find_btn_and_click('addAIPlayer.png')

            # 添加玫瑰金机器人
            print('添加玫瑰金机器人')
            find_btn_and_click('goldAIPlayer.png')

            # 开始游戏
            print('开始游戏')
            find_btn_and_click('startReady.png')
            # print('确认还有空位开始游戏')
            # find_btn_and_click('yesBtn.png')
            time.sleep(3)
            game_start_time = int(time.time())
        elif have_btn_position('cardsLight.png') or have_btn_position('cardsDark.png'):
            # 牌局内
            if have_btn_position('cancelHostingBtn.png') is None or have_btn_position(
                    'hostingText.png') is None or have_btn_position('hostingTextOnAvator.png') is None:
                # 牌局内等待托管
                print('牌局内等待托管')
                # time.sleep(20)
                # 开始托管
                print('开始托管')
                find_btn_and_click('hostingLight.png')
            else:
                # 牌局内托管中
                print('牌局内托管中')
                if have_btn_position('player3GreyBlood.png', player_pos) and have_btn_position(
                        'playerGreenBlood.png', player_pos) is None and have_btn_position(
                    'playerRedBlood.png', player_pos) is None and have_btn_position('playerYellowBlood.png',
                                                                                    player_pos) is None:
                    print('玩家已经阵亡')
                    game_time = int(time.time()) - game_start_time
                    if game_time > 60:
                        print('游戏时长超过60s')
                        print('退出牌局')
                        find_btn_and_click('backGame.png')
                        print('确定退出牌局')
                        find_btn_and_click('exitGameYesBtn.png')

                # 尝试关闭游戏内全场最佳结算页面
                elif have_btn_position('bestPlayer.png'):
                    print('尝试关闭游戏内全场最佳结算页面')
                    find_btn_and_click('bestPlayer.png')
                    time.sleep(2)
                elif have_btn_position('gameEndResult.png'):
                    print('尝试关闭结算页面')
                    find_btn_and_click('gameEndResult.png')
                else:
                    time.sleep(8)
        else:
            print('未知位置')
            time.sleep(8)
