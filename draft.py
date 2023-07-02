from moviepy.editor import VideoFileClip
import imageio
import random

def save_random_frame_as_jpg(video_path, output_path):
    video = VideoFileClip(video_path)
    print(type(video.duration))
    # Получение случайного времени кадра в секундах
    frame_time = 36 #random.randint(0, int(video.duration))
    print(frame_time)
    # Получение кадра по случайному времени
    frame = video.get_frame(frame_time)
    video.close()
    
    output_path_jpg = output_path + ".jpg"
    imageio.imwrite(output_path_jpg, frame)
    print("Случайный кадр сохранен по пути:", output_path_jpg)

# Пример использования
video_path = "./data/v.mp4"
output_path = "data/aaa"

save_random_frame_as_jpg(video_path, output_path)