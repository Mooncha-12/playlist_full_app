import time
import threading

class Song:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def getDuration(self):
        return self.duration

    def getName(self):
        return self.name


class Node:
    def __init__(self, song, next = None, previous=None):
        self.song = song
        self.next = next
        self.previous = previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def addsong(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.previous = self.tail
            new_node.next = self.head
        else:
            new_node.previous = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.previous = self.tail

        self.length += 1



class Operation:
    def __init__(self):
        self.playlist = DoublyLinkedList()
        self.current_node = None
        self.paused = True
        self.current_duration = 0
        self.const_checking = True
        self.count = 0
        self.event = threading.Event()
        self.play_thread = threading.Thread(target=self.run)
        self.play_thread.start()

    def add_song(self, song):
        self.playlist.addsong(song)


    def set_current_node(self, node):
        self.current_node = node

    def run(self):
        if self.current_node is None:
            self.current_node = self.playlist.head
        while True:
            if self.current_node is not None and not self.paused:

                n = self.current_node.song
                print()
                print(f"Playing: {n.getName()}")
                for i in range(self.current_duration, n.getDuration()):

                    if self.paused:
                        break
                    time.sleep(0.5)
                    print("#", end="")
                    self.current_duration += 1

                if not self.paused:
                    self.current_node = self.current_node.next
                    self.current_duration = 0
                if self.count == 1 and self.const_checking:
                    self.paused = False

            if self.event.is_set():
                break
    def play(self):
        self.paused = False
        self.count = 1


    def pause(self):
        self.paused = True
        self.count = 0



    def next_song(self):
        self.const_checking = False
        self.paused = True
        self.current_node = self.current_node.next
        self.current_duration = 0
        self.const_checking = True

    def previous_song(self):
        self.const_checking = False
        self.paused = True
        self.current_node = self.current_node.previous
        self.current_duration = 0
        self.const_checking = True

    def stop(self):
        self.paused = True
        self.event.set()
        self.play_thread.join()