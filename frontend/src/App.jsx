import { useState, useRef, useEffect } from 'react'
import BhaktiTab from './BhaktiTab'

const API_BASE = '/api'

function App() {
  const [messages, setMessages] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isTyping, setIsTyping] = useState(false)
  const [isRecording, setIsRecording] = useState(false)
  const [meditationTime, setMeditationTime] = useState(5)
  const [timerActive, setTimerActive] = useState(false)
  const [timerDisplay, setTimerDisplay] = useState('05:00')
  const [selectedTab, setSelectedTab] = useState('chat')
  
  const messagesEndRef = useRef(null)

  const quickActions = [
    'Guide me in meditation',
    'I need emotional support',
    'Share wisdom with me',
    'I feel grateful today'
  ]

  const initialGreeting = {
    role: 'agent',
    content: `Welcome, dear seeker!

I am your compassionate companion on the journey within - here to support your spiritual growth, offer gentle guidance, and walk alongside you in mindful exploration.

Take a deep breath... and share whatever is on your heart. I'm here to listen without judgment.`
  }

  useEffect(() => {
    setMessages([initialGreeting])
  }, [])

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isTyping])

  useEffect(() => {
    let interval = null
    if (timerActive && meditationTime > 0 && selectedTab === 'meditation') {
      interval = setInterval(() => {
        setMeditationTime(prev => {
          const newTime = prev - 1
          const minutes = Math.floor(newTime / 60)
          const seconds = newTime % 60
          setTimerDisplay(`${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`)
          return newTime
        })
      }, 1000)
    } else if (meditationTime === 0 && timerActive && selectedTab === 'meditation') {
      setTimerActive(false)
      setTimerDisplay('Namaste')
    }
    return () => clearInterval(interval)
  }, [timerActive, meditationTime, selectedTab])

  const formatMessage = (content) => {
    return content.split('\n').map((line, i) => <p key={i}>{line}</p>)
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
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message.trim(), context: {} })
      })

      if (!response.ok) throw new Error('Network response was not ok')

      const data = await response.json()
      const agentMessage = { role: 'agent', content: data.response }
      setMessages(prev => [...prev, agentMessage])
    } catch (error) {
      console.error('Error:', error)
      setMessages(prev => [...prev, {
        role: 'agent',
        content: 'I apologize, but I encountered a connection issue. Please try again.'
      }])
    } finally {
      setIsLoading(false)
      setIsTyping(false)
    }
  }

  const startVoiceInput = () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      alert('Speech recognition is not supported in your browser. Please try Chrome.')
      return
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    const recognition = new SpeechRecognition()
    
    recognition.continuous = false
    recognition.interimResults = false
    recognition.lang = 'en-US'

    recognition.onstart = () => setIsRecording(true)
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript
      setInputValue(prev => prev + transcript)
      handleSend(transcript)
    }
    recognition.onerror = () => setIsRecording(false)
    recognition.onend = () => setIsRecording(false)

    recognition.start()
  }

  const startMeditation = (minutes) => {
    setMeditationTime(minutes * 60)
    setTimerDisplay(`${minutes.toString().padStart(2, '0')}:00`)
    setTimerActive(true)
  }

  const stopMeditation = () => {
    setTimerActive(false)
    setMeditationTime(0)
    setTimerDisplay('05:00')
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>Spiritual AI Companion</h1>
        <p>Your mindful journey begins here</p>
      </header>

      <nav className="tab-nav">
        <button className={selectedTab === 'chat' ? 'active' : ''} onClick={() => setSelectedTab('chat')}>
          Chat
        </button>
        <button className={selectedTab === 'meditation' ? 'active' : ''} onClick={() => setSelectedTab('meditation')}>
          Meditate
        </button>
        <button className={selectedTab === 'spiritual' ? 'active' : ''} onClick={() => setSelectedTab('spiritual')}>
          Spiritual
        </button>
      </nav>

      {selectedTab === 'chat' ? (
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
                  <div className="message-content">{formatMessage(msg.content)}</div>
                </div>
              ))
            )}
            
            {isTyping && (
              <div className="message agent">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span><span></span><span></span>
                  </div>
                </div>
              </div>
            )}
            
            <div ref={messagesEndRef} />
          </div>

          <div className="quick-actions">
            {quickActions.map((action, index) => (
              <button key={index} onClick={() => handleSend(action)} disabled={isLoading}>
                {action}
              </button>
            ))}
          </div>

          <div className="input-area">
            <button className={`voice-btn ${isRecording ? 'recording' : ''}`} onClick={startVoiceInput}>
              Mic
            </button>
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSend()}
              placeholder="Share what's on your heart..."
              disabled={isLoading}
            />
            <button onClick={() => handleSend()} disabled={isLoading || !inputValue.trim()}>
              {isLoading ? '...' : 'Send'}
            </button>
          </div>
        </div>
      ) : selectedTab === 'spiritual' ? (
        <BhaktiTab />
      ) : (
        <div className="meditation-container">
          <div className="timer-section">
            <h2>Meditation Timer</h2>
            <div className="timer-display">{timerDisplay}</div>
            
            <div className="timer-presets">
              {[3, 5, 10, 15, 20].map(minutes => (
                <button key={minutes} onClick={() => startMeditation(minutes)} disabled={timerActive}>
                  {minutes} min
                </button>
              ))}
            </div>
            
            {timerActive && (
              <button className="stop-btn" onClick={stopMeditation}>End Session</button>
            )}
          </div>

          <div className="breathing-section">
            <h2>Breathing Exercise</h2>
            <div className="breathing-circle">
              <div className={`breath ${timerActive ? 'active' : ''}`}>
                {timerActive ? 'Breathe' : 'Ready'}
              </div>
            </div>
            <p className="breath-instructions">
              {timerActive ? 'Inhale... Exhale...' : 'Select a timer to begin'}
            </p>
          </div>

          <div className="audio-section">
            <h2>Sacred Sounds</h2>
            <div className="audio-display">
              <div className="om-symbol">AUM</div>
              <p className="track-name">Chakra Dhyana</p>
              <p className="sound-label">Sacred Healing Frequencies</p>
              <a 
                href="https://www.youtube.com/watch?v=2jbLyITT0Wo&autoplay=1" 
                target="_blank" 
                rel="noopener noreferrer"
                className="play-btn"
              >
                Click to Play Audio
              </a>
            </div>
          </div>

          <div className="meditation-tips">
            <h2>Today's Meditation</h2>
            <p>"The present moment is filled with joy and happiness."</p>
            <p className="author">- Thich Nhat Hanh</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
