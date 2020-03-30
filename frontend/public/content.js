chrome.runtime.onConnect.addListener(port => {
  port.onMessage.addListener(msg => {
    if (msg.cmd == "select") {
      port.postMessage({ selection: window.getSelection().toString() })
    } else {
      port.postMessage({ result: "error", message: "Invalid" });
    }
  }
)});
