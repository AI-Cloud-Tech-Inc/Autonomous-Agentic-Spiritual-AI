import api from "./api";

export async function sendMessage(sessionId: string, message: string) {
  const response = await api.post("/chat", { session_id: sessionId, message });
  return response.data;
}

export async function createSession(intention?: string) {
  const response = await api.post("/sessions", { intention });
  return response.data;
}

export async function getSession(sessionId: string) {
  const response = await api.get(`/sessions/${sessionId}`);
  return response.data;
}

export async function listSessions() {
  const response = await api.get("/sessions");
  return response.data;
}
