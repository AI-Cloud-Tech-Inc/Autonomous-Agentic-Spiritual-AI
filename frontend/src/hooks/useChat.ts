import { useCallback } from "react";
import { useChatStore } from "../store/chatStore";
import { sendMessage } from "../services/chatService";
import { Message } from "../types/chat";

export function useChat(sessionId: string) {
  const { messages, isLoading, addMessage, setLoading } = useChatStore();

  const send = useCallback(
    async (text: string) => {
      const userMessage: Message = {
        id: crypto.randomUUID(),
        role: "user",
        content: text,
        timestamp: new Date().toISOString(),
      };
      addMessage(userMessage);
      setLoading(true);

      try {
        const response = await sendMessage(sessionId, text);
        const assistantMessage: Message = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: response.message,
          timestamp: new Date().toISOString(),
          emotionDetected: response.emotion_detected,
        };
        addMessage(assistantMessage);
      } finally {
        setLoading(false);
      }
    },
    [sessionId, addMessage, setLoading]
  );

  return { messages, isLoading, send };
}
