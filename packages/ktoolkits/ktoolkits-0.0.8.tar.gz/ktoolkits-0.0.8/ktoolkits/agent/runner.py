#coding=utf-8

import time
import random
import threading
from tqdm import tqdm
from ktoolkits.client.base_api import BaseApi
from ktoolkits.api_entities.ktool_response import RunnerResponse


class ProgressThread(threading.Thread):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        #最长执行时间5分钟
        self._max_total = 3000

    def terminate(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    
    def run(self):
        progress_bar = tqdm(total=self._max_total, desc="工具正在执行", position=0, leave=True)
        while not self.stopped():
            try:
                self.work(progress_bar)
            except Exception as e:
                print(e)
                break
            finally:
                progress_bar.close()

    def work(self, progress_bar):
        for i in range(self._max_total):
            if self.stopped():
                progress_bar.update(self._max_total)
                progress_bar.close()
                return
            progress_bar.update(30)
            time.sleep(random.uniform(0.1, 0.5))

class Runner(BaseApi):
    task = 'tool-runner'
    """
    API for ktoolkits Runner.
    """
    @classmethod
    def call(
        cls,
        tool_name: str,
        tool_input: str,
        **kwargs
    ) -> RunnerResponse:
        """Call tool runner service.

        Args:
            tool_name (str): The name of requested tool, such as nmap
            tool_input (str): The input for requested tool, such as: scan_target,root_domain etc

        Returns:
            RunnerResponse.
        """
        # 启动进度条线程执行耗时操作
        worker = ProgressThread()
        worker.start()
        
        response = super().call(tool_name=tool_name,
                                tool_input=tool_input)   

        worker.terminate()
        worker.join()   

        is_stream = kwargs.get('stream', False)
        if is_stream:
            return (RunnerResponse.from_api_response(rsp)
                    for rsp in response)
        else:
            return RunnerResponse.from_api_response(response)

