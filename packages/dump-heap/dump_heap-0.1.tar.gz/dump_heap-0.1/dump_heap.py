#!/usr/bin/env python3

import sys

def exit_and_print_useage():
    """
    退出程序并打印使用说明。
    
    Args:
        无参数。
    
    Returns:
        无返回值。
    
    Raises:
        无异常抛出。
    """
    print("Usage: python3 dump_heap.py <PID>")
    sys.exit(1)

def dump_memory(pid, start, end, outfile):
    """
    将指定进程的内存区域导出到文件中。
    
    Args:
        pid (int): 进程ID。
        start (str): 起始内存地址，以十六进制表示。
        end (str): 结束内存地址，以十六进制表示。
        outfile (str): 输出文件的路径。
    
    Returns:
        None
    
    Raises:
        IOError: 当无法打开或读取内存文件时抛出。
    """
    mem_file = "/proc/{}/mem".format(pid)
    try:
        f = open(mem_file, "rb+")
        f.seek(int(start, 16))
        data = f.read(int(end, 16)-int(start, 16))
        with open(outfile, 'wb') as fp:
            fp.write(data)
        f.close()
    except IOError as e:
        print("Error: {}".format(e))
        f.close()
        sys.exit(1)
        
def detect_heap(pid):
    """
    检测指定进程的堆内存范围
    
    Args:
        pid (int): 目标进程的PID
    
    Returns:
        tuple: 包含堆内存起始地址和结束地址的元组，如果检测失败则返回(0, 0)
    
    Raises:
        SystemExit: 如果无法读取/proc/{pid}/maps文件，则退出程序并返回状态码1
    
    """
    start, end = 0, 0
    maps_file = "/proc/{}/maps".format(pid)
    try:
        f = open(maps_file, "r")
        for line in f:
            slice = line.split()
            if slice[-1] == "[heap]":
                addr = slice[0].split("-")
                start, end = addr[0], addr[1]
    except IOError as e:
        print("Error: {}".format(e))
        sys.exit(1)
    finally:
        f.close()
    return start, end

def dump_heap(pid, outfile="{}.heapdump.bin"):
    """
    将指定进程的堆内存数据导出到文件中。
    
    Args:
        pid (int): 进程ID
        outfile (str, optional): 导出文件的名称，默认为"{}.heapdump.bin"，其中"{}"会被替换为进程ID。
    
    Returns:
        None
    
    Raises:
        ValueError: 如果无法检测到堆内存范围，则引发异常。
    """
    heap_start, heap_end = detect_heap(pid)
    dump_memory(pid, heap_start, heap_end, outfile)
def main():
    if len(sys.argv) < 2:
        exit_and_print_useage()
    # print(sys.argv)

    pid = sys.argv[1]
    dump_heap(pid)

if __name__ == "__main__":
    main()