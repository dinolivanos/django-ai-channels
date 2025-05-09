import {
  ImageClassifier,
  FilesetResolver,
} from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.2";

let model = null;

function createWebSocket(url) {
  const webSocket = new WebSocket(url);
  webSocket.onmessage = function (e) {};

  webSocket.onclose = function (e) {
    console.error("Socket closed unexpectedly");
  };

  return webSocket;
}

function createWebSocketSender(url) {
  let webSocket = createWebSocket(url);

  function sender(classification) {
    if (
      classification.length > 0 &&
      classification[0]["categories"].length != 0
    ) {
      // send data over socket
      webSocket.send(
        JSON.stringify({
          classification: classification,
        }),
      );
    }
  }

  return sender;
}

export function createClassifyCallback(model, videoId, url) {
  const video = document.getElementById(videoId);
  const wsSend = createWebSocketSender(url);
  async function classifyVideoFrame() {
    if (model === null) {
      // model is not ready, nothing we can do
      return;
    }

    const result = model.classifyForVideo(video, performance.now());
    wsSend(result.classifications);

    // Call this function again to keep predicting when the browser is ready.
    window.requestAnimationFrame(classifyVideoFrame);
  }

  return classifyVideoFrame;
}

export async function activateVideoStream(videoId, callback) {
  if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia)) {
    console.error("getUserMedia() is not supported by your browser");
    return;
  }

  const video = document.getElementById(videoId);
  // getUsermedia parameters.
  const constraints = {
    video: true,
  };
  // Activate the webcam stream.
  navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
    video.srcObject = stream;
    video.addEventListener("loadeddata", callback);
  });
}

export async function initializeModel(
  modelUrl,
  runningMode,
  modelReadyCallback,
  maxResults,
  scoreThreshold,
) {
  const fileSet = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.2/wasm",
  );

  model = await ImageClassifier.createFromOptions(fileSet, {
    baseOptions: {
      modelAssetPath: modelUrl,
    },
    maxResults: maxResults,
    runningMode: runningMode,
    scoreThreshold: scoreThreshold,
  });

  if (modelReadyCallback !== undefined) {
    modelReadyCallback();
  }

  return model;
}
