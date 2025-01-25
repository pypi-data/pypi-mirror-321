import psutil
import time


def get_network_speed():
  # 获取初始网络I/O统计信息
  net_io_before = psutil.net_io_counters()

  # 等待1秒钟
  time.sleep(1)

  # 获取1秒后的网络I/O统计信息
  net_io_after = psutil.net_io_counters()

  # 计算发送和接收的字节数差值
  bytes_sent = net_io_after.bytes_sent - net_io_before.bytes_sent
  bytes_recv = net_io_after.bytes_recv - net_io_before.bytes_recv

  # 将字节数转换为Mbps
  sent_speed = bytes_sent * 8 / 1024 / 1024
  recv_speed = bytes_recv * 8 / 1024 / 1024

  return sent_speed, recv_speed


if __name__ == "__main__":
  sent_speed, recv_speed = get_network_speed()
  print(f"发送速度: {sent_speed:.2f} Mbps")
  print(f"接收速度: {recv_speed:.2f} Mbps")
