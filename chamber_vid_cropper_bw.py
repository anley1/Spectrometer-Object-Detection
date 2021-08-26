# From: https://stackoverflow.com/questions/61723675/crop-a-video-in-python
import numpy as np
import cv2
import argparse
#
# def parse_args():
#     parser = argparse.ArgumentParser(description='MMDetection video demo')
#     parser.add_argument('vid_path', help='Video file path')
#     parser.add_argument('dims', help='Dimensions [x,y,h,w]')
#     args = parser.parse_args()
#     return args


def main():
    # args = parse_args()
    # cropper(args.vid_path, args.dims)
    vid_path = "C:\\Users\\aleye\\Swin-Transformer-Object-Detection\\data" \
               "\\video\\GH010107.MP4"
    dims = [
            654,
            326,
            1317,
            1056
            ]
    cropper(vid_path, dims)

def cropper(vid_path, dims):
    # Open the video
    cap = cv2.VideoCapture(vid_path)

    # Initialize frame counter
    cnt = 0

    # Some characteristics from the original video
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # Here you can define your croping values
    # 0,0,100,100
    x,y,w,h = dims[0],dims[1],dims[2],dims[3]

    # output
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('GH010107_gray.avi', fourcc, fps, (w_frame, h_frame),
                          isColor=False)


    # Now we start
    while cap.isOpened() and cnt < frames:
        ret, frame = cap.read()

        cnt += 1 # Counting frames

        # Avoid problems when video finish
        if ret:
            # Cropping the frame
            # crop_frame = frame[y:y+h, x:x+w]
            # crop_frame = frame[0:h_frame, 0: w_frame]
            crop_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Percentage
            xx = cnt *100/frames
            print(int(xx),'%')

            # Saving from the desired frames
            #if 15 <= cnt <= 90:
            #    out.write(crop_frame)
            out.write(crop_frame)

            # Just to see the video in real time
            # cv2.imshow('frame',frame)
            # cv2.imshow('cropped',crop_frame)
            #
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break


    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
