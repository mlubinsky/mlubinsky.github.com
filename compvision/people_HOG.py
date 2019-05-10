# https://ubidots.com/blog/people-counting-with-opencv-python-and-ubidots/
# https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2
import requests
import time
import argparse
import time
import base64

'''
Usage:

python peopleCounter.py -i PATH_TO_IMAGE  # Reads and detect people in a single local stored image
python peopleCounter.py -c true    # Attempts to detect people using webcam

IMPORTANT: This example is given AS IT IS without any warranty

Made by: Jose Garcia

'''

URL_EDUCATIONAL = "http://things.ubidots.com"
URL_INDUSTRIAL = "http://industrial.api.ubidots.com"
INDUSTRIAL_USER = True  # Set this to False if you are an educational user
TOKEN = "...."  # Put here your Ubidots TOKEN
DEVICE = "detector"  # Device where will be stored the result
VARIABLE = "people"  # Variable where will be stored the result

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detector(image):
    '''
    @image is a numpy array
    '''

    clone = image.copy()

    (rects, weights) = HOGCV.detectMultiScale(image, winStride=(4, 4),
                                              padding=(8, 8), scale=1.05)

    print(rects)
    print(weights)
    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        print ("inside rects:",x,y,w,h)
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Applies non-max supression from imutils package to kick-off overlapped
    # boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    #if result:
    print ("result=")
    print (result)
    return result


def buildPayload(variable, value, context):
    return {variable: {"value": value, "context": context}}


def sendToUbidots(token, device, variable, value, context={}, industrial=True):

    return

    # Builds the endpoint
    url = URL_INDUSTRIAL if industrial else URL_EDUCATIONAL
    url = "{}/api/v1.6/devices/{}".format(url, device)

    payload = buildPayload(variable, value, context)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    attempts = 0
    status = 400

    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    return req


def argsParser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default=None,
                    help="path to image test file directory")
    ap.add_argument("-c", "--camera", default=False,
                    help="Set as true if you wish to use the camera")
    args = vars(ap.parse_args())

    return args


def localDetect(image_path):
    result = []
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    clone = image.copy()
    if len(image) <= 0:
        print("[ERROR] could not read your local image")
        return result
    print("[INFO] Detecting people")
    result = detector(image)

    # shows the result
    for (xA, yA, xB, yB) in result:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("result.png", np.hstack((clone, image)))
    return (result, image)


def cameraDetect(token, device, variable, sample_time=5):
    print ("Before VideoCapture")
    cap = cv2.VideoCapture(0)
    init = time.time()

    # Allowed sample time for Ubidots is 1 dot/second
    if sample_time < 1:
        sample_time = 1
    print ("Before while")

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        result = detector(frame.copy())

        # shows the result
        for (xA, yA, xB, yB) in result:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        cv2.imshow('frame', frame)

        # Sends results
        if time.time() - init >= sample_time:
            print("[INFO] Sending actual frame results")

            # Converts the image to base 64 and adds it to the context
            b64 = convert_to_base64(frame)
            context = {"image": b64}

            sendToUbidots(token, device, variable, len(result), context=context)
            init = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def convert_to_base64(image):
    image = imutils.resize(image, width=400)
    img_str = cv2.imencode('.png', image)[1].tostring()
    b64 = base64.b64encode(img_str)

    return b64.decode('utf-8')


def detectPeople(args):
    image_path = args["image"]
    camera = True if str(args["camera"]) == 'true' else False

    # Routine to read local image
    if image_path != None and not camera:
        print("[INFO] Image path provided, attempting to read image")
        (result, image) = localDetect(image_path)
        print("[INFO] sending results")
        # Converts the image to base 64 and adds it to the context
        b64 = convert_to_base64(image)
        context = {"image": b64}


        # Sends the result
        req = sendToUbidots(TOKEN, DEVICE, VARIABLE,
                            len(result), context=context)
        #if req.status_code >= 400:
        #    print("[ERROR] Could not send data to Ubidots")
        #    return req

    # Routine to read images from webcam
    if camera:
        print("[INFO] reading camera images")
        cameraDetect(TOKEN, DEVICE, VARIABLE)


def main():
    args = argsParser()
    detectPeople(args)


if __name__ == '__main__':
    main()
