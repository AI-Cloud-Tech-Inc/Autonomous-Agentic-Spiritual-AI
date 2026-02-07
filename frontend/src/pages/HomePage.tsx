import { Link } from 'react-router-dom'

function HomePage() {
  return (
    <div style={{ padding: '48px', maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
      <h1 style={{ fontSize: '32px', marginBottom: '16px', color: '#5c6bc0' }}>
        Autonomous Agentic Spiritual AI
      </h1>
      <p style={{ fontSize: '18px', color: '#757575', marginBottom: '48px' }}>
        Your companion for inner growth, reflection, and well-being
      </p>
      
      <div style={{ display: 'flex', gap: '24px', justifyContent: 'center', flexWrap: 'wrap' }}>
        <Link to="/chat">
          <button className="primary" style={{ padding: '16px 32px', fontSize: '18px' }}>
            Start a Conversation
          </button>
        </Link>
      </div>

      <div style={{ marginTop: '64px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '24px' }}>
        <div style={{ padding: '24px', background: '#fff', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }}>
          <h3 style={{ color: '#5c6bc0', marginBottom: '8px' }}>Mindfulness</h3>
          <p style={{ color: '#757575', fontSize: '14px' }}>Guided practices for present-moment awareness</p>
        </div>
        <div style={{ padding: '24px', background: '#fff', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }}>
          <h3 style={{ color: '#26a69a', marginBottom: '8px' }}>Reflection</h3>
          <p style={{ color: '#757575', fontSize: '14px' }}>Thought-provoking questions for self-discovery</p>
        </div>
        <div style={{ padding: '24px', background: '#fff', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }}>
          <h3 style={{ color: '#ff7043', marginBottom: '8px' }}Guidance</h3>
          <p style={{ color: '#757575', fontSize: '14px' }}>Non-dogmatic support for your spiritual journey</p>
        </div>
      </div>
    </div>
  )
}

export default HomePage
