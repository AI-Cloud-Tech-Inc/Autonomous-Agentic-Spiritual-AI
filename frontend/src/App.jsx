import { useState, useRef, useEffect } from 'react'

const API_BASE = '/api'

function App() {
  const [messages, setMessages] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isTyping, setIsTyping] = useState(false)
  const messagesEndRef = useRef(null)

  const quickActions = [
    'Guide me in meditation',
    'I need emotional support',
    'Share wisdom with me',
    'I feel grateful today'
  ]

  const initialGreeting = {
    role: 'agent',
    content: `🌟 Welcome, dear seeker! 🌟

I am your compassionate companion on the journey within — here to support your spiritual growth, offer gentle guidance, and walk alongside you in mindful exploration.

Take a deep breath... and share whatever is on your heart. I'm here to listen without judgment. 🙏`
  }

  useEffect(() => {
    setMessages([initialGreeting])
  }, [])

  useEffect(() => {
    scrollToBottom()
  }, [messages, isTyping])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const formatMessage = (content) => {
    return content.split('\n').map((line, i) => (
      <p key={i}>{line}</p>
    ))
  }

  const handleSend = async (message = inputValue) => {
    if (!message.trim() || isLoading) return

    const userMessage = { role: 'user', content: message.trim() }
    setMessages(prev => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)
    setIsTyping(true)

    try {
      const response = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: message.trim(),
          context: {}
        })
      })

      if (!response.ok) {
        throw new Error('Network response was not ok')
      }

      const data = await response.json()
      
      const agentMessage = { 
        role: 'agent', 
        content: data.response,
        context: data.context
      }
      
      setMessages(prev => [...prev, agentMessage])
    } catch (error) {
      console.error('Error:', error)
      const errorMessage = {
        role: 'agent',
        content: 'I apologize, but I encountered a connection issue. Please try again, or take a moment to breathe deeply and know that I\'m here when you\'re ready.',
        isError: true
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
      setIsTyping(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>🌸 Spiritual AI Companion</h1>
        <p>Your mindful journey begins here</p>
      </header>

      <div className="chat-container">
        <div className="messages-area">
          {messages.length === 0 ? (
            <div className="greeting-message">
              <h2>Take a moment to center yourself</h2>
              <p>Your compassionate companion is here to listen</p>
            </div>
          ) : (
            messages.map((msg, index) => (
              <div key={index} className={`message ${msg.role}`}>
                <div className={`message-content ${msg.isError ? 'emergency' : ''}`}>
                  {formatMessage(msg.content)}
                </div>
              </div>
            ))
          )}
          
          {isTyping && (
            <div className="message agent">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>

        <div className="quick-actions">
          {quickActions.map((action, index) => (
            <button
              key={index}
              onClick={() => handleSend(action)}
              disabled={isLoading}
            >
              {action}
            </button>
          ))}
        </div>

        <div className="input-area">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Share what's on your heart..."
            disabled={isLoading}
          />
          <button onClick={() => handleSend()} disabled={isLoading || !inputValue.trim()}>
            {isLoading ? '...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
