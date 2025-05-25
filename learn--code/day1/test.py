import requests

def download_file(url, save_path):
    try:
        # 设置HTTP头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # 发送GET请求
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 写入文件
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"文件已保存至：{save_path}")

    except Exception as e:
        print(f"下载失败：{str(e)}")

if __name__ == "__main__":
    # 使用示例（请替换为合法的测试URL）
    test_url = "https://storage.jamendo.com/download/p500608900/mp32"
    save_path = "demo1_music.mp3"
    
    download_file(test_url, save_path)
