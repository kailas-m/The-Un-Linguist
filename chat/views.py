from django.shortcuts import render
from .utils import generate_response, jumble_translate, additive_shift_cipher, cipher_clue

def index(request):
    base = output = cipher_text = clue = ""
    mode = action = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        mode = request.POST.get("mode", "")
        action = request.POST.get("action", "")

        if not mode:
            # First step: ask for mode
            return render(request, "chat/index.html", {
                "step": "choose_mode",
                "user_input": user_input,
            })

        base = generate_response(user_input)

        if mode == "easy":
            output = jumble_translate(base)
            if action == "give_up":
                return render(request, "chat/index.html", {
                    "step": "give_up",
                    "user_input": user_input,
                    "base": base,
                    "mode": mode,
                })
            return render(request, "chat/index.html", {
                "step": "easy",
                "user_input": user_input,
                "output": output,
                "mode": mode,
            })

        elif mode == "hard":
            cipher_text, shifts = additive_shift_cipher(base)
            if action == "need_help":
                clue = cipher_clue(shifts)
                return render(request, "chat/index.html", {
                    "step": "hard_help",
                    "user_input": user_input,
                    "cipher": cipher_text,
                    "clue": clue,
                    "mode": mode,
                })
            elif action == "give_up":
                return render(request, "chat/index.html", {
                    "step": "give_up",
                    "user_input": user_input,
                    "base": base,
                    "mode": mode,
                })
            return render(request, "chat/index.html", {
                "step": "hard",
                "user_input": user_input,
                "cipher": cipher_text,
                "mode": mode,
            })

    # Initial page load
    return render(request, "chat/index.html", {})
