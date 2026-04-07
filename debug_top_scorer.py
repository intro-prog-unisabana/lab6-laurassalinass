def run():
    scores = {}
    while True:
        entry = input("Enter player and score as 'name score' (or type 'stop' to finish): ").strip()
        if entry.lower() == "stop":
            break
        name, score = entry.split()
        score = int(score)
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score

    if not scores:
        print("No scores recorded.")
    else:
        top_player = max(scores, key=scores.get)
        print(f"Top scorer: {top_player} with {scores[top_player]} points.")

if _name_ == "_main_":
    run()
