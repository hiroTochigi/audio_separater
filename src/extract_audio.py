import os
import subprocess

preclip_video_dir = '/analyze/video/'
video_dir = '/analyze/result/'
audio_dir = '/analyze/audio/input/'
s_time = '01:47'
video = ''

def main():
    for root, dirs, files in os.walk(f'{preclip_video_dir}'):
        if dirs:
            continue
        video = [ f for f in files ][0]

    subprocess.run(
            ['ffmpeg', '-i', f'{os.path.join(preclip_video_dir, video)}','-ss', f'{s_time}', '-c:v',
            'libx264', '-crf', '30', f'{video_dir}clip_{video}']
        )

    for (root,dirs,video_file_list) in os.walk(f'{video_dir}'):
        for video_file in video_file_list:
            audio_file = f'{"".join(video_file.split(".")[:-1])}.mp3'
            subprocess.run(
                    ['ffmpeg', '-i', f'{video_dir}{video_file}', '-q:a', '0',
                    '-map', 'a', f'{audio_dir}{audio_file}']
                )

if __name__ == "__main__":
    main()

