import speedtest
import pprint


def print_hi(name):
    print(f"Hi, {name}")


def print_bit():
    hour = float(input("hour : "))
    minute = float(input("minute : "))
    bitrate = float(input("bitrate per second / mbps : "))
    total_flow = bitrate / 8 * (3600 * hour + 60 * minute)
    if total_flow < 1024:
        print(str(float(bitrate) / 8 * float(3600 * hour + 60 * minute)) + "MB")
    else:
        total_flow /= 1024
        print(str(total_flow) + "GB")


def bits_to_mbit(s, b):
    KB = 1000
    MB = KB * 1000
    GB = MB * 1000
    if b > GB:
        print(s, "{:.2f}".format(b / GB), "GiB/s")
    elif b > MB:
        print(s, "{:.2f}".format(b / MB), "MiB/s")
    elif b > KB:
        print(s, "{:.2f}".format(b / KB), "KiB/s")


def menu():
    servers = []
    threads = None
    s = speedtest.Speedtest()
    try:
        print("获取服务器列表...")
        s.get_servers(servers)
    except:
        pass
    try:
        print("获取最佳服务器中...")
        s.get_best_server()
        print("最小延迟 {} ms".formar(s.results.ping))
    except:
        pass
    try:
        print("测试上传中", "...")
        s.upload(threads=threads)
        bits_to_mbit("上传速度： ", s.results.upload)
    except KeyboardInterrupt:
        print("end")
    try:
        print("测试下载中...")
        s.download(threads=threads)
        bits_to_mbit("下载速度：", s.results.download)
    except KeyboardInterrupt:
        print("end")

    # 所有可选择显示信息
    # result_dict = s.results.dict()
    # pprint.pprint(result_dict)
    # print(s.results.client["ip"])


if __name__ == "__main__":
    menu()
