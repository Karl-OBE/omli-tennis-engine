from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "O.M.L.I. Tennis Engine is live!"}

    @app.get("/predict")
    def predict(player_a: str = "Player A", player_b: str = "Player B"):
        """
            Simulates a basic tennis prediction output.
                This will later connect to real tennis data APIs.
                    """
                        confidence = round(random.uniform(0.85, 0.99), 2)
                            winner = player_a if confidence > 0.9 else player_b
                                return {
                                        "match": f"{player_a} vs {player_b}",
                                                "predicted_winner": winner,
                                                        "confidence": f"{confidence * 100:.1f}%",
                                                                "engine_status": "Stable"
                                                                    }