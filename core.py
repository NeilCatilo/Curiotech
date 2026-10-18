"""UI-independent learning, navigation, and local persistence."""

import json
import os
from copy import deepcopy
from pathlib import Path
from random import Random

VERSION = "1.2.0"
DEFAULT_STATE = {
    "schema_version": 1,
    "settings": {"dark": False, "large_text": False, "sound": False, "reduced_motion": False, "language": "en"},
    "progress": {"completed": 0, "best_score": 0, "last_score": 0, "last_total": 0},
}


class LocalStore:
    """Validate on read; atomically replace state so an interrupted save is safe."""

    def __init__(self, path):
        self.path = Path(path)
        self.data = deepcopy(DEFAULT_STATE)
        self.last_error = None
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                for key in self.data["settings"]:
                    value = raw.get("settings", {}).get(key)
                    if key == "language" and value in ("en", "tl"):
                        self.data["settings"][key] = value
                    elif key != "language" and type(value) is bool:
                        self.data["settings"][key] = value
                for key in self.data["progress"]:
                    value = raw.get("progress", {}).get(key)
                    if type(value) is int and value >= 0:
                        self.data["progress"][key] = value
                self.data["progress"]["best_score"] = min(100, self.data["progress"]["best_score"])
        except FileNotFoundError:
            pass
        except (OSError, ValueError, TypeError, AttributeError) as exc:
            self.last_error = str(exc)

    def save(self):
        temporary = self.path.with_suffix(".tmp")
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with temporary.open("w", encoding="utf-8") as handle:
                json.dump(self.data, handle, indent=2)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
            self.last_error = None
            return True
        except OSError as exc:
            self.last_error = str(exc)
            return False

    def record_quiz(self, score, total):
        if total <= 0 or not 0 <= score <= total:
            raise ValueError("Invalid quiz score")
        progress = self.data["progress"]
        progress["completed"] += 1
        progress["last_score"], progress["last_total"] = score, total
        progress["best_score"] = max(progress["best_score"], round(score / total * 100))
        return self.save()


class NavigationHistory:
    def __init__(self, home="main"):
        self.home = home
        self.current = home
        self.stack = []

    def go(self, destination, section=False):
        if section or destination == self.home:
            self.stack.clear()
        elif destination != self.current:
            self.stack.append(self.current)
        self.current = destination
        return destination

    def back(self):
        self.current = self.stack.pop() if self.stack else self.home
        return self.current


class QuizSession:
    """One submission per question; explicit advancement leaves time to learn."""

    def __init__(self, questions, seed=None):
        if not questions:
            raise ValueError("A quiz needs at least one question")
        self.questions = deepcopy(list(questions))
        random = Random(seed)
        random.shuffle(self.questions)
        for question in self.questions:
            answer = question["choices"][question["answer"]]
            random.shuffle(question["choices"])
            question["answer"] = question["choices"].index(answer)
        self.index = 0
        self.score = 0
        self.selected = None
        self.recorded = False

    @property
    def complete(self):
        return self.index >= len(self.questions)

    @property
    def question(self):
        return None if self.complete else self.questions[self.index]

    def submit(self, choice):
        if self.complete or self.selected is not None:
            return None
        if type(choice) is not int or not 0 <= choice < len(self.question["choices"]):
            raise ValueError("Invalid answer choice")
        self.selected = choice
        correct = choice == self.question["answer"]
        self.score += int(correct)
        return correct

    def advance(self):
        if self.complete or self.selected is None:
            return False
        self.index += 1
        self.selected = None
        return True


def search_terms(entries, query="", category="All"):
    needle = query.strip().casefold()
    return [entry for entry in entries
            if (category == "All" or entry["category"] == category)
            and (not needle or needle in (entry["term"] + " " + entry["meaning"] + " " + entry.get("search_text", "")).casefold())]
