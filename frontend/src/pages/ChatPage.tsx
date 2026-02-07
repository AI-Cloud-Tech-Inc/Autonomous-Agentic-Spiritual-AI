import { useState } from 'react'
import { Link } from 'react-router-dom'

function ChatPage() {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([
    { role: 'assistant', content: 'Hello. I am here to listen and reflect with you. How are you feeling today?' }
  ])

  const sendMessage = () => {
    if (!message.trim()) return
    setMessages([...messages, { role: 'user', content: message }])
    setMessage('')
    // TODO: Call API
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', maxWidth: '800px', margin: '0 auto' }}>
      <header style={{ padding: '16px 24px', background: '#5c6bc0', color: 'white', display: 'flex', alignItems: 'center', gap: '16px' }}>
        <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>← Back</Link>
        <h1 style={{ fontSize: '18px' }}>Spiritual Guidance</h1>
      </header>

      <div style={{ flex: 1, overflow: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {messages.map((msg, i) => (
          <div key={i} style={{
            padding: '12px 16px',
            borderRadius: '12px',
            maxWidth: '80%',
            alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start',
            background: msg.role === 'user' ? '#5c6bc0' : '#fff',
            color: msg.role === 'user' ? 'white' : '#212121',
            boxShadow: '0 1px 3px rgba(0,0,0,0.1)'
          }}>
            {msg.content}
          </div>
        ))}
      </div>

      <div style={{ padding: '24px', display: 'flex', gap: '12px' }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Share your thoughts..."
        />
        <button className="primary" onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}

export default ChatPage
