import { useState } from "react";

interface MeditationTimerProps {
  durationMinutes?: number;
}

function MeditationTimer({ durationMinutes = 5 }: MeditationTimerProps) {
  const [isRunning, setIsRunning] = useState(false);

  return (
    <div style={{ textAlign: "center", padding: 32 }}>
      <h2 style={{ fontFamily: "var(--font-display)", marginBottom: 16 }}>Mindful Pause</h2>
      <p style={{ color: "var(--color-text-muted)", marginBottom: 24 }}>
        {durationMinutes} minute meditation
      </p>
      <button
        onClick={() => setIsRunning(!isRunning)}
        style={{
          padding: "12px 32px",
          backgroundColor: "var(--color-primary)",
          color: "#fff",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
          fontSize: "1rem",
        }}
      >
        {isRunning ? "Pause" : "Begin"}
      </button>
      {/* TODO: Implement countdown timer and completion state */}
    </div>
  );
}

export default MeditationTimer;
