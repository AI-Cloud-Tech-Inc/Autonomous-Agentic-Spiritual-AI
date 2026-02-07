import { useParams } from "react-router-dom";
import ChatWindow from "../components/chat/ChatWindow";

function ChatPage() {
  const { sessionId } = useParams<{ sessionId: string }>();

  return (
    <main style={{ maxWidth: 720, margin: "0 auto", height: "100vh", display: "flex", flexDirection: "column" }}>
      <ChatWindow sessionId={sessionId} />
    </main>
  );
}

export default ChatPage;
