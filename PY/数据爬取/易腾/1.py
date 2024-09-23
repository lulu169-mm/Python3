import m3u8
import requests
import os


def download_segment(segment_url, output_dir, segment_num):
    response = requests.get(segment_url, stream=True)
    segment_file = os.path.join(output_dir, f'segment_{segment_num}.ts')
    with open(segment_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    return segment_file


def download_m3u8(m3u8_url, output_dir):
    # 读取M3U8文件
    m3u8_obj = m3u8.load(m3u8_url)
    segment_files = []

    # 下载每个视频片段
    for i, segment in enumerate(m3u8_obj.segments):
        print(f'下载片段 {i + 1}/{len(m3u8_obj.segments)}')
        segment_file = download_segment(segment.uri, output_dir, i)
        segment_files.append(segment_file)

    return segment_files


def merge_segments(segment_files, output_file):
    with open(output_file, 'wb') as merged:
        for segment_file in segment_files:
            with open(segment_file, 'rb') as segment:
                merged.write(segment.read())

    # 删除临时文件
    for segment_file in segment_files:
        os.remove(segment_file)


def main():
    m3u8_file = 'stream.m3u8'  # M3U8文件路径
    output_dir = 'video_segments'  # 临时存储片段的目录
    output_file = 'output_video.mp4'  # 最终输出视频文件

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 下载M3U8文件中的所有视频片段
    segment_files = download_m3u8(m3u8_file, output_dir)

    # 合并所有视频片段到一个文件
    merge_segments(segment_files, output_file)

    print(f'视频已保存为 {output_file}')


if __name__ == '__main__':
    main()
