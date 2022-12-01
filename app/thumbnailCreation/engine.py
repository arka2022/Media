from app.thumbnailCreation.functions import downloadVideoFromS3, adaptiveScreenDetection, getFPS, \
    thresholdSceneDetection, contentdetSceneSetection, createJson_adaptive


def thumbnail_using_adaptive(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    adaptiveScreenDetection(video_Source)
    getFPS(video_Source)
    finalJson = createJson_adaptive(video_name, image_dest)
    return finalJson



