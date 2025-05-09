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

  function sender(predictions) {
    if (predictions.length != 0) {
      // send data over socket
      webSocket.send(
        JSON.stringify({
          classification: predictions,
        }),
      );
    }
  }

  return sender;
}

// Code used by all models

// aichannels model base class
// all models should implement a load and detect method
class AiChannelsModel {
  config(loadConfig, detectConfig) {
    this.loadConfig = loadConfig;
    this.detectConfig = detectConfig;
  }

  async load() {
    throw new Error("Method 'load()' must be implemented.");
  }

  async detect(data) {
    throw new Error("Method 'detect()' must be implemented.");
  }
}

function createDetectCallback(model, videoId, callbacks) {
  const video = document.getElementById(videoId);

  async function detectCallback() {
    let predictions = await model.detect(video);

    for (const callback of callbacks) {
      callback(predictions);
    }

    // Call this function again to keep predicting when the browser is ready.
    window.requestAnimationFrame(detectCallback);
  }

  return detectCallback;
}

function activateVideoStream(videoId, userMediaConstraints, callback) {
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

// COCO-SSD model wrappers

export function cocoGetDefaultConfig() {
  let config = {
    videoId: undefined,
    websocketPath: undefined,
    modelLoadedCallback: undefined,
    detectCallbacks: [],
    modelConfig: {},
    detectConfig: { maxNumBoxes: 20, minScore: 0.5 },
    userMediaConstraints: {
      video: true,
    },
  };

  return config;
}

class AiCoco extends AiChannelsModel {
  async load() {
    this.model = await cocoSsd.load(this.loadConfig);
  }

  async detect(data) {
    let predictions = await this.model.detect(
      data,
      this.detectConfig.maxNumBoxes,
      this.detectConfig.minScore,
    );
    return predictions;
  }
}

export async function cocoSetup(config) {
  const wsUrl = `ws://${config.host}/${config.websocketPath}`;
  let websocketSender = createWebSocketSender(wsUrl);
  config.detectCallbacks.push(websocketSender);

  let cocomodel = new AiCoco();

  cocomodel.config(config.modelConfig, config.detectConfig);
  await cocomodel.load();
  if (typeof config.modelLoadedCallback !== "undefined") {
    // If user gave us a mode loaded callback call it
    config.modelLoadedCallback();
  }

  let detectCallBack = createDetectCallback(
    cocomodel,
    config.videoId,
    config.detectCallbacks,
  );
  activateVideoStream(
    config.videoId,
    config.userMedidaConstraints,
    detectCallBack,
  );
}
