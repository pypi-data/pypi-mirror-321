#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.11.26 19:00:00                  #
# ================================================== #

import time

from PySide6.QtCore import Slot, Signal
from pygpt_net.plugin.base.worker import BaseWorker, BaseSignals


class WorkerSignals(BaseSignals):
    playback = Signal(object, str)
    stop = Signal()


class Worker(BaseWorker):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.args = args
        self.kwargs = kwargs
        self.plugin = None
        self.text = None
        self.event = None
        self.cache_file = None  # path to cache file
        self.mode = "generate"  # generate|playback
        self.audio_file = None

    @Slot()
    def run(self):
        try:
            if self.mode == "generate":
                self.generate()
            elif self.mode == "playback":
                self.play()
        except Exception as e:
            self.error(e)

    def generate(self):
        """
        Generate and play audio file
        """
        if self.text is None or self.text == "":
            time.sleep(0.2)  # wait
            return
        path = self.plugin.get_provider().speech(self.text)
        if path:
            from pygame import mixer
            mixer.init()
            playback = mixer.Sound(path)
            self.stop_playback()  # stop previous playback
            playback.play()
            self.send(playback)  # send playback object to main thread to allow force stop

            # store in cache if enabled
            if self.cache_file:
                self.cache_audio_file(path, self.cache_file)

    def play(self):
        """
        Play audio file only
        """
        if self.audio_file:
            from pygame import mixer
            mixer.init()
            playback = mixer.Sound(self.audio_file)
            playback.play()
            self.send(playback)  # send playback object to main thread to allow force stop

    def cache_audio_file(self, src: str, dst: str):
        """
        Store audio file in cache

        :param src: source path
        :param dst: destination path
        """
        import shutil
        try:
            shutil.copy(src, dst)
            # print("Cached audio file:", dst)
        except Exception as e:
            self.error(e)

    def send(self, playback):
        """
        Send playback object to main thread

        :param playback: playback object
        """
        self.signals.playback.emit(playback, self.event)

    def stop_playback(self):
        """Stop audio playback"""
        self.stop()

    def stop(self):
        """Send stop signal to main thread"""
        self.signals.stop.emit()
