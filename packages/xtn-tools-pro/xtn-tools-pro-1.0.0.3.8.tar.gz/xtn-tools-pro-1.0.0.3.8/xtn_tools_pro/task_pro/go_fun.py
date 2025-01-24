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
import random
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
        update_proxies_time = ini_dict.get('update_proxies_time', 0)
        upload_task_tine = ini_dict.get('upload_task_tine', 0)

        self.logger = logger

        self.__ini_info = {
            "host": host,
            "port": int(port),
            "task": task,
            "auto": auto,
            "processes_num": int(processes_num),
            "thread_num": int(thread_num),
            "restart_time": int(restart_time),
            "update_proxies_time": int(update_proxies_time),
            "upload_task_tine": int(upload_task_tine),
        }

        for server_k, server_v in self.__ini_info.items():
            if not server_v and server_k not in ["port", "processes_num", "thread_num", "restart_time",
                                                 "update_proxies_time", "upload_task_tine"]:
                raise Exception(f"ini_dict 配置 {server_k} 不存在")

        logger.info(f"\n当前设置配置如下:\n\t功能函数重启间隔:{restart_time};进程数:{processes_num};线程数:{thread_num}\n\t代理更新间隔:{update_proxies_time};回写间隔{upload_task_tine}\n")

        if port:
            task_host = f"http://{host}:{port}"
        else:
            task_host = f"http://{host}"

        download_url = task_host + "/filter_server/phone/get"
        upload_url = task_host + "/filter_server/phone/update"
        update_proxy_url = task_host + f"/filter_server/proxy/random/get?taskType={task}&limit=1"
        logger.info("无敌框架来咯~")

        external_ip = self.__get_external_ip(self.logger)

        self.__ini_info["download_url"] = download_url
        self.__ini_info["upload_url"] = upload_url
        self.__ini_info["update_proxy_url"] = update_proxy_url
        self.__ini_info["external_ip"] = external_ip

        if not go_task_function:
            return

        # 共享任务队列
        manager = multiprocessing.Manager()
        download_queue = multiprocessing.Queue()
        upload_queue = multiprocessing.Queue()
        proxies_dict = manager.dict()
        download_task_process = multiprocessing.Process(target=self._download_and_upload_task,
                                                        args=(download_queue, upload_queue, proxies_dict,
                                                              self.__ini_info, logger))
        download_task_process.start()

        # 根据配置启动任务
        if go_task_function:
            go_task_fun_process = multiprocessing.Process(target=self._go_task_fun_task,
                                                          args=(download_queue, upload_queue, proxies_dict,
                                                                self.__ini_info, go_task_function, logger))
            go_task_fun_process.start()

        download_task_process.join()

    def __get_external_ip(self, logger):
        """
            获取当前网络ip
        :return:
        """
        while True:
            try:
                rp = requests.get('https://httpbin.org/ip')
                rp_json = rp.json()
                logger.info(f"当前网络ip --> {rp_json}")
                return rp_json['origin']
            except Exception as e:
                pass

    def _download_and_upload_task(self, download_queue, upload_queue, proxies_dict, ini_info, logger):
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
        thread_update_proxy = threading.Thread(target=self.__update_proxy, args=(proxies_dict, ini_info, logger))
        thread_update_proxy.start()

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
            try:
                qsize = download_queue.qsize()
                logger.info(f"获取任务，当前队列任务数：{qsize}")
                if qsize >= 10:
                    time.sleep(2)
                    continue
                resp = requests.get(download_url, headers=headers, params=params, timeout=5)
                json_data = resp.json()
                result_list = json_data.get("result", [])

                if len(result_list) <= 0:
                    # 判断任务响应是否为空
                    time.sleep(2)
                    continue
                for task_item in result_list:
                    phone_item = task_item["phone"]
                    if not phone_item.isdigit():  # 判断是否全是整数(不包括小数点或负号)
                        continue
                    download_queue.put(task_item)
                logger.info(f"成功获取任务个数：{len(result_list)}")
            except Exception as e:
                logger.critical(f"获取任务请求异常：{e}")
                time.sleep(2)

    def __upload_task(self, upload_queue, ini_info, logger):
        """
            回写任务
        :return:
        """
        upload_url = ini_info["upload_url"]
        external_ip = ini_info["external_ip"]
        auto = ini_info["auto"]
        task = ini_info["task"]
        upload_task_tine = ini_info["upload_task_tine"]
        headers = {"Authorization": auto}
        params = {"taskType": task}
        while True:
            # 判断队列是否有值
            empty = upload_queue.empty()
            if empty:
                time.sleep(2)
                continue

            # 循环全部获取队列的任务
            result_list = []
            try:
                while True:
                    task_item = upload_queue.get_nowait()
                    taskNo = task_item["taskNo"]
                    phone = task_item["phone"]
                    isRegistered = task_item["isRegistered"]
                    country_region = task_item["country_region"]
                    full_phone = f"{country_region}{phone}"
                    task_item = {
                        'taskNo': taskNo,
                        'phone': full_phone,
                        'isRegistered': isRegistered
                    }
                    result_list.append(task_item)
            except Exception as e:
                pass

            # 回写任务
            data = {"result": result_list, "remoteAddr": external_ip}
            while True:
                try:
                    resp = requests.post(upload_url, json=data, headers=headers, params=params, timeout=5)
                    json_data = resp.json()
                    # logger.info(f"成功回写任务个数:{len(result_list)},{json_data},{data}")
                    logger.info(f"成功回写任务个数:{len(result_list)},{json_data}")
                    break
                except Exception as e:
                    logger.critical(f"回写异常,{len(result_list)},{e}")

            if not upload_task_tine:
                # 一直执行 不退出
                continue
            time.sleep(upload_task_tine)

    def __update_proxy(self, proxies_dict, ini_info, logger):
        """
            更新代理
        :return:
        """
        update_proxy_url = ini_info["update_proxy_url"]
        auto = ini_info["auto"]
        update_proxies_time = ini_info["update_proxies_time"]
        headers = {"Authorization": auto}

        while True:
            try:
                if not proxies_dict.get("status"):
                    resp = requests.get(update_proxy_url, headers=headers, timeout=5)
                    json_data = resp.json()
                    status_code = resp.status_code
                    result_list = json_data.get("result", [])
                    if not result_list or status_code != 200:
                        logger.critical(f"获取代理响应异常：{status_code} {len(result_list)} {json_data}")
                        time.sleep(2)

                    proxies_dict['http'] = 'http://' + random.choice(result_list)
                    proxies_dict['https'] = 'http://' + random.choice(result_list)
                    proxies_dict['status'] = True
                    logger.info(f"成功获取代理：{proxies_dict}")

                if not update_proxies_time:
                    # 一直执行 不退出
                    continue

                time.sleep(update_proxies_time)
                proxies_dict['status'] = False
            except Exception as e:
                logger.critical(f"获取代理请求异常：{e}")
                time.sleep(2)

    def _go_task_fun_task(self, download_queue, upload_queue, proxies_dict, ini_info, go_task_function, logger):
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
                                    args=(download_queue, upload_queue, proxies_dict, thread_num, go_task_function))
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

    def _run_with_timeout(self, download_queue, upload_queue, proxies_dict, thread_num, go_task_function):
        caller = inspect.stack()[1]  # 获取调用者的调用栈信息
        caller_name = caller.function  # 获取调用者的函数名
        caller_class = caller.frame.f_locals.get('self', None)  # 获取调用者的类实例
        if caller_name != "run" or caller_class is None:
            raise Exception("错误调用")

        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
            # 提交10个函数到线程池中执行
            futures = [executor.submit(go_task_function, download_queue, upload_queue, proxies_dict) for _ in
                       range(thread_num)]

            # 等待所有线程完成
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def get_ini_dict(self):
        """
            配置解释
        :return:
        """
        ini_dict = {
            "host": "域名",
            "port": "端口",
            "task": "任务",
            "auto": "token",
            "processes_num": "进程数",
            "thread_num": "线程数",
            "restart_time": "间隔x秒强制重启",
            "update_proxies_time": "间隔x秒更新代理",
            "upload_task_tine": "回写间隔",
        }
        return ini_dict
