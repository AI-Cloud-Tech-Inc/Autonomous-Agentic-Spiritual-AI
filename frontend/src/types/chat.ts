export interface Message {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
  timestamp: string;
  emotionDetected?: string;
}

export interface ChatSession {
  id: string;
  title?: string;
  intention?: string;
  status: "active" | "completed";
  createdAt: string;
  messages: Message[];
}
