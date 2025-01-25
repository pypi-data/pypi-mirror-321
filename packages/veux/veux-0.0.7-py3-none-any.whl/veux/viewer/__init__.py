# Claudio Perez
# Summer 2024
import base64
import textwrap
from pathlib import Path

class Viewer:
    def __init__(self, viewer=None, path=None, data=None):
        if data is not None:
            data64 = base64.b64encode(data).decode('utf-8')
            self._glbsrc=f"data:model/gltf-binary;base64,{data64}"
        else:
            self._glbsrc = path 

        self._viewer = viewer if viewer is not None else "mv"

    def get_html(self):
        if self._viewer == "babylon":
            with open(Path(__file__).parents[0]/"babylon.html", "r") as f:
                return f.read()

        if self._viewer == "three-170":
            with open(Path(__file__).parents[0]/"three-170.html", "r") as f:
                return f.read()

        if self._viewer == "three-160":
            with open(Path(__file__).parents[0]/"gltf.html", "r") as f:
                return f.read()

        elif self._viewer == "three-130":
            with open(Path(__file__).parents[0]/"index.html", "r") as f:
                return f.read()

        elif self._viewer == "mv":
            return _model_viewer(self._glbsrc, control=False)
            html = textwrap.dedent("""
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>veux</title>
            <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js"></script>
            """ + """
            <style>
              .controls {
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 10px;
              }

              .controls button {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
              }

              .controls button:hover {
                background-color: #45a049;
              }

              .controls button:disabled {
                background-color: #cccccc;
                cursor: not-allowed;
              }
            </style>
          </head>
          <body>
          """ + f"""
            <model-viewer id="veux-viewer"
                          alt="rendering"
                          src="{self._glbsrc}"
                          autoplay
                          style="width: 100%; height: 500px;"
                          max-pixel-ratio="2"
                          shadow-intensity="1"
                          environment-image="/black_ground.hdr"
                          environment-image="neutral"
                          shadow-light="10000 10000 10000"
                          exposure="0.8"
                          camera-controls
                          min-camera-orbit="auto auto 0m"
                          touch-action="pan-y">
            </model-viewer>
        <!--
                          bounds="0 0 0 10000 10000 10000"
                          ar
                          environment-image="https://modelviewer.dev/shared-assets/environments/spruit_sunrise_1k_LDR.jpg"
                          shadow-softness="0.8"
                          ar-modes="scene-viewer; quick-look"
                          position="0 0 -50"
                          scale="0.01 0.01 0.01"
        -->
            """ + """

              <div class="controls">
                <button id="step-backward">Step Left</button>
                <button id="toggle-animation">Pause</button>
                <button id="step-forward">Step Right</button>
              </div>

            <script>
              const modelViewer = document.getElementById('veux-viewer');
              const toggleButton = document.getElementById('toggle-animation');
              const stepBackwardButton = document.getElementById('step-backward');
              const stepForwardButton = document.getElementById('step-forward');

              toggleButton.addEventListener('click', () => {
                if (modelViewer.paused) {
                  modelViewer.play();
                  toggleButton.textContent = 'Pause';
                } else {
                  modelViewer.pause();
                  toggleButton.textContent = 'Play';
                }
              });

              stepBackwardButton.addEventListener('click', () => {
                if (modelViewer.currentTime > 0) {
                  modelViewer.currentTime -= 0.1; // Step backward by 0.1 seconds
                }
              });

              stepForwardButton.addEventListener('click', () => {
                if (modelViewer.currentTime < modelViewer.totalTime) {
                  modelViewer.currentTime += 0.1; // Step forward by 0.1 seconds
                }
              });

              // Disable step buttons when out of range
              modelViewer.addEventListener('timeupdate', () => {
                stepBackwardButton.disabled = modelViewer.currentTime <= 0;
                stepForwardButton.disabled = modelViewer.currentTime >= modelViewer.totalTime;
              });
            </script>
          </body>
          </html>
        """)
        return html

def _model_viewer(source, control=False):
      library = '<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js"></script>'

      with open(Path(__file__).parents[0]/"controls.css", "r") as f:
          control_style = f"<style>{f.read()}</style>"

      with open(Path(__file__).parents[0]/"controls.js", "r") as f:
          control_code = f"<script>{f.read()}</script>"

      control_html = """
        <div class="controls">
          <!-- <button id="step-backward">Step Left</button> -->
          <button id="toggle-animation">Pause</button>
          <!-- <button id="step-forward">Step Right</button> -->
        </div>
      """


      foot = "</body></html>"
      head = f"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>veux</title>
          {library}
          {control_style}
        </head>
        <body>
      """

      viewer = f"""
          <model-viewer id="veux-viewer"
                        alt="rendering"
                        src="{source}"
                        autoplay
                        style="width: 100%; height: 500px;"
                        max-pixel-ratio="2"
                        shadow-intensity="1"
                        environment-image="/black_ground.hdr"
                        environment-image="neutral"
                        shadow-light="10000 10000 10000"
                        exposure="0.8"
                        camera-controls
                        min-camera-orbit="auto auto 0m"
                        touch-action="pan-y">
          </model-viewer>
      """
      return textwrap.dedent(f"""
            {head}
            {viewer}
            {control_html if control else ""}
            {control_code if control else ""}
            {foot}
      """)
