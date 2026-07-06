============================================================
Local LLM Demo — Mode C (blocking)
API: stream=False  |  UI: print once
============================================================

⚙️  Initializing agent...
2026-07-06 15:51:57,878 - httpx - INFO - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2026-07-06 15:51:57,879 - __main__ - INFO - Using Ollama model: qwen3:0.6b
2026-07-06 15:51:57,892 - httpx - INFO - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2026-07-06 15:51:57,892 - ollama_native - INFO - Connected to Ollama with model: qwen3:0.6b
✅ Agent ready!

============================================================
TASK EXECUTION
============================================================

📋 Task: What's the current time and weather like in Vancouver right now?
------------------------------------------------------------

⏳ Processing (waiting for full API response)...

2026-07-06 15:51:57,892 - ollama_native - INFO - Task: What's the current time and weather like in Vancouver right now?
2026-07-06 15:51:57,892 - ollama_native - INFO - Mode C: Ollama API stream=False, blocking response
2026-07-06 15:51:57,892 - ollama_native - INFO - DEBUG_RESPONSE=1: printing full response breakdown
2026-07-06 15:51:57,892 - ollama_native - INFO - Iteration 1/10
2026-07-06 15:52:02,468 - httpx - INFO - HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"

[response] iteration=1
{
  "model": "qwen3:0.6b",
  "created_at": "2026-07-06T07:52:02.4679336Z",
  "done": true,
  "done_reason": "stop",
  "total_duration": 4573258700,
  "load_duration": 111274600,
  "prompt_eval_count": 495,
  "prompt_eval_duration": 23347300,
  "eval_count": 183,
  "eval_duration": 4369298200,
  "message": {
    "role": "assistant",
    "content": "",
    "thinking": "Okay, the user is asking for the current time and weather in Vancouver. Let me check the tools available. There's get_current_time and get_current_temperature. The get_current_time function requires the location and optionally the timezone. The user specified Vancouver, so I should use that. The get_current_temperature function needs the location. Since the user didn't mention the unit, I'll default to Celsius. So, I need to call both functions. Wait, but the user's question is two separate things: time and weather. So first, get the time with the location, then get the weather with the location. Let me structure each tool call properly.\n",
    "images": null,
    "tool_name": null,
    "tool_calls": [
      {
        "function": {
          "name": "get_current_time",
          "arguments": {
            "location": "Vancouver, Canada"
          }
        }
      },
      {
        "function": {
          "name": "get_current_temperature",
          "arguments": {
            "location": "Vancouver, Canada"
          }
        }
      }
    ]
  }
}

2026-07-06 15:52:02,470 - ollama_native - INFO - Model requested 2 tool call(s)
2026-07-06 15:52:02,471 - ollama_native - INFO - Executing tool: get_current_time with args: {'location': 'Vancouver, Canada'}
2026-07-06 15:52:04,315 - ollama_native - INFO - Executing tool: get_current_temperature with args: {'location': 'Vancouver, Canada'}
2026-07-06 15:52:08,078 - ollama_native - INFO - Iteration 2/10
2026-07-06 15:52:18,790 - httpx - INFO - HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"

[response] iteration=2
{
  "model": "qwen3:0.6b",
  "created_at": "2026-07-06T07:52:18.7886606Z",
  "done": true,
  "done_reason": "stop",
  "total_duration": 10707673600,
  "load_duration": 114907700,
  "prompt_eval_count": 801,
  "prompt_eval_duration": 2048997800,
  "eval_count": 291,
  "eval_duration": 8435667500,
  "message": {
    "role": "assistant",
    "content": "The current time in Vancouver, Canada is **00:52:04** (Monday, July 6, 2026). The weather is **clear sky** with a temperature of **15.8°C**. Humidity is 74%, and there's a wind speed of 6.3 km/h. The coordinates are **49.25°N, -123.12°E** for reference.",
    "thinking": "Okay, let's see. The user asked for the current time and weather in Vancouver right now. I used the get_current_time function with the location set to Vancouver, Canada. The response came back with the time as 00:52:04 on a Monday, July 6th, 2026. Then I called get_current_temperature for Vancouver, Canada. The temperature was 15.8°C, clear sky, humidity 74%, wind speed 6.3 km/h.\n\nNow I need to present this information in a clear way. Make sure to mention the time, the temperature, the conditions, and the humidity and wind details. Also, include the coordinates if that's helpful, but maybe it's better to just state that it's from Open-Meteo. Check for any typos and ensure the units are correct. Alright, putting it all together in a friendly, concise response.\n",
    "images": null,
    "tool_name": null,
    "tool_calls": null
  }
}

🔧 Tool Calls:
  → get_current_time: {'location': 'Vancouver, Canada'}
    ✓ {"timezone": "America/Vancouver", "datetime": "2026-07-06 00:52:04", "date": "2026-07-06", "time": "00:52:04", "day_of_week": "Monday", "utc_offset": "-0700", "timestamp": "2026-07-06T00:52:04.315338-07:00", "location": "Vancouver, Canada"}
  → get_current_temperature: {'location': 'Vancouver, Canada'}
    ✓ {"location": "Vancouver, Canada", "temperature": 15.8, "unit": "\u00b0C", "conditions": "clear sky", "humidity": 74, "wind_speed": 6.3, "wind_unit": "km/h", "coordinates": {"latitude": 49.24966, "longitude": -123.11934}, "timestamp": "2026-07-06T00:45", "source": "Open-Meteo"}

🤖 Assistant:
----------------------------------------
The current time in Vancouver, Canada is **00:52:04** (Monday, July 6, 2026). The weather is **clear sky** with a temperature of **15.8°C**. Humidity is 74%, and there's a wind speed of 6.3 km/h. The coordinates are **49.25°N, -123.12°E** for reference.
----------------------------------------

Iterations: 2