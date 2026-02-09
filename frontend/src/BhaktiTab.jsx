import { useState, useEffect, useRef } from 'react'
import { TELUGU_BHAJANS, DAILY_MANTRAS, SPIRITUAL_ROUTINES } from './spiritual_content'

// Audio fallback for when files don't exist - uses TTS
const playTTS = (text, lang = 'sa-IN') => {
  if (!('speechSynthesis' in window)) {
    console.warn('Speech synthesis not supported')
    return false
  }
  window.speechSynthesis.cancel()
  const utterance = new SpeechSynthesisUtterance(text)
  utterance.lang = lang
  utterance.rate = 0.6
  utterance.pitch = 1
  utterance.volume = 1
  window.speechSynthesis.speak(utterance)
  return true
}

function BhaktiTab() {
  const [activeSection, setActiveSection] = useState('mantras')
  const [playingMantra, setPlayingMantra] = useState(null)
  const [playingBhajan, setPlayingBhajan] = useState(null)
  const [audioError, setAudioError] = useState(null)
  const [isPlaying, setIsPlaying] = useState(false)
  const audioRef = useRef(new Audio())
  
  // Cleanup audio on unmount
  useEffect(() => {
    return () => {
      audioRef.current.pause()
      audioRef.current = null
      window.speechSynthesis.cancel()
    }
  }, [])
  
  const playBhajan = (bhajan) => {
    setAudioError(null)
    setPlayingBhajan(bhajan.id)
    setIsPlaying(true)
    
    // Try to play audio file
    const audio = audioRef.current
    audio.src = bhajan.audioUrl
    audio.load()
    
    audio.play().then(() => {
      console.log('Playing audio:', bhajan.title)
    }).catch((error) => {
      console.warn('Audio file not found, using TTS fallback:', error)
      setAudioError(`🎵 Playing: ${bhajan.title} (Text-to-Speech)`)
      // Use TTS fallback
      playTTS(`${bhajan.title}. ${bhajan.meaning}`, 'te-IN')
    })
    
    audio.onended = () => {
      setPlayingBhajan(null)
      setIsPlaying(false)
    }
    
    audio.onerror = () => {
      setAudioError('🎵 Playing: ' + bhajan.title + ' (Text-to-Speech)')
      playTTS(`${bhajan.title}. ${bhajan.meaning}`, 'te-IN')
      setPlayingBhajan(null)
      setIsPlaying(false)
    }
  }
  
  const stopBhajan = () => {
    audioRef.current.pause()
    audioRef.current.currentTime = 0
    window.speechSynthesis.cancel()
    setPlayingBhajan(null)
    setIsPlaying(false)
    setAudioError(null)
  }
  
  const chantMantra = (mantra) => {
    setPlayingMantra(mantra.id)
    // Use TTS for chanting Sanskrit
    playTTS(mantra.sanskrit, 'sa-IN')
    
    // Reset after estimated duration
    setTimeout(() => {
      setPlayingMantra(null)
    }, 10000)
  }

  return (
    <div className="bhakti-container">
      <h2>🕉️ Spiritual Practices</h2>
      
      {/* Section Tabs */}
      <div className="section-tabs">
        <button 
          className={activeSection === 'mantras' ? 'active' : ''}
          onClick={() => setActiveSection('mantras')}
        >
          📿 Mantras
        </button>
        <button 
          className={activeSection === 'bhajans' ? 'active' : ''}
          onClick={() => setActiveSection('bhajans')}
        >
          🎵 Bhajans
        </button>
        <button 
          className={activeSection === 'routines' ? 'active' : ''}
          onClick={() => setActiveSection('routines')}
        >
          🌅 Daily Routines
        </button>
        <button 
          className={activeSection === 'about' ? 'active' : ''}
          onClick={() => setActiveSection('about')}
        >
          📖 About
        </button>
      </div>

      {/* Error/Status Message */}
      {audioError && (
        <div className="audio-status" onClick={stopBhajan}>
          {audioError}
          <span className="stop-hint">Click to stop</span>
        </div>
      )}

      {/* Mantras Section */}
      {activeSection === 'mantras' && (
        <div className="mantras-section">
          <p className="section-desc">Chant these powerful mantras for spiritual growth</p>
          <div className="mantras-grid">
            {DAILY_MANTRAS.map((mantra) => (
              <div key={mantra.id} className="mantra-card">
                <div className="mantra-header">
                  <h3>{mantra.name}</h3>
                  <span className="mantra-english">{mantra.englishName}</span>
                </div>
                
                <div className="mantra-content">
                  <div className="sanskrit-text">{mantra.sanskrit}</div>
                  <div className="telugu-text">{mantra.telugu}</div>
                  <div className="mantra-meaning">"{mantra.english}"</div>
                  <div className="mantra-benefit">✨ {mantra.benefit}</div>
                </div>
                
                <button 
                  className={`chant-btn ${playingMantra === mantra.id ? 'playing' : ''}`}
                  onClick={() => chantMantra(mantra)}
                  disabled={!!playingMantra}
                >
                  {playingMantra === mantra.id ? '🔊 Chanting...' : '🕉️ Chant with Me'}
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bhajans Section */}
      {activeSection === 'bhajans' && (
        <div className="bhajans-section">
          <p className="section-desc">Traditional Telugu devotional songs</p>
          
          {playingBhajan && (
            <div className="now-playing">
              <span className="playing-indicator">🔊 Now Playing:</span>
              <span>{TELUGU_BHAJANS.find(b => b.id === playingBhajan)?.title}</span>
              <button className="stop-btn" onClick={stopBhajan}>⏹️ Stop</button>
            </div>
          )}
          
          <div className="bhajans-grid">
            {TELUGU_BHAJANS.map((bhajan) => (
              <div key={bhajan.id} className="bhajan-card">
                <div className="bhajan-header">
                  <h3>{bhajan.title}</h3>
                  <span className="bhajan-deity">🙏 {bhajan.deity}</span>
                </div>
                
                <div className="bhajan-content">
                  <div className="bhajan-verse">{bhajan.verse}</div>
                  <div className="bhajan-meaning">"{bhajan.meaning}"</div>
                  <div className="bhajan-poet">📝 {bhajan.poet || 'Traditional'}</div>
                </div>
                
                <div className="bhajan-actions">
                  <button 
                    className={`play-btn ${playingBhajan === bhajan.id ? 'playing' : ''}`}
                    onClick={() => playBhajan(bhajan)}
                    disabled={isPlaying && playingBhajan !== bhajan.id}
                  >
                    {playingBhajan === bhajan.id ? '🔊 Playing...' : '🎵 Listen'}
                  </button>
                </div>
              </div>
            ))}
          </div>
          
          <div className="audio-note">
            💡 Note: If audio files are not available, the lyrics will be read using text-to-speech.
          </div>
        </div>
      )}

      {/* Daily Routines Section */}
      {activeSection === 'routines' && (
        <div className="routines-section">
          {/* Morning */}
          <div className="routine-card morning">
            <h3>🌅 Morning Practices</h3>
            <p className="routine-intro">Begin your day with divine connection</p>
            {SPIRITUAL_ROUTINES.morning.map((item, i) => (
              <div key={i} className="routine-item">
                <span className="routine-practice">{item.practice}</span>
                <span className="routine-english">({item.english})</span>
                <span className="routine-duration">{item.duration}</span>
                <span className="routine-benefit">✨ {item.benefit}</span>
              </div>
            ))}
          </div>
          
          {/* Evening */}
          <div className="routine-card evening">
            <h3>🌙 Evening Practices</h3>
            <p className="routine-intro">End your day with gratitude and peace</p>
            {SPIRITUAL_ROUTINES.evening.map((item, i) => (
              <div key={i} className="routine-item">
                <span className="routine-practice">{item.practice}</span>
                <span className="routine-english">({item.english})</span>
                <span className="routine-duration">{item.duration}</span>
                <span className="routine-benefit">✨ {item.benefit}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* About Section */}
      {activeSection === 'about' && (
        <div className="about-section">
          <div className="about-card">
            <h3>📿 About Mantras</h3>
            <p>Mantras are sacred sounds, syllables, or phrases that carry spiritual energy. Regular chanting brings peace, clarity, and divine connection.</p>
            
            <h3>🎵 About Bhajans</h3>
            <p>Bhajans are devotional songs sung in praise of the divine. They express love for God and help cultivate devotion (bhakti).</p>
            
            <h3>🌅 Morning Routine</h3>
            <p>Start your day with Gayatri Mantra for wisdom, Surya Namaskar for energy, and a moment of gratitude.</p>
            
            <h3>🌙 Evening Routine</h3>
            <p>End with devotional singing, meditation, and reflection on blessings received.</p>
            
            <div className="safety-note">
              <h4>🙏🙏🙏</h4>
              <p>Always chant with a pure heart and sincere intention. The vibration of the mantra is more important than perfect pronunciation.</p>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default BhaktiTab
