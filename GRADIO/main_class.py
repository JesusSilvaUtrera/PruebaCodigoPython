import logging
from gradio_ui import UI
import utils
import os
import subprocess

logging.basicConfig(level=logging.INFO)


class UI_DEPLOYMENT(object):

    def __init__(self):

        self.new_ui = UI()

        self.container = []
        self.repo = ""
        self.branch = ""

        self.init_repos = utils.read_yaml_config("repo.yaml")
        self.dict_repos = {}

    def get_docs(self, val, label):
        logging.info(f"{val} {label}")

    def get_docs_btn(self, val):
        logging.info(f"{val}")

    def get_deployment_btn(self, label):
        self.build()

    def interface(self, repo, branch):
        self.container.append([repo, branch])
        return self.container

    def get_repos(self):
        self.names_repos = []
        for repo_url in self.init_repos:
            name = repo_url.split("/")[-1][:-4]
            self.names_repos.append(name)
            self.dict_repos[name] = repo_url

    def build(self):
        logging.info(self.container)
        logging.info(self.dict_repos)
        for get_repo in self.container:
            if get_repo[0] in self.dict_repos:
                repo_url = self.dict_repos[get_repo[0]]
                branch = get_repo[1]
                os.chdir("/home/david-loja-romero/tmp/docs_deployment/tmp")
                pro = subprocess.Popen(["git", "clone", repo_url, "-b", branch])
                pro.wait()

    def run(self):
        self.get_repos()

        with self.new_ui.gr.Blocks() as self.demo:

            with self.new_ui.gr.Tab("DOCS"):
                self.new_ui.docs_template(self.get_docs, self.get_docs_btn)

            with self.new_ui.gr.Tab("CONTAINER REGISTRY"):
                self.new_ui.deployment(
                    self.names_repos,
                    ["develop", "main"],
                    self.get_deployment_btn,
                    self.interface,
                )

            with self.new_ui.gr.Tab("DEPLOYMENT"):
                self.new_ui.deployment(
                    self.names_repos,
                    ["develop", "main"],
                    self.get_deployment_btn,
                    self.interface,
                )

            with self.new_ui.gr.Tab("VISION"):
                threshold = self.new_ui.gr.Slider(
                    0, 255, value=125, label="bin_threshold"
                )
                manometer = self.new_ui.gr.Number(
                    label="Choose manometer to read", value=0
                )

                @self.new_ui.gr.on(inputs=manometer)
                def set_manometer(value):
                    self.chosen_manometer = value
                    print(f"Chosen manometer: {self.chosen_manometer}")

                @self.new_ui.gr.on(inputs=threshold)
                def set_threshold(value):
                    self.bin_threshold = value
                    print(f"Current value of binary threshold: {self.bin_threshold}")

        self.demo.launch(
            server_name="0.0.0.0",
            server_port=7860,
            # share=True
        )


if __name__ == "__main__":
    exec_ = UI_DEPLOYMENT()
    exec_.run()
