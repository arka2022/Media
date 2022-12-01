from app.thumbnailCreation.functions import downloadVideoFromS3, adaptiveScreenDetection, getFPS, \
    contentdetSceneSetection, createJson_adaptive, createJson_content, createJson_threshold


def thumbnail_using_adaptive(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    finalJson = createJson_adaptive(video_name, image_dest)
    return finalJson

def thumbnail_using_content(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    finalJson = createJson_content(video_name, image_dest)
    return finalJson

def thumbnail_using_threshold(video_name,video_s3_path):
    video_Source = f"{video_s3_path}/{video_name}" if video_s3_path else video_name
    image_dest = "thumbnails"  # image folder
    downloadVideoFromS3(video_Source)
    finalJson = createJson_threshold(video_name, image_dest)
    return finalJson

