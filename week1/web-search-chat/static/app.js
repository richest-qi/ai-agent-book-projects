const SESSION_KEY = "web_search_chat_session_id";

const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const clearBtn = document.getElementById("clear-btn");

let sessionId = localStorage.getItem(SESSION_KEY);
let isSending = false;

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function createMessage(role, text, extraClass = "") {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${role} ${extraClass}`.trim();

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = role === "user" ? "你" : "K";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;

  wrapper.appendChild(avatar);
  wrapper.appendChild(bubble);
  messagesEl.appendChild(wrapper);
  scrollToBottom();

  return wrapper;
}

function setLoading(loading) {
  isSending = loading;
  sendBtn.disabled = loading;
  userInput.disabled = loading;
}

async function sendMessage(text) {
  const trimmed = text.trim();
  if (!trimmed || isSending) return;

  createMessage("user", trimmed);
  userInput.value = "";
  userInput.style.height = "auto";

  const loadingEl = createMessage("assistant", "正在搜索和思考…", "loading");
  setLoading(true);

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: sessionId,
        message: trimmed,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      const detail = data.detail || "请求失败";
      throw new Error(typeof detail === "string" ? detail : JSON.stringify(detail));
    }

    sessionId = data.session_id;
    localStorage.setItem(SESSION_KEY, sessionId);
    loadingEl.querySelector(".bubble").textContent = data.answer;
    loadingEl.classList.remove("loading");
  } catch (error) {
    loadingEl.querySelector(".bubble").textContent = `出错了：${error.message}`;
    loadingEl.classList.remove("loading");
  } finally {
    setLoading(false);
    scrollToBottom();
    userInput.focus();
  }
}

async function resetChat() {
  if (sessionId) {
    try {
      await fetch("/api/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId }),
      });
    } catch {
      // ignore reset errors; local UI still clears
    }
  }

  sessionId = null;
  localStorage.removeItem(SESSION_KEY);
  messagesEl.innerHTML = "";

  createMessage(
    "assistant",
    "你好，我是联网搜索助手。输入问题后我会搜索网络并回答，支持多轮追问。"
  );
  userInput.focus();
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage(userInput.value);
});

userInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendMessage(userInput.value);
  }
});

userInput.addEventListener("input", () => {
  userInput.style.height = "auto";
  userInput.style.height = `${Math.min(userInput.scrollHeight, 160)}px`;
});

clearBtn.addEventListener("click", resetChat);

userInput.focus();
