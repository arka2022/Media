from app.thumbnailCreation.functions import downloadVideoFromS3, adaptiveScreenDetection, getFPS, createJson, \
    thresholdSceneDetection, contentdetSceneSetection


def thumbnail_using_adaptive(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    adaptiveScreenDetection(video_Source)
    getFPS(video_Source)
    finalJson = createJson(video_name, image_dest)
    return finalJson

def thumbnail_using_threshold(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    thresholdSceneDetection(video_Source)
    getFPS(video_Source)
    finalJson = createJson(video_name, image_dest)
    return finalJson

def thumbnail_using_content(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    contentdetSceneSetection(video_Source)
    getFPS(video_Source)
    finalJson = createJson(video_name, image_dest)
    return finalJson
