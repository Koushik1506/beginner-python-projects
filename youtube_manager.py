import json


class Yt:
    def __init__(self, name, file, del_file):
        self.name = name
        self.file_name = file
        self.deleted_file = del_file
        self.deleted_video = None
        # self.videos = self.fetch_data()
        # self.deleted_videos = self.fetch_del_data()
        print(f"\nHello {self.name}!")
        # print("\n")
        print("*" * 158)
        print("                                                            Welcome To \"Youtube Video Manager\" Application")
        print("*" * 158)
        print("\n")
        while True:
            self.videos = self.fetch_data()  # fetch information of added videos if any exists
            self.deleted_videos = self.fetch_del_data()  # fetch information of deketed videos if any exists
            print("Please Enter any Option\n1.Add a Video\n2.List all your Videos\n3.Update a Video\n4.Delete a Video\n5.Recycle Bin\n6.Exit App")
            choice = input()
            match choice:
                case "1":
                    self.add_video()
                case "2":
                    self.list_videos()
                case "3":
                    self.update_video()
                case "4":
                    self.delete_video()
                case "5":
                    self.recycle_bin()
                case "6":
                    exit()
                case _:
                    print("Invalid Option")
            print("\n")

    def fetch_data(self):
        try:
            with open(f"{self.file_name}", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def fetch_del_data(self):
        try:
            with open(f"{self.deleted_file}", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_video(self):
        video_name = input("Enter Video Name: ")
        video_time = input("Enter video Duration: ")
        self.videos.append({"name": video_name, "Duration": video_time})
        print("\n\"Added Successfully\"")
        self.save_to_files(self.videos)  #updating latest information about changes

    def list_videos(self):
        if len(self.videos) == 0:
            print("No Videos to Display")
        else:
            for index, video in enumerate(self.videos, start=1):
                print(f"{index}. video name: {video["name"]}, video duration: {video["Duration"]}")

    def update_video(self):
        self.list_videos()
        idx = int(input("Enter video number to update: "))
        new_video_name = input("Enter new video name: ")
        new_video_duration = input("Enter new video Duration: ")
        self.videos[idx - 1]["name"] = new_video_name
        self.videos[idx - 1]["Duration"] = new_video_duration
        print("\n\"Updated Successfully\"")
        self.save_to_files(self.videos)

    def delete_video(self):
        if len(self.videos) > 0:
            self.list_videos()
            idx = int(input("Enter video number to delete: "))
            print("\n\"Deleted Successfully\"")
            self.deleted_video = self.videos.pop(idx - 1)
            self.deleted_videos.insert(0, self.deleted_video)
            self.save_to_files(self.videos)
            self.save_to_del_files(self.deleted_videos)
        else:
            self.list_videos()

    def recycle_bin(self):  # Recycle bin functionality
        try:
            with open(f"{self.deleted_file}", "r") as file:
                del_vid_list = json.load(file)
            print("Recently Deleted Videos\n")
            for index, vid in enumerate(del_vid_list, start=1):
                print(f"{index}.video name: {vid["name"]}")
        except FileNotFoundError:
            print("No Videos To Display")

    def save_to_files(self, videos):
        with open(f"{self.file_name}", "w") as file:
            json.dump(videos, file)

    def save_to_del_files(self, del_videos):
        with open(f"{self.deleted_file}", "w") as file:
            json.dump(del_videos, file)


if __name__ == "__main__":
    name_yt_user_1 = input("Enter Your Name: ").capitalize()
    yt_user_1_file = "youtube_1.txt"
    yt_user_1_del_file = "del.txt"
    yt_user_1 = Yt(name_yt_user_1, yt_user_1_file, yt_user_1_del_file)
