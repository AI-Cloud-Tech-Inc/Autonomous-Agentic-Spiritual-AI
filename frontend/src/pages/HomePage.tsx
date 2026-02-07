import { Link } from "react-router-dom";

function HomePage() {
  return (
    <main style={{ maxWidth: 640, margin: "80px auto", padding: "0 24px", textAlign: "center" }}>
      <h1 style={{ fontFamily: "var(--font-display)", fontSize: "2rem", marginBottom: 16 }}>
        Spiritual AI
      </h1>
      <p style={{ color: "var(--color-text-muted)", marginBottom: 32 }}>
        A mindful companion for inner growth, reflection, and well-being.
      </p>
      <Link
        to="/chat"
        style={{
          display: "inline-block",
          padding: "12px 32px",
          backgroundColor: "var(--color-primary)",
          color: "#fff",
          borderRadius: 8,
          textDecoration: "none",
        }}
      >
        Begin a Session
      </Link>
    </main>
  );
}

export default HomePage;
