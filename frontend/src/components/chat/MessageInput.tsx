import { useState, FormEvent } from "react";

interface MessageInputProps {
  onSend: (text: string) => void;
}

function MessageInput({ onSend }: MessageInputProps) {
  const [text, setText] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const trimmed = text.trim();
    if (!trimmed) return;
    onSend(trimmed);
    setText("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", gap: 8, padding: 16, borderTop: "1px solid var(--color-border)" }}>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Share what's on your mind..."
        style={{
          flex: 1,
          padding: "12px 16px",
          border: "1px solid var(--color-border)",
          borderRadius: 8,
          fontSize: "1rem",
          outline: "none",
        }}
      />
      <button
        type="submit"
        style={{
          padding: "12px 24px",
          backgroundColor: "var(--color-primary)",
          color: "#fff",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
          fontSize: "1rem",
        }}
      >
        Send
      </button>
    </form>
  );
}

export default MessageInput;
