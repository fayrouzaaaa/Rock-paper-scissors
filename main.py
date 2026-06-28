import cv2 as cv
import time
import GameManager as gm
import HandTracker as hd
import PositionDetector as pd

capture = cv.VideoCapture(0)
play = False
shoot = False
timer = 0
background = cv.imread("images/bg.png")
kiki = cv.imread("images/default.png")
game_manager = gm.GameManager()
hand_tracker = hd.HandTracker()

while True:
    success, video = capture.read()

    video = cv.flip(video, 1)
    video = cv.resize(video, (0,0), None, 0.53, 0.53)
    video = video[:,48:302]

    if play:
        if not shoot:
            hand_tracker.detect(video)
            timer = int(time.time()) - start_time

            if timer == 1:
                background = cv.imread("images/bg_rock.png")

            elif timer == 2:
                background = cv.imread("images/bg_paper.png")

            elif timer==3:
                background = cv.imread("images/bg_scissors.png")

            elif timer == 4:
                shoot = True
                play = False
                background = cv.imread("images/bg_shoot.png")
                position_detector = pd.PositionDetector(hand_tracker, video)
                human_play = position_detector.hand_position()
                computer_play = game_manager.choose_play()
                kiki = cv.imread(f'images/{computer_play}.png')
                if not human_play == 0:
                    game_manager.determine_winner(human_play, computer_play)


    if not play and timer > 0:
        timer = int(time.time()) - start_time
        if timer == 6:
            background = cv.imread("images/bg.png")
            timer = 0

    background[183:437, 386:640] = video
    background[227:405, 98:276] = kiki

    cv.putText(background, str(game_manager.get_computer_score()),
               (280, 510), cv.FONT_HERSHEY_SIMPLEX, 1.8, (69, 12, 38),5)
    cv.putText(background, str(game_manager.get_human_score()),
               (600, 510), cv.FONT_HERSHEY_SIMPLEX, 1.8,(69,12,38),5)


    cv.imshow("Rock, Paper, Scissors!", background)
    key = cv.waitKey(1)


    if cv.getWindowProperty("Rock, Paper, Scissors!", cv.WND_PROP_VISIBLE) < 1:
        break


    if key == ord('\r'):
        play = True
        shoot = False
        start_time = int(time.time())

capture.release()
cv.destroyAllWindows()
