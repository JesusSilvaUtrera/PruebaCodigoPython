import gradio
import logging

logging.basicConfig(level=logging.INFO)


class UI(object):
    def __init__(self):
        logging.info("INIT UI CONTROL")
        self.gr = gradio

        self.box_text = None

        self.data_deployment = None

    # ! Al definir como callable
    def callback_btn(self, btn, _fn: callable):
        btn.click(_fn, inputs=btn)

    def callback_slider(self, slider, _fn: callable):
        slider.change(_fn, inputs=[slider, self.gr.State(slider.label)])

    def callback_textbox(self, textbox, _fn: callable):
        textbox.change(_fn, inputs=[textbox, self.gr.State(textbox.label)])

    def callback_dropdown(self, dropdown, _fn: callable):
        dropdown.change(_fn, inputs=[dropdown, self.gr.State(dropdown.label)])

    def ptz(self, _fn):
        with self.gr.Row():
            with self.gr.Column():
                self.gr.Image()

            with self.gr.Column():
                self.gr.Markdown("Move PTZ")
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("TEST"), _fn)
                    self.callback_btn(self.gr.Button("DOWN"), _fn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("LEFT"), _fn)
                    self.callback_btn(self.gr.Button("RIGHT"), _fn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("NIGHT"), _fn)
                    self.callback_btn(self.gr.Button("DAY"), _fn)
                    self.callback_btn(self.gr.Button("HOME"), _fn)
                    self.callback_btn(self.gr.Button("SNAPSHOT"), _fn)
                    self.callback_btn(self.gr.Button("STOP"), _fn)

    def parameters(self, _fn_btn, _fn_slider, _type="analog"):
        with self.gr.Row():
            with self.gr.Column():
                if _type == "digital":
                    with self.gr.Row():
                        self.callback_slider(self.gr.Slider(label="ROI X"), _fn_slider)
                        self.callback_slider(self.gr.Slider(label="ROI Y"), _fn_slider)
                    with self.gr.Row():
                        self.callback_slider(self.gr.Slider(label="ROI W"), _fn_slider)
                        self.callback_slider(self.gr.Slider(label="ROI H"), _fn_slider)
                with self.gr.Row():
                    self.callback_slider(self.gr.Slider(label="THRESHOLD"), _fn_slider)
                with self.gr.Row():
                    self.callback_slider(self.gr.Slider(label="VAL MIN"), _fn_slider)
                    self.callback_slider(self.gr.Slider(label="VAL MAX"), _fn_slider)
                with self.gr.Row():
                    self.callback_slider(
                        self.gr.Slider(label="Skew Angle X"), _fn_slider
                    )
                    self.callback_slider(
                        self.gr.Slider(label="Skew Angle Y"), _fn_slider
                    )
            with self.gr.Column():
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("1"), _fn_btn)
                    self.callback_btn(self.gr.Button("2"), _fn_btn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("3"), _fn_btn)
                    self.callback_btn(self.gr.Button("4"), _fn_btn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("5"), _fn_btn)
                    self.callback_btn(self.gr.Button("6"), _fn_btn)

    def mission_robot(self, _fn_btn, _fn_textbox, _type="robot"):
        with self.gr.Row():
            self.callback_textbox(
                self.gr.Textbox(label="TASK", placeholder="m1"), _fn_textbox
            )
            self.callback_textbox(
                self.gr.Textbox(label="MAX", placeholder="20"), _fn_textbox
            )
            self.callback_textbox(
                self.gr.Textbox(label="UNIT", placeholder="bar"), _fn_textbox
            )
        if _type == "robot":
            with self.gr.Row():
                self.callback_textbox(
                    self.gr.Textbox(label="WAYPOINT", placeholder="wp_0"), _fn_textbox
                )
                self.callback_textbox(
                    self.gr.Textbox(label="POSE", placeholder="pose_0"), _fn_textbox
                )
            with self.gr.Row():
                self.callback_btn(self.gr.Button("SAVE WP"), _fn_btn)
                self.callback_btn(self.gr.Button("SAVE POSE"), _fn_btn)
            with self.gr.Row():
                self.callback_btn(self.gr.Button("REC"), _fn_btn)
                self.callback_btn(self.gr.Button("CONFIG TASK"), _fn_btn)
                self.callback_btn(self.gr.Button("STOP REC"), _fn_btn)
        else:
            with self.gr.Row():
                self.callback_btn(self.gr.Button("REC MISSION"), _fn_btn)
                self.callback_btn(self.gr.Button("STOP MISSION"), _fn_btn)
                self.callback_btn(self.gr.Button("PLAY MISSION"), _fn_btn)

    def control_spot(self, _fn):
        self.callback_btn(self.gr.Button("UPDATE STATUS"), _fn)
        self.callback_btn(self.gr.Button("LOAD MISSIONS"), _fn)
        with self.gr.Row():
            with self.gr.Column():
                with self.gr.Row():
                    self.gr.Dropdown(
                        ["m1", "m2", "m3"], label="Mission list", info="Select mission"
                    )
                    self.callback_btn(self.gr.Button("SET MISSION"), _fn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("PLAY"), _fn)
                    self.callback_btn(self.gr.Button("PAUSE"), _fn)
                    self.callback_btn(self.gr.Button("RESUME"), _fn)
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("STOP"), _fn)
                    self.callback_btn(self.gr.Button("LOCALIZE"), _fn)
            with self.gr.Column():
                with self.gr.Row():
                    with self.gr.Tab("Fiducial"):
                        self.gr.Dropdown(["202", "201", "203"], label="")
                    with self.gr.Tab("Waypoint"):
                        self.gr.Dropdown(["wp_0", "wp_2", "wp_3"], label="")
                with self.gr.Row():
                    self.gr.Checkbox(label="enable task")
                with self.gr.Row():
                    self.callback_btn(self.gr.Button("GO TO"), _fn)

    def docs_template(self, _fn_textbox, _fn):
        self.callback_textbox(
            self.gr.Textbox(
                label="URL ssh repo",
                placeholder="git@gitlab.alisys.net:robotica/tar/resources/rabbitmq_control.git",
            ),
            _fn_textbox,
        )
        self.callback_textbox(
            self.gr.Textbox(label="Branch", placeholder="develop,main,v1.0.0"),
            _fn_textbox,
        )

        with self.gr.Row():
            self.callback_btn(self.gr.Button("UPLOAD"), _fn)
            self.callback_btn(self.gr.Button("REMOVE"), _fn)

        self.callback_btn(self.gr.Button("GO to DOCS"), _fn)

    def deployment(self, list_repo, list_branch, _fn_btn, _fn_inter):

        self.gr.Interface(
            _fn_inter,
            inputs=[
                self.gr.Dropdown(list_repo, label="REPO", info="Select REPO"),
                self.gr.Textbox(label="Branch", placeholder="v1.0.0"),
            ],
            outputs=self.gr.Dataframe(
                headers=["REPO", "RAMA"],
                datatype=["str", "str"],
                row_count=1,
                col_count=(2, "fixed"),
            ),
            allow_flagging="never",
        )

        self.callback_btn(self.gr.Button("BUILD"), _fn_btn)

    def reload(self):
        logging.info("UPDATE")
        return self.gr.update()
