import { Message } from "../../types/chat";

interface MessageBubbleProps {
  message: Message;
}

function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: 12,
      }}
    >
      <div
        style={{
          maxWidth: "75%",
          padding: "12px 16px",
          borderRadius: 12,
          backgroundColor: isUser ? "var(--color-primary)" : "var(--color-surface)",
          color: isUser ? "#fff" : "var(--color-text)",
          border: isUser ? "none" : "1px solid var(--color-border)",
          lineHeight: 1.5,
        }}
      >
        {message.content}
      </div>
    </div>
  );
}

export default MessageBubble;
