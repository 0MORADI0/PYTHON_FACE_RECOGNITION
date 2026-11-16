import subprocess, threading, time, winsound

_lock = threading.Lock()
_busy = False
_last_unknown = 0.0
UNKNOWN_COOLDOWN = 15

def _speak(text):
    text = text.replace("'", "''")
    ps = ("Add-Type -AssemblyName System.Speech; "
          "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
          f"$s.Speak('{text}')")
    subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                   creationflags=0x08000000)

def _run(text, beep):
    global _busy
    try:
        _speak(text)
        if beep:
            winsound.Beep(1000, 5000)
    finally:
        with _lock:
            _busy = False

def _start(text, beep=False):
    global _busy
    with _lock:
        if _busy:
            return False
        _busy = True
    threading.Thread(target=_run, args=(text, beep), daemon=True).start()
    return True

def announce_known(name):
    return _start(f"Face {name} identified;RATE THIS PROJECT")

def announce_unknown():
    global _last_unknown
    if time.time() - _last_unknown < UNKNOWN_COOLDOWN:
        return False
    if _start("Face not identified ; RATE THIS PROJECT", beep=True):
        _last_unknown = time.time()
        return True
    return False