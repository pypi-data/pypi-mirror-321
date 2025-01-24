#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    程序说明xxxxxxxxxxxxxxxxxxx
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2025/1/14    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import time
import inspect
import requests
import threading
import multiprocessing
import concurrent.futures
from multiprocessing import Process


class GoFun:
    def __init__(self, ini_dict, logger, go_task_function=None):
        # 读取配置信息
        host = ini_dict.get('host', '')
        port = ini_dict.get('port', 0)
        task = ini_dict.get('task', '')
        auto = ini_dict.get('auto', '')
        processes_num = ini_dict.get('processes_num', 0)
        thread_num = ini_dict.get('thread_num', 0)
        restart_time = ini_dict.get('restart_time', 0)

        self.__ini_info = {
            "host": host,
            "port": port,
            "task": task,
            "auto": auto,
            "processes_num": processes_num,
            "thread_num": thread_num,
            "restart_time": restart_time,
        }

        for server_k, server_v in self.__ini_info.items():
            if not server_v and server_k not in ["port", "processes_num", "thread_num", "restart_time"]:
                raise Exception(f"ini_dict 配置 {server_k} 不存在")

        if port:
            task_host = f"http://{host}:{port}"
        else:
            task_host = f"http://{host}"

        download_url = task_host + "/filter_server/phone/get"
        upload_url = task_host + "/filter_server/phone/update"
        external_ip = self.__get_external_ip()

        self.__ini_info["download_url"] = download_url
        self.__ini_info["upload_url"] = upload_url
        self.__ini_info["external_ip"] = external_ip

        self.logger = logger

        if not go_task_function:
            return

        # 共享任务队列
        download_queue = multiprocessing.Queue()
        upload_queue = multiprocessing.Queue()
        download_task_process = multiprocessing.Process(target=self._download_and_upload_task,
                                                        args=(download_queue, upload_queue, self.__ini_info, logger))
        download_task_process.start()

        # 根据配置启动任务
        if go_task_function:
            go_task_fun_process = multiprocessing.Process(target=self._go_task_fun_task,
                                                          args=(download_queue, upload_queue, self.__ini_info,
                                                                go_task_function, logger))
            go_task_fun_process.start()

    def __get_external_ip(self):
        """
            获取当前网络ip
        :return:
        """
        while True:
            try:
                rp = requests.get('https://httpbin.org/ip')
                rp_json = rp.json()
                print(f"当前网络ip --> {rp_json}")
                return rp_json['origin']
            except Exception as e:
                pass

    def _download_and_upload_task(self, download_queue, upload_queue, ini_info, logger):
        """
            使用两个线程 打开 获取任务、回写任务
        :param queue:
        :return:
        """
        caller = inspect.stack()[1]  # 获取调用者的调用栈信息
        caller_name = caller.function  # 获取调用者的函数名
        caller_class = caller.frame.f_locals.get('self', None)  # 获取调用者的类实例
        if caller_name != "run" or caller_class is None:
            raise Exception("错误调用")
        thread_download_task = threading.Thread(target=self.__download_task, args=(download_queue, ini_info, logger))
        thread_download_task.start()
        thread_upload_task = threading.Thread(target=self.__upload_task, args=(upload_queue, ini_info, logger))
        thread_upload_task.start()

    def __download_task(self, download_queue, ini_info, logger):
        """
            获取任务
        :param queue:
        :return:
        """
        download_url = ini_info["download_url"]
        external_ip = ini_info["external_ip"]
        auto = ini_info["auto"]
        task = ini_info["task"]
        headers = {"Authorization": auto}
        params = {"taskType": task}
        while True:
            qsize = download_queue.qsize()
            logger.info(f"获取任务，当前队列任务数：{qsize}")
            if download_queue.qsize() >= 10:
                time.sleep(2)
                continue
            resp = requests.get(download_url, headers=headers, params=params, timeout=5)
            json_data = resp.json()
            result_list = json_data.get("result", [])
            for task_item in result_list:
                download_queue.put(task_item)
            logger.info(f"成功获取任务个数：{len(result_list)}")

    def __upload_task(self, queue, ini_info, logger):
        """
            回写任务
        :return:
        """
        upload_url = ini_info["upload_url"]
        external_ip = ini_info["external_ip"]
        auto = ini_info["auto"]
        task = ini_info["task"]
        headers = {"Authorization": auto}
        params = {"taskType": task}
        while True:
            qsize = queue.qsize()
            print("回写任务", qsize)
            time.sleep(1)

    def _go_task_fun_task(self, download_queue, upload_queue, ini_info, go_task_function, logger):
        """
            单函数，根据配置启动程序
        :param queue:
        :return:
        """
        caller = inspect.stack()[1]  # 获取调用者的调用栈信息
        caller_name = caller.function  # 获取调用者的函数名
        caller_class = caller.frame.f_locals.get('self', None)  # 获取调用者的类实例
        if caller_name != "run" or caller_class is None:
            raise Exception("错误调用")

        processes_num = ini_info["processes_num"]
        thread_num = ini_info["thread_num"]
        restart_time = ini_info["restart_time"]

        processes_num = 1 if processes_num <= 0 else processes_num
        thread_num = 1 if thread_num <= 0 else thread_num

        go_task_fun_cnt = 0
        processes_start_list = []
        while True:
            try:
                if not processes_start_list:
                    go_task_fun_cnt += 1
                    logger.info(
                        f"第{go_task_fun_cnt}次,进程数:{processes_num},线程数:{thread_num},等待{restart_time}秒强制下一次")
                    for i in range(processes_num):
                        p = Process(target=self._run_with_timeout,
                                    args=(download_queue, upload_queue, thread_num, go_task_function))
                        processes_start_list.append(p)
                        p.start()

                if not restart_time:
                    # 一直执行 不退出
                    continue

                time.sleep(restart_time)
                # 关闭所有进程
                for p in processes_start_list:
                    p.terminate()
                    p.join()  # 等待进程确实结束
                processes_start_list = []

            except Exception as e:
                pass

    def _run_with_timeout(self, download_queue, upload_queue, thread_num, go_task_function):
        caller = inspect.stack()[1]  # 获取调用者的调用栈信息
        caller_name = caller.function  # 获取调用者的函数名
        caller_class = caller.frame.f_locals.get('self', None)  # 获取调用者的类实例
        if caller_name != "run" or caller_class is None:
            raise Exception("错误调用")

        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
            # 提交10个函数到线程池中执行
            futures = [executor.submit(go_task_function, download_queue, upload_queue) for _ in range(thread_num)]

            # 等待所有线程完成
            for future in concurrent.futures.as_completed(futures):
                future.result()
