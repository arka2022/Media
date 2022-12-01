import cv2
from scenedetect import (
    open_video,
    StatsManager,
    SceneManager,
    AdaptiveDetector,
    VideoManager, ThresholdDetector, ContentDetector,
)
from starlette.responses import JSONResponse
from starlette.responses import JSONResponse
from utils.utils import download_file_from_s3, upload_file_to_s3
from utils.constants import *




def downloadVideoFromS3(test_video_file):
    download_file_from_s3(test_video_file, os.getcwd())

def adaptiveScreenDetection(test_video_file):
    try:
        video_path = test_video_file
        video_stream = open_video(video_path, backend="pyav")
        video_manager = VideoManager([video_path])
        stats_manager = StatsManager()
        # Construct our SceneManager and pass it our StatsManager.
        scene_manager = SceneManager(stats_manager)
        # Add ContentDetector algorithm (each detector's constructor
        # takes various options, e.g. threshold).
        detector = AdaptiveDetector(
            adaptive_threshold=25.0,
            luma_only=True,
            min_scene_len=40,
            min_delta_hsv=15.0,
            window_width=10,
            video_manager=None,
        )
        scene_manager.add_detector(detector)
        # Perform scene detection.
        scene_manager.detect_scenes(video=video_stream)
        scene_list = scene_manager.get_scene_list()
        video_manager.set_downscale_factor()
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        print(f"{len(scene_list)} scenes detected!")
        # create a list to store start time
        list = []
        for scene in scene_list:
            start, end = scene
            # your code
            # print(f'{start.get_seconds()} - {end.get_seconds()}')
            list.append(int(start.get_seconds()))
        return list
    except Exception as e:
        print(e)
        print("Exception raises on adaptiveScreenDetection")
def thresholdSceneDetection(test_video_file):
    try:
        video_path = test_video_file
        video_stream = open_video(video_path, backend="pyav")
        stats_manager = StatsManager()
        video_manager = VideoManager([video_path])
        # Construct our SceneManager and pass it our StatsManager.
        scene_manager = SceneManager(stats_manager)
        # Add ContentDetector algorithm (each detector's constructor
        # takes various options, e.g. threshold).
        detector = ThresholdDetector(
            threshold=3,
            min_scene_len=180,
            fade_bias=-0.0,
            add_final_scene=False,
            block_size=None
        )
        scene_manager.add_detector(detector)
        # Perform scene detection.
        video_manager.start()
        scene_manager.detect_scenes(video=video_stream)
        scene_list = scene_manager.get_scene_list()
        print(f"{len(scene_list)} scenes detected!")
        list=[]
        for scene in scene_list:
            start, end = scene
            list.append(int(start.get_seconds()))
        return list
    except Exception as e:
        print(e)
    finally:
        video_manager.release()
def contentdetSceneSetection(test_video_file):
    video_path = test_video_file
    video_manager = VideoManager([video_path])
    try:
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)
        scene_manager.add_detector(ContentDetector(threshold=30))
        video_manager.set_downscale_factor()
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        scene_list = scene_manager.get_scene_list()
        print(f'{len(scene_list)} scenes detected!')
        list = []
        for scene in scene_list:
            start, end = scene
            list.append(int(start.get_seconds()))
        return list
    except Exception as e:
        print(e)
    finally:
        video_manager.release()
def getFPS(vid_source):
    try:
        vid = cv2.VideoCapture(os.getcwd() + os.sep + vid_source)
        fps = vid.get(cv2.CAP_PROP_FPS)
        return int(fps)
    except Exception as e:
        print(e)
        print("Exception raises on getFPS")
def getDuration(vid_source):
    try:
        vid = cv2.VideoCapture(os.getcwd() + os.sep + vid_source)
        frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)
        seconds = round(frames / getFPS(vid_source))
        return seconds
    except Exception as e:
        print(e)
def ExtractImages(vid_src, img_dest, time):
    try:
        cap = cv2.VideoCapture(os.getcwd() + os.sep + vid_src)
        time_length = getDuration(vid_src)
        fps = getFPS(vid_src)
        frame1 = fps * time
        cap.set(1, frame1)
        img_name = img_dest + '/img_' + str(time) + '.jpg'
        ret, frame = cap.read()  # Read the frame
        cv2.imwrite(img_name, frame)
        # write on s3 bucket
        upload_file_to_s3(img_dest, img_name)
        cap.release()
        # cv2.destroyAllWindows()
        return img_name
    except Exception as e:
        print(e)
        print("exception raises from ExtractImages")
def createJson(vid_src, img_dest):
    try:
        start_time_list = adaptiveScreenDetection(os.getcwd() + os.sep + vid_src)
        processed_data = []
        for i in start_time_list:
            startTime = i
            imgUrl = ExtractImages(vid_src, img_dest, i)
            obj = {
                "start": startTime,
                "imageURL": f"{cloud_front}{s3_bucket_name}/{imgUrl}"
            }
            processed_data.append(obj)
        # write processed data into json
        # with open(jsonFile, 'w') as f:
        #     json.dump(processed_data, f)
        #     upload_file_to_s3(img_dest, jsonFile)
        # return as  a json object
        return JSONResponse(processed_data)
    except Exception as e:
        print(e)
        print("Exception raises on CreateJson")


