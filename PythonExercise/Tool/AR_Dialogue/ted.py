import requests
import json
import base64
import os
import logging
import speech_recognition as sr
import cv2
import math
import dlib
from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import threading

def get_token():
    logging.info('开始获取token...')
    #获取token
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "up7sdaBHdk09sbMk1l6ijszx"
    client_secret = "XmoFEcE4i8ErqBbnuSlgWb2B81AKXard"

    #拼url
    url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token

def audio_baidu(filename):
    logging.info('开始识别语音文件...')
    with open(filename, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(filename)
    token = get_token()
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": "1536",
        "speech": speech,
        "cuid": "TEDxPY",
        "len": size,
        "channel": 1,
        "token": token,
    }
    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)
    global talk
    if result["err_msg"] == "success.":
        print(result['result'])
        temp=result['result'][0]
        text=""
        while temp:
            text += temp[:10]+"\n"
            temp = temp[10:]
        talk = text
        return result['result']
    else:
        talk="#@&%@##@@#zz!"
        print("内容获取失败，重新获取语音信息")
        return -1
def yuyin():
    logging.basicConfig(level=logging.INFO)
    wav_num = 0
    while True:
        r = sr.Recognizer()
        #启用麦克风
        mic = sr.Microphone()
        logging.info('录音中...')
        with mic as source:
            #降噪
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        with open(f"00{wav_num}.wav", "wb") as f:
            #将麦克风录到的声音保存为wav文件
            f.write(audio.get_wav_data(convert_rate=16000))
        logging.info('录音结束，识别中...')
        target = audio_baidu(f"00{wav_num}.wav")
        wav_num += 1
        if target == -1:
            continue


def chatbox():

    chatpng = "chat.png"

    #opencv启用摄像头
    cap = cv2.VideoCapture(0)

    #dlib面部识别模块相关
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    #定义图片名称，temp为摄像头最初抓取的图像，result为最终处理后生成图像
    temp = "temp.jpg"
    result = "result.png"

    while True:
        #将摄像头抓取到的结果进行赋值
        _, frame = cap.read()
        #将抓到的数据写入temp图片
        cv2.imwrite(temp,frame)
        #通过PIL重新打开图片，因为后续需要PIL贴图操作，所以要使用PIL模块打开
        im = Image.open(temp)

        #在摄像头抓取的数据中进行面部识别
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            #获取面部模式
            landmarks = predictor(gray,face)
            x1, y1 = landmarks.part(16).x, landmarks.part(16).y

            chatBox= Image.open(chatpng)
            resized1 = chatBox.resize((300, 200))
            im.paste(resized1, (int(x1), int(y1-200)), resized1)
            im.save(result)

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('simhei.ttf', 20)
            draw.text((int(x1+50), int(y1-150)),talk,fill="rgb(255,255,255)",font=font)


        #将窗口定义为可调节大小
        cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
        #将result图片展示在窗口中
        #cv2.imshow("Frame", cv2.imread(result))
        cv2.imshow("Frame",np.array(im)[:,:,::-1])

        key = cv2.waitKey(1)
        #按ESC键退出摄像头视频
        if key==27:
            break

    #退出摄像头、关闭窗口
    cap.release()
    cv2.destroyAllWindows()



talk="Hello World!"
threads = []

t1 = threading.Thread(target=chatbox, args=())
threads.append(t1)
t2 = threading.Thread(target=yuyin, args=())
threads.append(t2)

if __name__ == "__main__":
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print("Let's go")
