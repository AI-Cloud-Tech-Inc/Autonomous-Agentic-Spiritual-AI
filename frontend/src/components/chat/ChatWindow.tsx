import { useState } from "react";
import MessageList from "./MessageList";
import MessageInput from "./MessageInput";
import { Message } from "../../types/chat";

interface ChatWindowProps {
  sessionId?: string;
}

function ChatWindow({ sessionId: _sessionId }: ChatWindowProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content: "Welcome. I'm here to listen and reflect with you. What's on your mind?",
      timestamp: new Date().toISOString(),
    },
  ]);

  const handleSend = (text: string) => {
    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
      timestamp: new Date().toISOString(),
    };
    setMessages((prev) => [...prev, userMessage]);

    // TODO: Call backend API and append assistant response
  };

  return (
    <>
      <MessageList messages={messages} />
      <MessageInput onSend={handleSend} />
    </>
  );
}

export default ChatWindow;
